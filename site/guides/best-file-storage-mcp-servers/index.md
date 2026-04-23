# Best File & Storage MCP Servers in 2026 — Local Filesystem vs Cloud Storage vs Enterprise Platforms

> We compared 35+ file and storage MCP servers across local filesystem, Google Drive, AWS S3, Dropbox, OneDrive, Box, MinIO, and multi-cloud options. Updated April 2026 with official Google Drive, Microsoft Work IQ, and Dropbox remote servers.


File and storage MCP servers let AI assistants read, write, search, and manage files — whether on your local machine, in cloud storage, or across enterprise platforms. This is one of the most fundamental MCP categories: almost every AI workflow touches files somewhere.

The ecosystem splits into two worlds. **Local filesystem servers** give AI agents controlled access to files on your machine — sandboxed by directory allowlists. **Cloud storage servers** connect to Google Drive, S3, Dropbox, OneDrive, Box, and other platforms via their APIs. The security models are completely different, and picking the wrong one can expose sensitive data.

What surprised us: the landscape flipped in a single month. Google, Microsoft, and Dropbox all shipped official MCP servers in March–April 2026, joining AWS, Box, and MinIO. The era of "community fills the gaps" is ending — but the security story got worse, with Anthropic's own filesystem server hit by sandbox escape CVEs.

## What Changed (March → April 2026)

| Server | March 2026 | April 2026 | Change |
|--------|-----------|------------|--------|
| **Official Filesystem** | 81,700 stars | 84,300 stars | CVE-2025-53109/53110 sandbox escape discovered + patched |
| **Google Drive** | No official server | **Google Official Drive MCP (NEW)** | 7 tools, managed remote, Developer Preview |
| **taylorwilsdon/google_workspace_mcp** | 1,900 stars, 10 services | 2,200 stars, 12 services | +Apps Script, Search; stateless mode fix |
| **Microsoft OneDrive/SharePoint** | Deprecated official | **Work IQ OneDrive + SharePoint (NEW)** | 14 + 33 tools, separate servers |
| **Dropbox** | No official file server | **Dropbox Remote MCP (NEW)** | Beta at mcp.dropbox.com, DCR auth |
| **Box** | 97 stars | 100 stars | Multi-transport (STDIO + HTTP + SSE) |
| **awslabs/mcp** | 8,500 stars | 8,800 stars | Removed SSE, Streamable HTTP only |
| **mark3labs/mcp-filesystem-server** | 619 stars | 633 stars | Steady growth |
| **ftaricano/mcp-onedrive-sharepoint** | — | 5 stars | Graph helpers, working auth flow |

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Local filesystem** | [Official Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | 84,300 (monorepo) | [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) (633, Go) |
| **Google Drive / Workspace** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 2,200 | [Google Official Drive MCP](https://developers.google.com/workspace/guides/configure-mcp-servers) (managed remote, NEW) |
| **AWS S3** | [aws-samples/sample-mcp-server-s3](https://github.com/aws-samples/sample-mcp-server-s3) | 80 | [txn2/mcp-s3](https://github.com/txn2/mcp-s3) (Go, multi-account) |
| **Dropbox** | [Dropbox Official Remote MCP](https://help.dropbox.com/integrations/connect-dropbox-mcp-server) | Beta (NEW) | [amgadabdelhafez/dbx-mcp-server](https://github.com/amgadabdelhafez/dbx-mcp-server) (27, self-hosted) |
| **OneDrive / SharePoint** | [Work IQ OneDrive + SharePoint](https://learn.microsoft.com/en-us/microsoft-agent-365/tooling-servers-overview) | Official (NEW) | [ftaricano/mcp-onedrive-sharepoint](https://github.com/ftaricano/mcp-onedrive-sharepoint) (5, self-hosted) |
| **Box** | [box-community/mcp-server-box](https://github.com/box-community/mcp-server-box) | 100 | [box/mcp-server-box-remote](https://github.com/box/mcp-server-box-remote) (hosted) |
| **MinIO / S3-compatible** | [minio/mcp-server-aistor](https://github.com/minio/mcp-server-aistor) | 39 | [ucesys/minio-python-mcp](https://github.com/ucesys/minio-python-mcp) (4) |
| **FTP / SFTP** | [alxspiker/mcp-server-ftp](https://github.com/alxspiker/mcp-server-ftp) | 16 | [gradyyoung/sftp-ssh-mcp](https://github.com/gradyyoung/sftp-ssh-mcp) (6) |
| **Multi-cloud (universal)** | [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) | 34 | — |

## Local Filesystem Servers

These give AI agents controlled access to files on your machine. They're the foundation of most MCP setups — reading code, editing configs, managing project files.

### Official Filesystem — The Winner

**Stars:** 84,300 (monorepo) | **Language:** TypeScript | **License:** MIT

The reference implementation from Anthropic, included in the [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) monorepo. It's the default filesystem server recommended by most MCP clients and the one most developers start with.

**What makes it stand out:**
- **14 tools** — read_text_file, write_file, edit_file, create_directory, list_directory, search_files, directory_tree, get_file_info, move_file, list_allowed_directories
- **Directory allowlisting** — only directories you explicitly pass via CLI args (or via MCP Roots protocol) are accessible
- **Dynamic access control** — supports the MCP Roots protocol for runtime directory access changes without restarting
- **Battle-tested** — used by Claude Desktop, VS Code, and most MCP clients out of the box

**⚠️ Security alert (patched):** In mid-2025, Cymulate Research Labs disclosed two critical sandbox escape vulnerabilities:
- **CVE-2025-53110** (directory containment bypass) — the server used naive `path.startsWith()` validation, allowing access via directories with similar name prefixes (e.g., `/tmp/allowed_dir_evil` bypasses `/tmp/allowed_dir`)
- **CVE-2025-53109** (symlink bypass to code execution) — crafted symlinks bypass the access enforcement mechanism entirely, granting full read/write to the entire filesystem
Both were patched in version 2025.7.1. **If you're running an older version, update immediately.** These CVEs demonstrate that even the reference implementation from the protocol's creators can have fundamental security flaws.

**Limitations:**
- Read-only for files outside allowed directories, but full read/write within them — no granular per-tool permissions
- No binary file support (images, PDFs, etc.)
- TypeScript/Node.js dependency
- Historical sandbox escape CVEs — always run the latest version

**Best for:** Most developers. Start here unless you have a specific reason not to. Verify you're on version 2025.7.1 or later.

### mark3labs/mcp-filesystem-server — Go Alternative

**Stars:** 633 | **Language:** Go | **License:** MIT

A Go reimplementation of the official filesystem server. Single binary, no Node.js dependency. Docker image available.

**What makes it stand out:**
- **Single binary deployment** — download and run, no runtime needed
- **Content search** — search within file contents, not just filenames
- **Symlink resolution** — follows symlinks safely with path traversal prevention
- **Docker support** — mount directories as volumes for containerized deployments

**Limitations:**
- Fewer community resources and examples compared to the official server
- No MCP Roots protocol support

**Best for:** Teams that prefer Go binaries over Node.js, or need containerized filesystem access.

### cyanheads/filesystem-mcp-server — HTTP + JWT Auth

**Stars:** 34 | **Language:** TypeScript | **License:** Apache 2.0

Adds HTTP transport with JWT authentication on top of standard filesystem operations. Supports both STDIO and HTTP modes.

**Best for:** Teams that need remote filesystem access with authentication — useful for shared development servers.

## Google Drive / Workspace

The Google Drive MCP story transformed in March–April 2026. Google shipped official managed remote MCP servers for Workspace, filling the #1 gap we flagged in our original guide. Meanwhile, taylorwilsdon's community server continues to lead on features and flexibility.

### Google Official Drive MCP — NEW

**Type:** Managed remote | **Auth:** OAuth 2.0 | **Status:** Developer Preview

Google now ships fully-managed, remote MCP servers for Workspace as part of the [Google Workspace Developer Preview Program](https://developers.google.com/workspace/guides/configure-mcp-servers). No self-hosting needed — Google runs the infrastructure.

**What makes it stand out:**
- **7 tools** — create_file, download_file_content, get_file_metadata, get_file_permissions, list_recent_files, read_file_content, search_files
- **Managed remote** — Google hosts it, no server to run or maintain
- **Part of a suite** — alongside Gmail (10 tools), Calendar (8 tools), Chat (2 tools), and People API (3 tools)
- **Enterprise-ready** — built on Google's existing API infrastructure with global endpoints

**Limitations:**
- Developer Preview — not yet GA, may change
- Fewer tools than taylorwilsdon's community server (7 vs 12+ services)
- Requires Google Cloud project with OAuth 2.0 credentials
- No Docs/Sheets/Slides editing — just Drive file operations

**Best for:** Teams that want official Google backing and managed infrastructure. If you only need Drive file operations (read, write, search), this is now the safest choice.

### taylorwilsdon/google_workspace_mcp — The Community Winner

**Stars:** 2,200 | **Language:** Python | **License:** MIT

Still the most comprehensive Google Workspace MCP server, now covering **12 services**: Gmail, Drive, Calendar, Docs, Sheets, Slides, Forms, Chat, Apps Script, Tasks, Contacts, and Search.

**What makes it stand out:**
- **12 services** — the full Workspace suite in one server, including Apps Script and Search (new since March)
- **OAuth 2.1** — modern authentication with multi-user bearer token support for organizations
- **Streamable HTTP mode** — recommended modern transport for MCP clients
- **Stateless mode** — fixed in recent updates to properly reach FastMCP's stateless_http runtime flag. Before this fix, the app advertised stateless behavior while FastMCP still kept in-memory sessions
- **1,954 commits** — heavily maintained with active development
- **Tiered access levels** — core, extended, and complete tool sets plus granular permissions and read-only mode
- **Re-auth improvements** — now uses `select_account` when user already has required scopes instead of forcing consent; preserves existing refresh token when Google omits it on reauth

**Limitations:**
- Requires a Google Cloud project with OAuth credentials configured — the setup isn't trivial
- Large surface area means more potential attack surface
- Python dependency

**Best for:** Anyone who needs more than just Drive — Gmail, Calendar, Docs editing, Sheets, etc. The breadth of 12 services in one server means you won't need separate servers. Choose this over the official server when you need the full Workspace suite.

### felores/gdrive-mcp-server — Lightweight Read-Only

**Stars:** 67 | **Language:** JavaScript | **License:** MIT

A minimal Google Drive server with just two tools: `gdrive_search` and `gdrive_read_file`. Enforces read-only scopes — the AI can search and read but never modify or delete files.

**What makes it stand out:**
- **Read-only by design** — uses `drive.readonly` scope. Cannot modify files even if the AI tries
- **Auto-conversion** — Google Docs to Markdown, Sheets to CSV, Slides to plain text
- **Simple setup** �� fewer moving parts than the full Workspace server

**Best for:** Teams that want AI assistants to reference Google Drive documents without any write risk.

### Other Google Drive Options

- **[a-bonus/google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** — Full Google Docs editing with formatting support (bold, italic, headers). The only option if you need to write and format Docs, not just read them
- **[distrihub/mcp-google-workspace](https://github.com/distrihub/mcp-google-workspace)** — Rust implementation covering Drive and Sheets. Choose this if you want Rust's performance and safety guarantees

## AWS S3

AWS has official MCP presence, but the S3 story is fragmented across multiple repos.

### aws-samples/sample-mcp-server-s3 — The Winner

**Stars:** 80 | **Language:** Python | **License:** MIT-0

An official AWS sample demonstrating S3 access via MCP. Three tools: ListBuckets, ListObjectsV2, and GetObject. Supports PDF document retrieval.

**What makes it stand out:**
- **Official AWS** — maintained under aws-samples, follows AWS best practices
- **PDF support** — can retrieve and surface PDF content from S3
- **Simple and auditable** — small codebase, easy to review for security

**Limitations:**
- Read-only — no upload, delete, or copy operations
- Minimal tool set — just list and get
- Requires AWS credentials configured locally

**Best for:** Teams that need safe, read-only S3 access from AI agents. The official backing and limited scope make it a secure choice.

### txn2/mcp-s3 — Multi-Account Go Server

**Stars:** 1 | **Language:** Go | **License:** Apache 2.0

A Go-based S3 server with broader capabilities and safety controls.

**What makes it stand out:**
- **9 tools** — list buckets/objects, get/put/delete/copy objects, presigned URLs, multi-account connections
- **Multi-account support** — switch between AWS accounts via `s3_list_connections`
- **Safety controls** — write and delete disabled by default, must be explicitly enabled via flags
- **S3-compatible** — works with SeaweedFS and other S3-compatible object stores

**Best for:** Teams managing files across multiple AWS accounts or S3-compatible stores who want granular safety controls.

### samuraikun/aws-s3-mcp — TypeScript with Multiple Transports

**Stars:** 23 | **Language:** TypeScript | **License:** MIT

Supports STDIO, HTTP, and streamable HTTP transports. Handles both text and binary file retrieval with prefix filtering. MinIO compatible.

**Best for:** Teams that need HTTP/SSE transport for remote S3 access.

### AWS Official S3 Tables

The [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (8,800 stars) includes an S3 Tables MCP server for table-formatted S3 data. It's specialized for structured data queries, not general file management. Note: as of May 2025, AWS removed SSE transport support from all their MCP servers, moving to Streamable HTTP only.

## Dropbox

Dropbox transformed its MCP story in April 2026 by shipping an official remote MCP server with full file management capabilities. This fills the gap we flagged in March.

### Dropbox Official Remote MCP — The Winner (NEW)

**Type:** Managed remote (Beta) | **Endpoint:** mcp.dropbox.com | **Auth:** OAuth + Dynamic Client Registration

Dropbox now hosts an official remote MCP server at `mcp.dropbox.com` with file management built in — no self-hosting required.

**What makes it stand out:**
- **Full file operations** — upload, download, list, delete, search, sharing links, account info
- **Dynamic Client Registration (DCR)** — frictionless auth for supported MCP clients, no pre-registration needed
- **Zero infrastructure** — Dropbox runs it for you, just point your MCP client at the endpoint
- **Works with major clients** — Claude, Cursor, ChatGPT, and any MCP-compatible app

**Limitations:**
- Beta — may have restricted functionality and additional terms
- DCR only supports a "trusted set" of MCP clients currently, with more being added
- No chunked uploads for very large files (community servers still win here)

**Best for:** Most teams that need Dropbox access from AI agents. Start here unless you need large file support or self-hosted control.

### amgadabdelhafez/dbx-mcp-server — Self-Hosted Alternative

**Stars:** 27 | **Language:** TypeScript | **License:** MIT

The most complete community Dropbox file management server, with full CRUD operations and sharing. Still relevant for teams that need self-hosted control.

**What makes it stand out:**
- **Full file operations** — list, upload, download, delete, copy, move, create folders
- **Sharing** — create and manage sharing links
- **Search and metadata** — search files and retrieve detailed metadata
- **OAuth 2.0 with PKCE** — modern, secure authentication flow

**Best for:** Teams that want self-hosted Dropbox access or need features not yet in the official beta.

### ngs/dropbox-mcp-server — Large Files + Version History

**Stars:** 3 | **Language:** Go | **License:** MIT

A Go implementation with 17+ tools, including features neither the official nor TypeScript server offers.

**What makes it stand out:**
- **Chunked uploads** — handles files over 150MB that would fail with standard upload
- **Version history** — browse revision history and restore previous versions
- **Shared link management** — create, list, and revoke shared links

**Best for:** Teams working with large files or needing version control within Dropbox.

### Dropbox Dash MCP — Enterprise Search

Dropbox also offers a separate **Dash remote MCP server** (updated April 14, 2026) and a **local Dash MCP server** for AI-powered search across connected services. The original `dropbox/mcp-server-dash` (9 stars, Python) provides `dash_company_search` and `dash_get_file_details`. These focus on search and context, not file management — use the main Dropbox remote MCP for file operations.

## OneDrive / SharePoint

Microsoft completely revamped its MCP story in March 2026. The old combined OneDrive/SharePoint server was deprecated on March 13, replaced by separate **Work IQ** servers with dramatically more capabilities. This fills the #2 gap we flagged in our original guide.

### Work IQ OneDrive — The Winner (NEW)

**Type:** Managed remote (Preview) | **Server ID:** mcp_OneDriveRemoteServer | **Requires:** M365 Copilot license

Microsoft's official OneDrive MCP server with 14 tools for personal OneDrive file management.

**What makes it stand out:**
- **14 tools** — getOnedrive, getFolderChildrenInMyOnedrive, findFileOrFolderInMyDrive, getFileOrFolderMetadata (by ID or URL), readSmallTextFile, createSmallTextFile, createFolder, renameFileOrFolder, deleteFileOrFolder, moveSmallFile, shareFileOrFolder, setSensitivityLabelOnFile
- **Concurrency control** — eTags on delete/rename/move operations prevent conflicts in concurrent editing
- **Sensitivity labels** — apply/remove Microsoft Information Protection labels with audit justification
- **Sharing** — role-based invitations (read, write) with email notifications

**Limitations:**
- **Requires M365 Copilot license** (~$30/user/month) — not free
- File operations limited to ≤5MB — no large file support
- Preview — tool names and parameters may change
- Folder listing capped at 20 items per call

**Best for:** Enterprise Microsoft 365 teams with Copilot licenses who need official, managed OneDrive access.

### Work IQ SharePoint — NEW

**Type:** Managed remote (Preview) | **Server ID:** mcp_SharePointRemoteServer | **Requires:** M365 Copilot license

Microsoft's official SharePoint MCP server with a massive 33 tools covering files, folders, lists, columns, and sharing.

**What makes it stand out:**
- **33 tools** — site discovery (findSite, getSiteByPath, listSubsites), document libraries (list, get default), file operations (create/read/delete/rename/move/copy text and binary files), folder management, async operations (copyFileOrFolder + checkOperationStatus), list operations (CRUD for lists, items, columns), sharing with roles, sensitivity labels
- **Binary file support** — read and create binary files via base64 encoding (unique among the Work IQ file servers)
- **Cross-library copy** — async file/folder copy across different document libraries
- **Full list management** — create lists from templates, manage columns with 20+ types, CRUD list items
- **Upload from URL** — copy files directly from SharePoint/OneDrive URLs

**Limitations:**
- **Requires M365 Copilot license** (~$30/user/month)
- File operations limited to ≤5MB
- Move operations only within the same document library
- Preview — may change

**Best for:** SharePoint-heavy organizations that need AI agents to manage sites, document libraries, lists, and files.

### ftaricano/mcp-onedrive-sharepoint — Self-Hosted Alternative

**Stars:** 5 | **Language:** TypeScript | **License:** —

The community option covering OneDrive, SharePoint, and Excel in one self-hosted server. Recent updates include working ESLint config, executable tests, reusable Graph helpers, and fixed `npm run setup-auth`.

**What makes it stand out:**
- **32 tools** — file management, SharePoint list CRUD, and Excel-specific tools with formula support
- **Device Code Flow** — user-friendly authentication with auto-refresh
- **Excel integration** — read/write cells, create charts, manage worksheets. Unique among storage servers
- **No Copilot license required** — works with standard M365 licenses via Microsoft Graph API
- **CLI tool** — also usable as a standalone `ods` CLI for shell scripting

**Limitations:**
- Small community (5 stars, single maintainer)
- Self-hosted — you manage the server

**Best for:** Teams that can't justify the Copilot license cost, need Excel integration, or want self-hosted control.

### Other Microsoft Options

- **[SAIB-Inc/Helix](https://github.com/SAIB-Inc/Helix)** — .NET 10 implementation covering email, calendar, SharePoint sites/lists/documents. Good for .NET shops
- **[godwin3737/mcp-server-microsoft365-filesearch](https://github.com/godwin3737/mcp-server-microsoft365-filesearch)** (11 stars) — Python, search-focused with local file caching. Uses Microsoft Graph API
- **[pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server)** — Wraps the entire CLI for Microsoft 365. Natural language execution of any M365 CLI command

## Box

Box stands out as the enterprise storage provider with the best MCP support — both self-hosted and cloud-hosted official servers.

### box-community/mcp-server-box — The Winner

**Stars:** 100 | **Language:** Python | **License:** MIT

The official self-hosted Box MCP server with enterprise-grade features.

**What makes it stand out:**
- **13 tool categories** — file/folder operations, collaboration, document generation, metadata, search, shared links, task assignments, user/group management, web links
- **AI-powered queries** — ask natural language questions about file content, powered by Box AI
- **Enterprise auth** — supports OAuth 2.0, CCG (Client Credentials Grant), JWT, and MCP client auth
- **Multiple transports** — stdio, SSE, and HTTP

**Limitations:**
- Requires a Box account with API access (enterprise plans for full features)
- Self-hosted — you run and maintain the server

**Best for:** Enterprise teams on Box who need the full range of file operations and AI-powered content queries.

### box/mcp-server-box-remote — Cloud Hosted

**Stars:** 1 | **License:** MIT

The official remote/cloud-hosted alternative at mcp.box.com. No self-hosting needed.

**What makes it stand out:**
- **Zero infrastructure** — Box runs it for you
- **Box AI integration** — Q&A against file content
- **GitHub MCP registry** — listed in the official registry for easy discovery

**Best for:** Teams that want Box MCP access without managing a server.

## MinIO / S3-Compatible Storage

### minio/mcp-server-aistor — The Winner

**Stars:** 39 | **Language:** Containerized | **License:** —

The official MinIO MCP server with an impressive 30+ tools and granular permission controls.

**What makes it stand out:**
- **30+ tools** — read (list buckets/objects, metadata, tagging, presigned URLs), write (bucket creation, uploads), delete, AI queries, admin (cluster health, storage metrics)
- **AI-powered queries** — ask questions about object content. Unique among object storage servers
- **Granular safety flags** — `--allow-write`, `--allow-delete`, `--allow-admin` must be explicitly set. Read-only by default
- **StreamableHTTP transport** — modern transport protocol

**Limitations:**
- Docker/Podman required — no standalone binary
- MinIO-specific — works with MinIO, not generic S3

**Best for:** MinIO users who want comprehensive AI-assisted object storage management with strong safety defaults.

## FTP / SFTP

Legacy protocols, but still widely used. Options are limited but functional.

### alxspiker/mcp-server-ftp — The Winner

**Stars:** 16 | **Language:** TypeScript | **License:** MIT

The most complete FTP-specific MCP server.

**Tools:** list-directory, download-file, upload-file, create-directory, delete-file, delete-directory. Supports FTPS (TLS) via the `FTP_SECURE` flag.

**Best for:** Teams that still manage files over FTP/FTPS and want AI agent access.

### gradyyoung/sftp-ssh-mcp — SFTP + SSH

**Stars:** 6 | **Language:** JavaScript | **License:** MIT

Combines SFTP file transfer with SSH shell command execution. Supports password and private key authentication.

**Best for:** Teams that need both file transfer and remote command execution on Linux/Windows servers.

## Multi-Cloud / Universal Storage

### Xuanwo/mcp-server-opendal — The Universal Adapter

**Stars:** 34 | **Language:** Python | **License:** Apache 2.0

Built on [Apache OpenDAL](https://github.com/apache/opendal), this server provides unified access to **S3, Azure Blob Storage, Google Cloud Storage, and 40+ other storage backends** through a single MCP server.

**What makes it stand out:**
- **40+ backends** — S3, Azure Blob, GCS, HDFS, WebDAV, FTP, SFTP, local filesystem, and more. One server to rule them all
- **Auto text/binary detection** — handles both content types without configuration
- **Unified API** — same tools work regardless of backend

**Limitations:**
- Read-focused — listing and reading only, limited write support
- Configuration requires knowing OpenDAL's env var patterns
- Smaller community than provider-specific servers

**Best for:** Teams working across multiple storage providers who want a single MCP server instead of configuring one per service.

## Decision Flowchart

**Do you need local file access?**

→ **Standard setup** → Official Filesystem (modelcontextprotocol/servers) — verify v2025.7.1+ for security patches

→ **Go binary / Docker** → mark3labs/mcp-filesystem-server

→ **Remote with auth** → cyanheads/filesystem-mcp-server (HTTP + JWT)

**Do you need Google Drive?**

→ **Just Drive files (read/write/search)** → Google Official Drive MCP (managed remote, NEW)

→ **Full Workspace (Drive + Gmail + Calendar + 9 more)** → taylorwilsdon/google_workspace_mcp

→ **Read-only Drive access** → felores/gdrive-mcp-server

→ **Google Docs editing with formatting** → a-bonus/google-docs-mcp

**Do you need AWS S3?**

→ **Safe, read-only** → aws-samples/sample-mcp-server-s3 (official)

→ **Full CRUD + multi-account** → txn2/mcp-s3

→ **S3-compatible (MinIO, SeaweedFS)** → txn2/mcp-s3 or minio/mcp-server-aistor

**Do you need Dropbox?**

→ **Standard file management** → Dropbox Official Remote MCP (mcp.dropbox.com, NEW)

→ **Self-hosted control** → amgadabdelhafez/dbx-mcp-server

→ **Large files + version history** → ngs/dropbox-mcp-server

**Do you need OneDrive / SharePoint?**

→ **Have M365 Copilot license?** → Work IQ OneDrive + Work IQ SharePoint (official, NEW)

→ **No Copilot license / need Excel** → ftaricano/mcp-onedrive-sharepoint (self-hosted)

→ **Broad M365 coverage (.NET)** → SAIB-Inc/Helix

**Do you need Box?**

→ **Self-hosted with AI queries** → box-community/mcp-server-box (official)

→ **Zero infrastructure** → box/mcp-server-box-remote (official hosted)

**Do you need multiple cloud providers?**

→ Xuanwo/mcp-server-opendal (40+ backends, one server)

## Three Trends Shaping This Space

### 1. The official vendor wave arrived — and it's real

In a single month (March–April 2026), Google, Microsoft, and Dropbox all shipped official MCP servers for their storage platforms. This is a dramatic reversal from our March assessment where we flagged Google Drive and OneDrive/SharePoint as the two biggest gaps. Now every major cloud storage provider except Apple has at least one official MCP server. The era of relying entirely on community implementations for major platforms is ending — though community servers remain superior for feature breadth (taylorwilsdon's 12-service Workspace server vs. Google's 5-server suite).

### 2. File MCP security is proven broken

Anthropic's own filesystem server — the reference implementation used by most MCP setups — had critical sandbox escape vulnerabilities (CVE-2025-53109, CVE-2025-53110). A naive `startsWith()` path check and missing symlink validation let attackers escape the directory sandbox entirely. Across the broader ecosystem, 82% of file-operation MCP servers are vulnerable to path traversal. This isn't theoretical — these are the specific patterns that file storage servers exhibit. Run the latest versions, use containers, and verify your path validation.

### 3. Managed remote is becoming the default

Google, Microsoft, and Dropbox all chose managed remote hosting for their official servers — you point your MCP client at an endpoint, no server to run. This matches the broader MCP trend away from local STDIO toward Streamable HTTP. The trade-off: you gain zero-maintenance deployment but lose self-hosted control and often face licensing costs (Microsoft requires M365 Copilot at ~$30/user/month). For enterprises, this is the right model. For individual developers, community self-hosted servers remain more flexible and free.

## What's Missing

- ~~No maintained official Google Drive MCP server~~ — **FILLED (April 2026).** Google shipped managed remote MCP servers for Workspace including Drive (7 tools). Developer Preview, not yet GA
- ~~No official OneDrive/SharePoint MCP server~~ — **FILLED (March 2026).** Microsoft shipped Work IQ OneDrive (14 tools) and Work IQ SharePoint (33 tools). Requires M365 Copilot license
- ~~No official Dropbox file management server~~ — **FILLED (April 2026).** Dropbox shipped remote MCP server (Beta) at mcp.dropbox.com with full file operations
- **No iCloud MCP server** — Apple's ecosystem is completely absent from the MCP world. No official or community implementation exists
- **No Backblaze B2 MCP server** — popular S3-compatible storage with no dedicated MCP support (OpenDAL covers it generically)
- **No file sync/conflict resolution** — no MCP server handles bidirectional file sync between local and cloud storage
- **File MCP security is fundamentally weak** — 82% of file-operation MCP servers vulnerable to path traversal, reference implementation had sandbox escape CVEs, no standard approach to path validation across the ecosystem
- **5MB file limits on official servers** — Microsoft Work IQ limits all file operations to ≤5MB. Community servers handle larger files but lack official backing
- **No file preview/transformation** — no server generates thumbnails, converts formats, or previews documents. AI agents get raw content or nothing

