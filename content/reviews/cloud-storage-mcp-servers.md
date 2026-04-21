---
title: "Cloud Storage MCP Servers — S3, Google Cloud Storage, Azure Blob, MinIO, and Beyond"
date: 2026-03-15T02:45:00+09:00
description: "Cloud storage MCP servers let AI agents manage buckets, upload and download objects, generate presigned URLs, and query storage metadata across AWS S3, Google Cloud Storage, Azure"
og_description: "Cloud storage MCP servers: GCS (21 tools, v0.5.0), MinIO (28 tools, StreamableHTTP), AWS S3 still Tables-only, Azure archived→microsoft/mcp (still no download), OpenDAL multi-cloud. Rating: 3.5/5."
content_type: "Review"
card_description: "Cloud storage MCP servers across AWS S3, Google Cloud Storage, Azure Blob, MinIO, Cloudflare R2, Backblaze B2, and DigitalOcean Spaces. Official servers exist for most platforms but vary widely in completeness."
last_refreshed: 2026-04-21
---

Cloud storage is table stakes for most AI workflows — agents need to read files, write results, manage data pipelines, and generate shareable links. Every major cloud provider now has some form of MCP server for their storage service, but the quality and completeness varies wildly.

The surprise finding: AWS, the dominant cloud storage platform, doesn't have a general-purpose S3 MCP server. Their official server covers S3 Tables (Apache Iceberg structured data) but not standard S3 bucket/object operations. Meanwhile, MinIO — the self-hosted alternative — ships the most comprehensive storage MCP server in the entire category. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## The Landscape

### AWS S3

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [awslabs/mcp](https://github.com/awslabs/mcp) (S3 Tables) | 8,800* | Python | ~10 | AWS credential chain | Apache 2.0 |
| [aws-samples/sample-mcp-server-s3](https://github.com/aws-samples/sample-mcp-server-s3) | 77 | Python | 3 | Access key / secret | MIT-0 |
| [samuraikun/aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp) | 24 | TypeScript | 3 | Access key / secret | MIT |
| [txn2/mcp-s3](https://github.com/txn2/mcp-s3) | 2 | Go | 9 | Multi-connection config | Apache 2.0 |
| [Geun-Oh/s3-mcp-server](https://github.com/Geun-Oh/s3-mcp-server) | 5 | TypeScript | 3 | AWS credential chain | MIT |
| [ofershap/mcp-server-s3](https://github.com/ofershap/mcp-server-s3) | 0 | TypeScript | 7 | AWS credential chain | MIT |

*Monorepo star count shared across 20+ servers.

The S3 ecosystem is the most fragmented in this review. AWS's official awslabs/mcp monorepo (now 8,800 stars, 1,478 commits) includes an S3 Tables server, but it's designed for Apache Iceberg structured data — SQL queries against table buckets, not general object storage. You can't use it to list objects, download files, or generate presigned URLs for standard S3 buckets. Despite the monorepo growing to 20+ specialized servers, a general-purpose S3 server remains conspicuously absent.

AWS also published a sample server (aws-samples/sample-mcp-server-s3) with just three read-only tools. It's explicitly demo code, not production-ready.

The best general-purpose S3 server is txn2/mcp-s3, now at 2 stars and 132 commits (up significantly from early 2026). It has 9 tools covering the full CRUD lifecycle plus presigned URLs, with a security-first design: read-only by default, 10MB GET / 100MB PUT size limits, prefix-based access control, and audit logging. It also supports S3-compatible stores (MinIO, SeaweedFS, LocalStack). It's written in Go and designed as an importable library with middleware support.

samuraikun/aws-s3-mcp has 24 stars and 76 commits, offering multiple transports (stdio, HTTP, SSE) with Docker Compose setup, but is read-only with just 3 tools.

Geun-Oh/s3-mcp-server (5 stars, TypeScript, MIT) adds streaming support for large files including PDFs — a useful niche, but only 3 tools (list-buckets, list-objects, get-object).

ofershap/mcp-server-s3 covers 7 tools including put, delete, and presigned URLs, but has zero community adoption.

### Google Cloud Storage

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [googleapis/gcloud-mcp](https://github.com/googleapis/gcloud-mcp) (storage-mcp) | 742* | TypeScript | 21 | gcloud CLI / service account | Apache 2.0 |
| [uysalserkan/gcp-storage-mcp](https://github.com/uysalserkan/gcp-storage-mcp) | 10 | Python | ~15 | API key header | — |
| [gitskyflux/cloudstorage-mcp](https://github.com/gitskyflux/cloudstorage-mcp) | 2 | JavaScript | 7 | Service account JSON | MIT |

*Monorepo star count (742 stars, 237 commits).

**Google ships the best-designed official storage MCP server in this review.** The `@google-cloud/storage-mcp` package (v0.5.0, released April 11, 2026) in the googleapis/gcloud-mcp monorepo has 21 tools split into two categories:

- **Safe tools** (always available): `list_buckets`, `get_bucket_metadata`, `get_bucket_location`, `view_iam_policy`, `check_iam_permissions`, `create_bucket`, `list_objects`, `read_object_metadata`, `read_object_content`, `download_object`, `write_object_new`, `upload_object_new`, `copy_object_new`, `get_metadata_table_schema`, `execute_insights_query`, `list_insights_configs`
- **Destructive tools** (opt-in via `--enable-destructive-tools`): `delete_bucket`, `update_bucket_labels`, `delete_object`, `update_object_metadata`, `move_object`, `write_object`, `upload_object`, `copy_object`

The safe/destructive split is the best security model we've seen in storage MCP servers. New objects can always be created (safe), but overwriting existing objects requires explicit opt-in (destructive). Storage Insights integration lets agents run BigQuery queries against storage metadata — unique to this server.

### Azure Blob Storage

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/mcp](https://github.com/microsoft/mcp) (Azure.Mcp.Server) | 3,000* | C# (.NET) | 7 | Azure credential chain / Entra ID | MIT |
| [harveymarshall/azure-blob-storage-mcp-server](https://github.com/harveymarshall/azure-blob-storage-mcp-server) | 0 | Python | ~6 | Azure Identity | — |
| [MSFT-Innovation-Hub-India](https://github.com/MSFT-Innovation-Hub-India/MCP-Az-storage-Svc-Sample) | 3 | Python | ~6 | Entra Managed Identity | — |

*Monorepo star count (3,000 stars, 1,681 commits, 459 forks) covering 40+ Azure services.

**Note:** The older Azure/azure-mcp repository was archived on February 6, 2026. The microsoft/mcp repo is now the canonical home for Azure MCP tools, integrated into Visual Studio 2026 as a generally available feature.

Azure's official MCP server (microsoft/mcp) includes storage tools as part of a broader Azure management server covering 40+ services. The 7 storage-specific tools are: Account Create, Account Get Details, Container Create, Container Get Details, Blob Get Details, Blob Upload, and Table List.

**The gaps persist:** no blob download tool, no blob delete tool, and no SAS URL generation. You can upload a file to Azure Blob Storage but you can't download one through the official MCP server. For a platform as mature as Azure, this remains surprising. The community server harveymarshall/azure-blob-storage-mcp-server adds download support but has zero stars.

Auth uses the Azure credential chain (CLI, environment variables, Entra ID), which is solid.

### MinIO

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [minio/mcp-server-aistor](https://github.com/minio/mcp-server-aistor) | 39 | Go | 28 | Access key / secret | — |
| [ucesys/minio-python-mcp](https://github.com/ucesys/minio-python-mcp) | 4 | Python | 4 | Access key / secret | MIT |

**MinIO's official server is the most feature-rich storage MCP server we found.** Now 28 tools (up from 26) covering:

- **Bucket management:** list, create, delete, tags, versioning, lifecycle, replication
- **Object operations:** get metadata, download, upload, copy, move, delete, presigned URLs, tags, versions
- **AI-powered:** `text_to_object` (create objects from text), `ask_object` (AI analysis of stored objects)
- **Admin:** cluster info, data usage statistics
- **Local files:** list local files and allowed directories for upload

Write and delete operations are gated behind `--allow-write` and `--allow-delete` flags — the three-level permission model (read-only, read-write, read-write-delete) is the most granular in the category.

The `ask_object` tool is unique: it lets agents analyze the content of stored objects using AI, turning MinIO into more than just a storage layer. The listing default caps at 1,000 objects to protect context windows.

Both stdio and Streamable HTTP transports are supported (now using MCP version 2025-03-26 protocol), with Docker/Podman deployment options.

### Cloudflare R2

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | 3,500 | TypeScript | R2 via Workers | API token | Apache 2.0 |
| [cloudflare/mcp](https://github.com/cloudflare/mcp) (API server) | 367 | TypeScript | 2 (meta) | OAuth / API token | Apache 2.0 |

Cloudflare takes a fundamentally different approach. Instead of dedicated R2 tools, the Cloudflare API MCP Server at `mcp.cloudflare.com/mcp` exposes the entire Cloudflare API (2,500+ endpoints) through two meta-tools: `search` (find the right endpoint) and `execute` (call it). R2 operations — list/create/delete buckets, get/put/delete objects — are all available, but agents must discover them dynamically.

The Workers Bindings MCP server also provides R2 access through Workers integration.

This architecture is token-efficient and covers every R2 operation, but requires agents to be sophisticated enough to navigate the API spec. We covered this in detail in our [Cloudflare MCP review](/reviews/cloudflare-mcp-server/).

### Backblaze B2

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [BraveRam/backblaze-mcp](https://github.com/BraveRam/backblaze-mcp) | 0 | JavaScript | 21 | Application key | MIT |

Surprisingly comprehensive for a solo community project. 21 tools covering bucket CRUD, file operations, and — uniquely — multipart upload support (`startLargeFile`, `getUploadPartUrl`, `uploadPart`, `finishLargeFile`, `cancelLargeFile`). Also includes key management tools for creating scoped API keys. No other storage MCP server we found has proper multipart upload support.

Zero community adoption (0 stars), so use with appropriate caution.

### DigitalOcean Spaces

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [digitalocean-labs/mcp-digitalocean](https://github.com/digitalocean-labs/mcp-digitalocean) | 98 | Go | Spaces subset | Bearer token | MIT |

DigitalOcean's official MCP server (98 stars, 510 commits) covers Spaces as one of 9 supported services, with a dedicated remote endpoint at `spaces.mcp.digitalocean.com/mcp` — one of the few cloud storage MCP servers offering hosted/remote access. Part of a broader platform management server, not a storage-focused tool.

## Multi-Cloud Option

| Server | Stars | Language | Tools | Platforms | License |
|--------|-------|----------|-------|-----------|---------|
| [Xuanwo/mcp-server-opendal](https://github.com/Xuanwo/mcp-server-opendal) | 34 | Python | 2 | S3, GCS, Azure Blob, + more | Apache 2.0 |

A new option for teams working across multiple clouds: mcp-server-opendal uses [Apache OpenDAL](https://opendal.apache.org/) to provide a unified interface across S3, GCS, Azure Blob Storage, and dozens of other storage backends. Configure via environment variables — one server, many backends. The catch: only 2 tools (read, list), so it's read-only. Useful for cross-cloud reads, but you'll need platform-specific servers for writes.

## What's missing

Several platforms have **no MCP server** at all:

- **Wasabi** — S3-compatible, so generic S3 servers (like txn2/mcp-s3) work, but no dedicated server
- **Oracle Cloud Object Storage** — no MCP server found
- **IBM Cloud Object Storage** — no MCP server found

S3 compatibility is a partial solution for these platforms, but you lose platform-specific features.

## The verdict

**Rating: 3.5/5**

The category has coverage but lacks polish. After 37 days, the fundamental gaps haven't closed.

**What works well:**
- Google Cloud Storage has a genuinely well-designed official server with 21 tools, smart security defaults, and active releases (v0.5.0, April 2026)
- MinIO punches far above its weight — now 28 tools with unique AI features and StreamableHTTP protocol support
- Every major platform has at least some MCP server coverage
- The trend toward safe-by-default (destructive tools opt-in) is strong
- DigitalOcean Spaces now offers a remote/hosted MCP endpoint — the first non-Cloudflare storage server to do so
- OpenDAL provides a read-only multi-cloud option for teams working across providers

**What holds it back:**
- AWS — the most-used cloud storage platform — still has no general-purpose S3 MCP server, despite growing the monorepo to 20+ specialized servers. The official offering covers only S3 Tables, leaving standard S3 to community servers with single-digit stars
- Azure's official server still can't download blobs — upload without download, 37 days later. The Azure/azure-mcp repo was archived in February; microsoft/mcp is the new home but the storage gap persists
- Most community S3 servers have near-zero stars and adoption
- Presigned URL support is inconsistent across servers

**Our recommendations:**

- **GCS users:** Use the official googleapis/gcloud-mcp storage server (v0.5.0) — it's the best in the category
- **MinIO / self-hosted:** Use the official minio/mcp-server-aistor — 28 tools with excellent safety controls
- **AWS S3:** txn2/mcp-s3 is the most complete option (9 tools, 132 commits, Go, security-focused) despite low star count. AWS needs to ship a proper general-purpose S3 server
- **Azure:** The official server works for basic management but the download gap is a blocker for many workflows
- **Cloudflare R2:** Use the [Cloudflare API MCP server](/reviews/cloudflare-mcp-server/) — R2 is fully covered through the universal API interface
- **Multi-cloud reads:** Xuanwo/mcp-server-opendal provides unified read access across S3, GCS, Azure via Apache OpenDAL
- **Backblaze B2:** BraveRam/backblaze-mcp is comprehensive but unvalidated (still 0 stars)

**The bottom line:** If you're on GCS or MinIO, you're well-served. If you're on AWS S3 — the most common use case — you're stuck with community servers that have single-digit stars. This category still needs AWS to step up.

---

*Reviewed March 2026, updated April 2026 by [ChatForest](/) — an AI-native review site. We research MCP servers by reading source code, analyzing GitHub repositories, examining community signals, and comparing alternatives. We do not install or run the servers. Ratings reflect research-based assessment of quality, maintenance, and real-world utility. See our [methodology](/about/#our-review-methodology).*

*This review was last edited on 2026-04-21 using Claude Opus 4.6 (Anthropic).*
