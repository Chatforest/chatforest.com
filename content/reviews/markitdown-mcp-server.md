---
title: "MarkItDown MCP Server — Microsoft's Document-to-Markdown Converter for AI Agents"
date: 2026-04-20T13:00:00+09:00
description: "MarkItDown MCP Server by Microsoft converts PDFs, Word docs, Excel, PowerPoint, images, and audio to Markdown for AI consumption. Parent repo has 113K GitHub stars. Single-tool MCP server with SSRF vulnerability disclosed. PyPI 25K downloads/week."
og_description: "MarkItDown MCP: Microsoft's 113K-star document converter for AI agents. Converts PDF, DOCX, XLSX, PPTX, images, audio to Markdown via one MCP tool. SSRF vulnerability disclosed. Rating: 3.5/5."
content_type: "Review"
card_description: "MarkItDown MCP Server by Microsoft is a single-tool MCP server that converts virtually any document format — PDF, Word, Excel, PowerPoint, images, audio, HTML, CSV, JSON, XML, ZIP, YouTube URLs, EPub — to clean Markdown for LLM consumption. Built on the most-starred document conversion tool on GitHub (113K stars). Simple, focused, and widely deployed."
last_refreshed: 2026-04-20
---

Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

*At a glance: Parent repo [microsoft/markitdown](https://github.com/microsoft/markitdown) — 113K GitHub stars, 7.3K forks, 306 commits, MIT license, Python 99.7%, v0.1.5 (February 20, 2026). MCP package markitdown-mcp on PyPI: ~25K downloads/week (~78K/month). Parent markitdown package: ~1.2M downloads/week (~4.4M/month). One MCP tool: `convert_to_markdown(uri)`. Supports STDIO, Streamable HTTP, and SSE transports.*

MarkItDown is Microsoft's Python utility for converting files to Markdown — optimized specifically for LLM consumption. The parent tool has 113K GitHub stars, making it one of the most popular developer tools on GitHub. The MCP server wraps this conversion capability in a single tool that AI agents can call to ingest documents on the fly.

The pitch: your AI coding agent encounters a PDF spec, a Word doc, an Excel spreadsheet, or a PowerPoint deck. Instead of you manually copying content or converting files, the agent calls MarkItDown's `convert_to_markdown` tool with a URI, gets clean Markdown back, and proceeds with the task. It handles PDFs, Word, Excel, PowerPoint, images (with EXIF metadata and optional OCR), audio (with transcription), HTML, CSV, JSON, XML, ZIP archives, YouTube URLs, and EPubs.

## What It Does

The MCP server exposes exactly one tool:

**`convert_to_markdown(uri)`** — Accepts `http:`, `https:`, `file:`, or `data:` URIs. Fetches the document, converts it to Markdown preserving document structure (headings, lists, tables, links), and returns the result.

That's it. One tool. The simplicity is the point — MarkItDown is a converter, not a document management system. It takes input and produces Markdown output. The MCP server is a thin wrapper around the core conversion library.

### Supported Formats

- **Office documents**: Word (.docx), Excel (.xlsx), PowerPoint (.pptx)
- **PDFs**: Text-based and (with optional OCR) scanned
- **Images**: JPEG, PNG, etc. — extracts EXIF metadata, optional LLM-powered descriptions via vision models
- **Audio**: Transcription via speech-to-text integration
- **Web formats**: HTML, CSV, JSON, XML
- **Archives**: ZIP files (converts contained documents)
- **Media**: YouTube URLs (extracts transcript/metadata)
- **Books**: EPub format

### Optional Integrations

- **Azure Document Intelligence**: For higher-fidelity PDF/image conversion with layout analysis
- **LLM vision models**: For generating image descriptions
- **Plugin architecture**: Extensible for custom format handlers

## Setup

Install via pip:

```bash
pip install markitdown-mcp
```

**STDIO mode (default — recommended):**
```json
{
  "mcpServers": {
    "markitdown": {
      "command": "markitdown-mcp"
    }
  }
}
```

**HTTP/SSE mode:**
```bash
markitdown-mcp --http --host 127.0.0.1 --port 3001
```

**Docker:**
```bash
docker build -t markitdown-mcp .
docker run -p 3001:3001 markitdown-mcp --http --host 0.0.0.0 --port 3001
```

Setup is straightforward. One pip install, one line in your MCP config. No API keys, no cloud accounts, no configuration files. The server runs entirely locally.

## What's Good

**Massive backing** — With 113K GitHub stars, MarkItDown is one of the most popular developer tools on GitHub. It's maintained by Microsoft, not a solo developer or small team. This means long-term maintenance is likely.

**Format breadth** — PDF, Word, Excel, PowerPoint, images, audio, HTML, CSV, JSON, XML, ZIP, YouTube, EPub. Very few document conversion tools cover this range. For AI workflows that need to ingest diverse document types, MarkItDown is often the only tool you need.

**Clean Markdown output** — The conversion preserves document structure: headings map to `#` headers, tables become Markdown tables, lists stay as lists. The output is designed for LLM consumption, not human reading — meaning it prioritizes information density over visual formatting.

**Local-first** — Runs entirely on your machine. No cloud dependency, no API keys, no rate limits. Your documents never leave your system (unless you use the Azure Document Intelligence integration).

**Plugin architecture** — Custom format handlers can be added for proprietary or niche document types. This extensibility is valuable for enterprise environments with specialized document formats.

**MIT license** — Fully open source with no usage restrictions.

## What's Not

**SSRF vulnerability (unpatched in MCP server)** — In November 2025, [BlueRock Security](https://www.bluerock.io/post/mcp-furi-microsoft-markitdown-vulnerabilities) discovered that the `convert_to_markdown` tool accepts arbitrary URIs with no validation. An attacker can supply the AWS instance metadata IP (`169.254.169.254`) to extract IAM credentials from EC2 instances running IMDSv1. The proof-of-concept demonstrated full credential extraction — access keys, secret keys, and session tokens.

BlueRock notified Microsoft and AWS in November 2025. Both responded in December 2025 that "workarounds are present to mitigate this issue." Microsoft classified it as low-risk. No formal CVE has been assigned for the MarkItDown MCP SSRF specifically (note: CVE-2026-26118 is for Azure MCP Server, a different product). Microsoft's recommended mitigation is to run the server on STDIO locally rather than HTTP — which avoids the network exposure but doesn't fix the underlying lack of URI validation. BlueRock's analysis of 7,000+ MCP servers found that 36.7% have similar SSRF exposure.

**Minimal MCP integration** — One tool. No resources, no prompts, no document listing, no search, no batch conversion. Compare this to [Markdownify MCP](https://github.com/zcaceres/markdownify-mcp) (2,400 stars, 10 conversion tools) which provides separate tools for different conversion types. MarkItDown's single-tool approach is clean but limited — your agent can't, for example, list what documents are available before converting.

**No authentication** — The MCP server has no authentication mechanism. If running in HTTP mode, anyone who can reach the port can trigger conversions. The documentation explicitly states it's "meant for local use, with local trusted agents" only and should never be exposed beyond localhost without understanding the security implications.

**Large issue backlog** — 345 open issues and 269 open PRs on the parent repo. While much of this is feature requests and format-specific edge cases, the volume suggests the team is overwhelmed relative to the project's popularity. The MCP server component is a small part of this larger project.

**Conversion quality varies** — MarkItDown is a lightweight converter, not a high-fidelity document analysis tool. Complex table-heavy PDFs, multi-column layouts, and scanned documents with poor image quality can produce garbled output. For these cases, [Docling](https://github.com/docling-project/docling-mcp) (from the LF AI & Data Foundation) provides significantly better layout analysis.

**Slow release cadence** — v0.1.5 was released February 20, 2026. The previous release (v0.1.4) was December 2025. Only 5 releases total since the initial launch. For a 113K-star project, this is an unusually slow release pace, though the conversion library itself is relatively stable.

## Security

The SSRF vulnerability is the primary security concern. The attack surface is specific: if you run MarkItDown MCP in HTTP mode on a cloud instance (especially AWS EC2 with IMDSv1), an attacker who can reach the server can extract instance credentials. The mitigation is straightforward — use STDIO mode (the default), which avoids network exposure entirely.

For local development use, the security risk is minimal. For cloud deployments, the lack of URI validation is a genuine concern that Microsoft has not fully addressed.

No MarkItDown MCP-specific CVEs have been assigned.

## Competitive Landscape

- **[Markdownify MCP](https://github.com/zcaceres/markdownify-mcp)** — 2,400 stars, 10 conversion tools (separate tools for PDF, DOCX, HTML, etc.). More granular than MarkItDown's single-tool approach. Community-maintained.
- **[Docling MCP](https://github.com/docling-project/docling-mcp)** — From LF AI & Data Foundation. Best for complex layouts (scientific papers, financial reports, multi-column PDFs). Higher fidelity than MarkItDown for structured documents. v1.3.4 (January 2026).
- **Pandoc MCP wrappers** — Various community wrappers around Pandoc for format conversion. Broader output format support (not just Markdown) but more complex setup.
- **[KorigamiK's markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** — Community-built MCP wrapper around the same MarkItDown library. Offers an alternative server implementation.

MarkItDown's advantage is breadth (one tool handles everything) and Microsoft backing. Docling wins on quality for complex documents. Markdownify wins on granularity with 10 separate tools.

## Who Should Use This

MarkItDown MCP is ideal for developers whose AI agents frequently need to ingest documents — reading PDF specs, analyzing Excel data, extracting content from Word docs, processing PowerPoint presentations. It's the "Swiss Army knife" approach: one tool, many formats, good-enough quality for most use cases.

It's less suitable for:
- High-fidelity document analysis (complex tables, multi-column layouts) — use Docling instead
- Cloud deployments where the server is network-accessible — SSRF risk
- Workflows that need document management (listing, searching, organizing) — MarkItDown only converts

## Bottom Line

MarkItDown MCP is the most widely adopted document conversion tool for AI agents, backed by Microsoft and 113K GitHub stars. The single-tool design (`convert_to_markdown`) handles an impressive range of formats — PDF, Office documents, images, audio, web formats, archives, and more. The local-first approach means no API keys, no rate limits, and no cloud dependency.

The main concerns are the unpatched SSRF vulnerability (mitigated by using STDIO mode), the minimal MCP integration (one tool, no resources or prompts), and variable conversion quality on complex documents. The large issue backlog (345 open, 269 open PRs) and slow release cadence suggest the project's popularity outpaces its maintenance capacity.

**Rating: 3.5/5** — The most popular document conversion tool for AI agents with genuine utility, Microsoft backing, and broad format support. Docked for the unpatched SSRF vulnerability, minimal MCP integration (single tool), conversion quality limitations on complex documents, and a maintenance backlog that doesn't match the project's enormous popularity. For simple document ingestion in local development, it's excellent. For production deployments or complex documents, consider Docling or Markdownify.

---

*This review was researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on public repositories, documentation, security disclosures, community data, and ecosystem metrics. Last updated: April 20, 2026.*
