# Best File & Storage MCP Servers in 2026 — Local Filesystem vs Cloud Storage vs Enterprise Platforms

> We compared 30+ file and storage MCP servers across local filesystem, Google Drive, AWS S3, Dropbox, OneDrive, Box, MinIO, and multi-cloud options.


File and storage MCP servers let AI assistants read, write, search, and manage files — whether on your local machine, in cloud storage, or across enterprise platforms. This is one of the most fundamental MCP categories: almost every AI workflow touches files somewhere.

The ecosystem splits into two worlds. **Local filesystem servers** give AI agents controlled access to files on your machine — sandboxed by directory allowlists. **Cloud storage servers** connect to Google Drive, S3, Dropbox, OneDrive, Box, and other platforms via their APIs. The security models are completely different, and picking the wrong one can expose sensitive data.

What surprised us: several major providers (AWS, Box, MinIO) now ship official MCP servers, while others (Google, Microsoft) have either archived or deprecated theirs. The community has filled most gaps, but quality varies widely.

**Disclosure:** Our recommendations are based on research — analyzing documentation, GitHub repositories, community feedback, and published benchmarks. We have not hands-on tested every server in this guide.

## At a Glance: Top Picks

| Category | Our pick | Stars | Runner-up |
|----------|----------|-------|-----------|
| **Local filesystem** | [Official Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) | 81,700 (monorepo) | [mark3labs/mcp-filesystem-server](https://github.com/mark3labs/mcp-filesystem-server) (619, Go) |
| **Google Drive / Workspace** | [taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp) | 1,900 | [felores/gdrive-mcp-server](https://github.com/felores/gdrive-mcp-server) (66, read-only) |
| **AWS S3** | [aws-samples/sample-mcp-server-s3](https://github.com/aws-samples/sample-mcp-server-s3) | 77 | [txn2/mcp-s3](https://github.com/txn2/mcp-s3) (Go, multi-account) |
| **Dropbox** | [amgadabdelhafez/dbx-mcp-server](https://github.com/amgadabdelhafez/dbx-mcp-server) | 26 | [ngs/dropbox-mcp-server](https://github.com/ngs/dropbox-mcp-server) (Go, chunked uploads) |
| **OneDrive / SharePoint** | [ftaricano/mcp-onedrive-sharepoint](https://github.com/ftaricano/mcp-onedrive-sharepoint) | — | [SAIB-Inc/Helix](https://github.com/SAIB-Inc/Helix) (.NET, broad M365) |
| **Box** | [box-community/mcp-server-box](https://github.com/box-community/mcp-server-box) | 97 | [box/mcp-server-box-remote](https://github.com/box/mcp-server-box-remote) (hosted) |
| **MinIO / S3-compatible** | [minio/mcp-server-aistor](https://github.com/minio/mcp-server-aistor) | 39 | [ucesys/minio-python-mcp](https://github.com/ucesys/minio-python-mcp) (4) |
| **FTP / SFTP** | [alxspiker/mcp-server-ftp](https://github.com/alxspiker/mcp-server-ftp) | 16 | [gradyyoung/sftp-ssh-mcp](https://github.com/gradyyoung/sftp-ssh-mcp) (6) |
| **Multi-cloud (universal)** | [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) | 34 | — |

## Local Filesystem Servers

These give AI agents controlled access to files on your machine. They're the foundation of most MCP setups — reading code, editing configs, managing project files.

### Official Filesystem — The Winner

**Stars:** 81,700 (monorepo) | **Language:** TypeScript | **License:** MIT

The reference implementation from Anthropic, included in the [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) monorepo. It's the default filesystem server recommended by most MCP clients and the one most developers start with.

**What makes it stand out:**
- **14 tools** — read_text_file, write_file, edit_file, create_directory, list_directory, search_files, directory_tree, get_file_info, move_file, list_allowed_directories
- **Directory allowlisting** — only directories you explicitly pass via CLI args (or via MCP Roots protocol) are accessible. The AI agent can't escape the sandbox
- **Dynamic access control** — supports the MCP Roots protocol for runtime directory access changes without restarting
- **Battle-tested** — used by Claude Desktop, VS Code, and most MCP clients out of the box

**Limitations:**
- Read-only for files outside allowed directories, but full read/write within them — no granular per-tool permissions
- No binary file support (images, PDFs, etc.)
- TypeScript/Node.js dependency

**Best for:** Most developers. Start here unless you have a specific reason not to.

### mark3labs/mcp-filesystem-server — Go Alternative

**Stars:** 619 | **Language:** Go | **License:** MIT

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

Google hasn't shipped a maintained official MCP server. Anthropic's reference implementation was archived. The community has filled the gap with a standout option.

### taylorwilsdon/google_workspace_mcp — The Winner

**Stars:** 1,900 | **Language:** Python | **License:** MIT

The most comprehensive Google Workspace MCP server. Covers not just Drive but Gmail, Calendar, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat — the full suite.

**What makes it stand out:**
- **Full Workspace coverage** — 10+ Google services in one server. If you need Drive access, you probably also need Calendar and Gmail
- **OAuth 2.1** — modern authentication with multi-user bearer token support for organizations
- **Stateless mode** — can run without local state, useful for serverless deployments
- **1,654 commits** — heavily maintained with active development
- **.dxt package** — installable as a desktop extension

**Limitations:**
- Requires a Google Cloud project with OAuth credentials configured — the setup isn't trivial
- Large surface area means more potential attack surface
- Python dependency

**Best for:** Anyone who needs Google Drive access. The full Workspace coverage means you won't need separate servers for Gmail or Calendar.

### felores/gdrive-mcp-server — Lightweight Read-Only

**Stars:** 66 | **Language:** JavaScript | **License:** MIT

A minimal Google Drive server with just two tools: `gdrive_search` and `gdrive_read_file`. Enforces read-only scopes — the AI can search and read but never modify or delete files.

**What makes it stand out:**
- **Read-only by design** — uses `drive.readonly` scope. Cannot modify files even if the AI tries
- **Auto-conversion** — Google Docs to Markdown, Sheets to CSV, Slides to plain text
- **Simple setup** — fewer moving parts than the full Workspace server

**Best for:** Teams that want AI assistants to reference Google Drive documents without any write risk.

### Other Google Drive Options

- **[a-bonus/google-docs-mcp](https://github.com/a-bonus/google-docs-mcp)** — Full Google Docs editing with formatting support (bold, italic, headers). The only option if you need to write and format Docs, not just read them
- **[distrihub/mcp-google-workspace](https://github.com/distrihub/mcp-google-workspace)** — Rust implementation covering Drive and Sheets. Choose this if you want Rust's performance and safety guarantees

## AWS S3

AWS has official MCP presence, but the S3 story is fragmented across multiple repos.

### aws-samples/sample-mcp-server-s3 — The Winner

**Stars:** 77 | **Language:** Python | **License:** MIT-0

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

The [awslabs/mcp](https://github.com/awslabs/mcp) monorepo (8,500 stars) includes an S3 Tables MCP server for table-formatted S3 data. It's specialized for structured data queries, not general file management.

## Dropbox

Dropbox's official MCP server focuses on Dash (enterprise search), not file management. Community servers fill the gap.

### amgadabdelhafez/dbx-mcp-server — The Winner

**Stars:** 26 | **Language:** TypeScript | **License:** MIT

The most complete Dropbox file management server, with full CRUD operations and sharing.

**What makes it stand out:**
- **Full file operations** — list, upload, download, delete, copy, move, create folders
- **Sharing** — create and manage sharing links
- **Search and metadata** — search files and retrieve detailed metadata
- **OAuth 2.0 with PKCE** — modern, secure authentication flow

**Limitations:**
- No chunked uploads for very large files
- Community-maintained — no official Dropbox backing for file operations

**Best for:** Teams that need full Dropbox file management from AI agents.

### ngs/dropbox-mcp-server — Large Files + Version History

**Stars:** 3 | **Language:** Go | **License:** MIT

A Go implementation with 17+ tools, including features the TypeScript server lacks.

**What makes it stand out:**
- **Chunked uploads** — handles files over 150MB that would fail with standard upload
- **Version history** — browse revision history and restore previous versions
- **Shared link management** — create, list, and revoke shared links

**Best for:** Teams working with large files or needing version control within Dropbox.

### dropbox/mcp-server-dash — Official (Search Only)

**Stars:** 9 | **Language:** Python | **License:** Apache 2.0

The official Dropbox MCP server, but it's Dash-focused — enterprise search across connected services, not direct file management. Tools: `dash_company_search` and `dash_get_file_details`.

**Best for:** Enterprise teams using Dropbox Dash for cross-platform content search.

## OneDrive / SharePoint

Microsoft's OneDrive/SharePoint MCP story is currently the weakest among major cloud storage providers. The official server was deprecated, and community options are nascent.

### ftaricano/mcp-onedrive-sharepoint — The Winner

**Language:** TypeScript | **License:** —

The most comprehensive community option, covering OneDrive, SharePoint, and Excel in one server.

**What makes it stand out:**
- **35+ tools** — file management (upload/download/move/rename/delete/search), SharePoint list CRUD, and 12 Excel-specific tools with formula support
- **Device Code Flow** — user-friendly authentication with auto-refresh and secure keychain storage
- **Excel integration** — read/write cells, create charts, manage worksheets. Unique among storage servers

**Limitations:**
- Very new, minimal star count
- Single maintainer

**Best for:** Microsoft 365 teams that need unified OneDrive + SharePoint + Excel access.

### Other Microsoft Options

- **[SAIB-Inc/Helix](https://github.com/SAIB-Inc/Helix)** — .NET 10 implementation covering email, calendar, SharePoint sites/lists/documents. Good for .NET shops
- **[godwin3737/mcp-server-microsoft365-filesearch](https://github.com/godwin3737/mcp-server-microsoft365-filesearch)** (11 stars) — Python, search-focused with local file caching. Uses Microsoft Graph API
- **[pnp/cli-microsoft365-mcp-server](https://github.com/pnp/cli-microsoft365-mcp-server)** — Wraps the entire CLI for Microsoft 365. Natural language execution of any M365 CLI command
- **[microsoft/mcp](https://github.com/microsoft/mcp)** (2,800 stars) — Official Microsoft MCP catalog includes Mail, Calendar, and Copilot Chat servers, but OneDrive/SharePoint support is deprecated

## Box

Box stands out as the enterprise storage provider with the best MCP support — both self-hosted and cloud-hosted official servers.

### box-community/mcp-server-box — The Winner

**Stars:** 97 | **Language:** Python | **License:** MIT

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

→ **Standard setup** → Official Filesystem (modelcontextprotocol/servers)

→ **Go binary / Docker** → mark3labs/mcp-filesystem-server

→ **Remote with auth** → cyanheads/filesystem-mcp-server (HTTP + JWT)

**Do you need Google Drive?**

→ **Full Workspace (Drive + Gmail + Calendar)** → taylorwilsdon/google_workspace_mcp

→ **Read-only Drive access** → felores/gdrive-mcp-server

→ **Google Docs editing with formatting** → a-bonus/google-docs-mcp

**Do you need AWS S3?**

→ **Safe, read-only** → aws-samples/sample-mcp-server-s3 (official)

→ **Full CRUD + multi-account** → txn2/mcp-s3

→ **S3-compatible (MinIO, SeaweedFS)** → txn2/mcp-s3 or minio/mcp-server-aistor

**Do you need Dropbox?**

→ **Full file management** → amgadabdelhafez/dbx-mcp-server

→ **Large files + version history** → ngs/dropbox-mcp-server

**Do you need OneDrive / SharePoint?**

→ **Full OneDrive + SharePoint + Excel** → ftaricano/mcp-onedrive-sharepoint

→ **Broad M365 coverage** → SAIB-Inc/Helix

**Do you need Box?**

→ **Self-hosted with AI queries** → box-community/mcp-server-box (official)

→ **Zero infrastructure** → box/mcp-server-box-remote (official hosted)

**Do you need multiple cloud providers?**

→ Xuanwo/mcp-server-opendal (40+ backends, one server)

## Three Trends Shaping This Space

### 1. Official servers are appearing — then disappearing

The MCP file storage landscape is unstable at the provider level. Anthropic's reference Google Drive server was archived. Microsoft deprecated their OneDrive/SharePoint server. Meanwhile, Box ships both self-hosted and remote servers, MinIO has a 30-tool official server, and AWS has multiple S3 options. There's no consistency in how major providers approach MCP support, which means community servers remain critical.

### 2. Safety defaults are diverging

MinIO's server is read-only by default — you must pass explicit flags to enable writes and deletes. The official Filesystem server allows full read/write within allowed directories. Box's remote server requires OAuth consent flows. There's no standard approach to safety in file MCP servers, and the risk profiles are very different. Local filesystem access (sandboxed by directory) and cloud storage access (sandboxed by OAuth scopes) require different mental models.

### 3. Workspace servers are replacing single-service servers

taylorwilsdon's Google Workspace MCP covers 10 services in one server. ftaricano's OneDrive server bundles SharePoint and Excel. The trend is toward consolidated servers that cover an entire productivity suite rather than individual file storage. This makes sense — if you need Drive access, you almost certainly need Calendar and Gmail too.

## What's Missing

- **No maintained official Google Drive MCP server** — Anthropic's was archived, Google hasn't shipped one. The community server is excellent but Google's API changes could break it anytime
- **No official OneDrive/SharePoint MCP server** — Microsoft deprecated theirs. The gap is filled by small community projects with minimal stars
- **No iCloud MCP server** — Apple's ecosystem is completely absent from the MCP world
- **No Backblaze B2 MCP server** — popular S3-compatible storage with no dedicated MCP support (OpenDAL covers it generically)
- **No file sync/conflict resolution** — no MCP server handles bidirectional file sync between local and cloud storage
- **Limited write safety** — most cloud storage servers either allow full writes or no writes. Few offer granular per-operation permissions (MinIO is the exception)
- **No file preview/transformation** — no server generates thumbnails, converts formats, or previews documents. AI agents get raw content or nothing

