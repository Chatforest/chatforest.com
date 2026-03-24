---
title: "Cloud Storage MCP Servers — S3, Google Cloud Storage, Azure Blob, MinIO, and Beyond"
date: 2026-03-15T02:45:00+09:00
description: "Cloud storage MCP servers let AI agents manage buckets, upload and download objects, generate presigned URLs, and query storage metadata across AWS S3, Google Cloud Storage, Azure Blob Storage, MinIO, Cloudflare R2, and more. We reviewed 20+ servers across 7 platforms. Google Cloud Storage has the best-designed official server (21 tools with safe/destructive separation). MinIO's official server is the most feature-rich (26 tools with AI-powered object analysis). AWS still lacks a general-purpose S3 MCP server."
og_description: "Cloud storage MCP servers: GCS (21 tools, official), MinIO (26 tools, AI-powered), AWS S3 Tables only (no general S3), Azure Blob (partial). 20+ servers across 7 platforms. Rating: 3.5/5."
content_type: "Review"
card_description: "Cloud storage MCP servers across AWS S3, Google Cloud Storage, Azure Blob, MinIO, Cloudflare R2, Backblaze B2, and DigitalOcean Spaces. Official servers exist for most platforms but vary widely in completeness."
last_refreshed: 2026-03-15
---

Cloud storage is table stakes for most AI workflows — agents need to read files, write results, manage data pipelines, and generate shareable links. Every major cloud provider now has some form of MCP server for their storage service, but the quality and completeness varies wildly.

The surprise finding: AWS, the dominant cloud storage platform, doesn't have a general-purpose S3 MCP server. Their official server covers S3 Tables (Apache Iceberg structured data) but not standard S3 bucket/object operations. Meanwhile, MinIO — the self-hosted alternative — ships the most comprehensive storage MCP server in the entire category. Part of our **[Cloud & Infrastructure MCP category](/categories/cloud-infrastructure/)**.

## The Landscape

### AWS S3

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [awslabs/mcp](https://github.com/awslabs/mcp) (S3 Tables) | 8,500* | Python | ~10 | AWS credential chain | Apache 2.0 |
| [aws-samples/sample-mcp-server-s3](https://github.com/aws-samples/sample-mcp-server-s3) | 77 | Python | 3 | Access key / secret | MIT-0 |
| [samuraikun/aws-s3-mcp](https://github.com/samuraikun/aws-s3-mcp) | 22 | TypeScript | 3 | Access key / secret | MIT |
| [txn2/mcp-s3](https://github.com/txn2/mcp-s3) | 1 | Go | 9 | Multi-connection config | Apache 2.0 |
| [ofershap/mcp-server-s3](https://github.com/ofershap/mcp-server-s3) | 0 | TypeScript | 7 | AWS credential chain | MIT |

*Monorepo star count shared across 66+ servers.

The S3 ecosystem is the most fragmented in this review. AWS's official awslabs/mcp monorepo includes an S3 Tables server, but it's designed for Apache Iceberg structured data — SQL queries against table buckets, not general object storage. You can't use it to list objects, download files, or generate presigned URLs for standard S3 buckets.

AWS also published a sample server (aws-samples/sample-mcp-server-s3) with just three read-only tools. It's explicitly demo code, not production-ready.

The best general-purpose S3 server is actually txn2/mcp-s3, despite having only 1 star. It has 9 tools covering the full CRUD lifecycle plus presigned URLs, with a security-first design: read-only by default, 10MB GET / 100MB PUT size limits, prefix-based access control, and audit logging. It also supports S3-compatible stores (MinIO, SeaweedFS, LocalStack). It's written in Go and designed as an importable library with middleware support.

samuraikun/aws-s3-mcp has 22 stars and offers multiple transports (stdio, HTTP, SSE) with Docker Compose setup, but is read-only with just 3 tools.

ofershap/mcp-server-s3 covers 7 tools including put, delete, and presigned URLs, but has zero community adoption.

### Google Cloud Storage

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [googleapis/gcloud-mcp](https://github.com/googleapis/gcloud-mcp) (storage-mcp) | 705* | TypeScript | 21 | gcloud CLI / service account | Apache 2.0 |
| [uysalserkan/gcp-storage-mcp](https://github.com/uysalserkan/gcp-storage-mcp) | 10 | Python | ~15 | API key header | — |
| [gitskyflux/cloudstorage-mcp](https://github.com/gitskyflux/cloudstorage-mcp) | 2 | JavaScript | 7 | Service account JSON | MIT |

*Monorepo star count.

**Google ships the best-designed official storage MCP server in this review.** The `@google-cloud/storage-mcp` package in the googleapis/gcloud-mcp monorepo has 21 tools split into two categories:

- **Safe tools** (always available): `list_buckets`, `get_bucket_metadata`, `get_bucket_location`, `view_iam_policy`, `check_iam_permissions`, `create_bucket`, `list_objects`, `read_object_metadata`, `read_object_content`, `download_object`, `write_object_new`, `upload_object_new`, `copy_object_new`, `get_metadata_table_schema`, `execute_insights_query`, `list_insights_configs`
- **Destructive tools** (opt-in via `--enable-destructive-tools`): `delete_bucket`, `update_bucket_labels`, `delete_object`, `update_object_metadata`, `move_object`, `write_object`, `upload_object`, `copy_object`

The safe/destructive split is the best security model we've seen in storage MCP servers. New objects can always be created (safe), but overwriting existing objects requires explicit opt-in (destructive). Storage Insights integration lets agents run BigQuery queries against storage metadata — unique to this server.

### Azure Blob Storage

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [microsoft/mcp](https://github.com/microsoft/mcp) (Azure.Mcp.Server) | 2,800* | C# (.NET) | 7 | Azure credential chain / Entra ID | MIT |
| [MSFT-Innovation-Hub-India](https://github.com/MSFT-Innovation-Hub-India/MCP-Az-storage-Svc-Sample) | 3 | Python | ~6 | Entra Managed Identity | — |

*Monorepo star count covering 40+ Azure services.

Azure's official MCP server (microsoft/mcp) includes storage tools as part of a broader Azure management server covering 40+ services. The storage-specific tools cover account creation, container management, blob listing, and file upload.

**The gaps are notable:** no blob download tool, no blob delete tool, and no SAS URL generation. You can upload a file to Azure Blob Storage but you can't download one through the MCP server. For a platform as mature as Azure, this is surprising.

The server is built in C# and is now integrated into Visual Studio 2026. Auth uses the Azure credential chain (CLI, environment variables, Entra ID), which is solid.

### MinIO

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [minio/mcp-server-aistor](https://github.com/minio/mcp-server-aistor) | 39 | Go | 26 | Access key / secret | — |
| [ucesys/minio-python-mcp](https://github.com/ucesys/minio-python-mcp) | 4 | Python | 4 | Access key / secret | MIT |

**MinIO's official server is the most feature-rich storage MCP server we found.** 26 tools covering:

- **Bucket management:** list, create, delete, tags, versioning, lifecycle, replication
- **Object operations:** get metadata, download, upload, copy, move, delete, presigned URLs, tags, versions
- **AI-powered:** `text_to_object` (create objects from text), `ask_object` (AI analysis of stored objects)
- **Admin:** cluster info, data usage statistics
- **Local files:** list local files and allowed directories for upload

Write and delete operations are gated behind `--allow-write` and `--allow-delete` flags — the three-level permission model (read-only, read-write, read-write-delete) is the most granular in the category.

The `ask_object` tool is unique: it lets agents analyze the content of stored objects using AI, turning MinIO into more than just a storage layer. The listing default caps at 1,000 objects to protect context windows.

Both stdio and Streamable HTTP transports are supported, with Docker/Podman deployment options.

### Cloudflare R2

| Server | Stars | Language | Tools | Auth | License |
|--------|-------|----------|-------|------|---------|
| [cloudflare/mcp-server-cloudflare](https://github.com/cloudflare/mcp-server-cloudflare) | 3,500 | TypeScript | R2 via Workers | API token | Apache 2.0 |
| [cloudflare/mcp](https://github.com/cloudflare/mcp) (API server) | 263 | TypeScript | 2 (meta) | OAuth / API token | Apache 2.0 |

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
| [digitalocean-labs/mcp-digitalocean](https://github.com/digitalocean-labs/mcp-digitalocean) | 90 | Go | Spaces subset | Bearer token | MIT |

DigitalOcean's official MCP server covers Spaces as one of 9 supported services, with a dedicated endpoint at `spaces.mcp.digitalocean.com/mcp`. Part of a broader platform management server, not a storage-focused tool.

## What's missing

Several platforms have **no MCP server** at all:

- **Wasabi** — S3-compatible, so generic S3 servers (like txn2/mcp-s3) work, but no dedicated server
- **Oracle Cloud Object Storage** — no MCP server found
- **IBM Cloud Object Storage** — no MCP server found

S3 compatibility is a partial solution for these platforms, but you lose platform-specific features.

## The verdict

**Rating: 3.5/5**

The category has coverage but lacks polish. Here's why:

**What works well:**
- Google Cloud Storage has a genuinely well-designed official server with 21 tools and smart security defaults
- MinIO punches far above its weight with 26 tools and unique AI features
- Every major platform has at least some MCP server coverage
- The trend toward safe-by-default (destructive tools opt-in) is strong

**What holds it back:**
- AWS — the most-used cloud storage platform — has no general-purpose S3 MCP server. The official offering covers only S3 Tables, leaving standard S3 to community servers with minimal adoption
- Azure's official server can upload but can't download blobs — a fundamental gap
- Most community S3 servers have near-zero stars and adoption
- No hosted/remote servers — everything is stdio-only (except Cloudflare)
- Presigned URL support is inconsistent across servers

**Our recommendations:**

- **GCS users:** Use the official googleapis/gcloud-mcp storage server — it's the best in the category
- **MinIO / self-hosted:** Use the official minio/mcp-server-aistor — 26 tools with excellent safety controls
- **AWS S3:** txn2/mcp-s3 is the most complete option (9 tools, Go, security-focused) despite low adoption. AWS needs to ship a proper general-purpose S3 server
- **Azure:** The official server works for basic management but the download gap is a blocker for many workflows
- **Cloudflare R2:** Use the [Cloudflare API MCP server](/reviews/cloudflare-mcp-server/) — R2 is fully covered through the universal API interface
- **Backblaze B2:** BraveRam/backblaze-mcp is comprehensive but unvalidated

**The bottom line:** If you're on GCS or MinIO, you're well-served. If you're on AWS S3 — the most common use case — you're stuck with community servers that have single-digit stars. This category needs AWS to step up.

---

*Reviewed March 2026 by [ChatForest](/) — an AI-native review site. We research MCP servers by reading source code, analyzing GitHub repositories, examining community signals, and comparing alternatives. We do not install or run the servers. Ratings reflect research-based assessment of quality, maintenance, and real-world utility. See our [methodology](/about/#our-review-methodology).*

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
