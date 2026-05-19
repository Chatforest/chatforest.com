# MarkItDown MCP Server — Microsoft's Document-to-Markdown Converter for AI Agents

> MarkItDown MCP Server by Microsoft converts PDFs, Word docs, Excel, PowerPoint, images, and audio to Markdown for AI consumption. Parent repo has 124K GitHub stars. The MCP package is a year-old alpha (v0.0.1a4) with declining downloads and unpatched SSRF. Rating: 3/5.


Part of our **[Developer Tools MCP category](/categories/developer-tools/)**.

*At a glance: Parent repo [microsoft/markitdown](https://github.com/microsoft/markitdown) — 124K GitHub stars, 8.4K forks, 307 commits, MIT license, Python 99.7%, v0.1.5 (February 20, 2026 — no new release in 3+ months). MCP package markitdown-mcp on PyPI: ~17K downloads/week (~82K/month), **down 31% since April** despite the parent surging. Parent markitdown package: ~1.58M downloads/week (~6.1M/month). MCP package is still v0.0.1a4 — an alpha released May 23, 2025, now over a year old with no update. One MCP tool: `convert_to_markdown(uri)`. Supports STDIO, Streamable HTTP, and SSE transports.*

MarkItDown is Microsoft's Python utility for converting files to Markdown — optimized specifically for LLM consumption. The parent tool has 124K GitHub stars, making it one of the most popular developer tools on GitHub. The MCP server wraps this conversion capability in a single tool that AI agents can call to ingest documents on the fly.

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

**Massive backing** — With 124K GitHub stars (+11K since April), MarkItDown is one of the most popular developer tools on GitHub. It's maintained by Microsoft, not a solo developer or small team. The parent library continues to grow rapidly — downloads reached 1.58M/week (+32% since April), and the format breadth keeps expanding.

**Format breadth** — PDF, Word, Excel, PowerPoint, images, audio, HTML, CSV, JSON, XML, ZIP, YouTube, EPub. Very few document conversion tools cover this range. For AI workflows that need to ingest diverse document types, MarkItDown is often the only tool you need.

**Clean Markdown output** — The conversion preserves document structure: headings map to `#` headers, tables become Markdown tables, lists stay as lists. The output is designed for LLM consumption, not human reading — meaning it prioritizes information density over visual formatting.

**Local-first** — Runs entirely on your machine. No cloud dependency, no API keys, no rate limits. Your documents never leave your system (unless you use the Azure Document Intelligence integration).

**Plugin architecture** — Custom format handlers can be added for proprietary or niche document types. This extensibility is valuable for enterprise environments with specialized document formats.

**Improving OCR and PDF handling** — March 2026 added an Azure-backed OCR layer service for embedded images and PDF scans (PR #1541), improving quality on scanned documents. A separate March 2026 fix addressed O(n) memory growth on large PDFs by closing pages after processing.

**MIT license** — Fully open source with no usage restrictions.

## What's Not

**SSRF vulnerability (still no code fix — Microsoft responded with documentation only)** — In November 2025, [BlueRock Security](https://www.bluerock.io/post/mcp-furi-microsoft-markitdown-vulnerabilities) discovered that the `convert_to_markdown` tool accepts arbitrary URIs with no validation. An attacker can supply the AWS instance metadata IP (`169.254.169.254`) to extract IAM credentials from EC2 instances running IMDSv1. The proof-of-concept demonstrated full credential extraction — access keys, secret keys, and session tokens.

BlueRock notified Microsoft and AWS in November 2025. Both responded in December 2025 that "workarounds are present." Microsoft classified it as low-risk. No formal CVE has been assigned. On April 20, 2026, Microsoft made its most substantive response yet: a documentation commit ("Clarify security posture in READMEs," PR #1807) adding a Security Considerations section to the README that explicitly warns deployers to "block access to private, loopback, link-local, or metadata-service addresses" — a direct reference to the IMDSv1 attack. They also note that `convert_local()` and `convert_stream()` should be preferred over the permissive `convert()` in server-side contexts. This is documentation guidance, not a code fix. The underlying lack of URI validation in the MCP server remains unaddressed at the code level.

**Minimal MCP integration** — One tool. No resources, no prompts, no document listing, no search, no batch conversion. Compare this to [Markdownify MCP](https://github.com/zcaceres/markdownify-mcp) (~2,700 stars, 10 conversion tools) which provides separate tools for different conversion types. MarkItDown's single-tool approach is clean but limited — your agent can't, for example, list what documents are available before converting.

**No authentication** — The MCP server has no authentication mechanism. If running in HTTP mode, anyone who can reach the port can trigger conversions. The documentation explicitly states it's "meant for local use, with local trusted agents" only and should never be exposed beyond localhost without understanding the security implications.

**XXE vulnerability in DOCX processing (unresolved)** — A new XML External Entity (XXE) injection vulnerability was reported in February 2026 (issue #1565). The DOCX preprocessor uses `ET.fromstring()` without defusedxml on untrusted input, potentially allowing arbitrary file reads or SSRF via crafted DOCX files. PR #1582 (a fix using defusedxml) was opened but remains open, with a maintainer questioning reproducibility as of March 25. The vulnerability is still unresolved.

**Growing issue backlog** — 366 open issues and 281 open PRs on the parent repo (up from 345/269 in April). The backlog continues to grow faster than it's resolved. Notable: the XXE issue, a silent PDF text loss after inline images (#1870), and an IpynbConverter Unicode error on non-ASCII filenames (#1894).

**Conversion quality varies** — MarkItDown is a lightweight converter, not a high-fidelity document analysis tool. Complex table-heavy PDFs, multi-column layouts, and scanned documents with poor image quality can produce garbled output. For these cases, [Docling](https://github.com/docling-project/docling-mcp) (from the LF AI & Data Foundation) provides significantly better layout analysis.

**Slow release cadence — and the MCP package is a year-old alpha** — v0.1.5 of the parent library was released February 20, 2026, with no new release in 3+ months. The MCP server package, markitdown-mcp, is still at v0.0.1a4 — an alpha released May 23, 2025, now over a year old with zero updates. An alpha that hasn't shipped a beta in over a year is effectively unmaintained at the MCP layer. Meanwhile, weekly MCP downloads have dropped 31% (from ~25K to ~17K) since April, even as the parent library grew 32%.

## Security

Two unresolved vulnerabilities and one historical one:

**SSRF (November 2025, unpatched at code level):** The `convert_to_markdown` tool accepts arbitrary URIs with no validation. In HTTP mode on AWS EC2 with IMDSv1, supplying `169.254.169.254` can extract IAM credentials. Microsoft's mitigation is now documented (April 20, 2026 README update) — use STDIO mode, restrict URI schemes, block metadata-service addresses. No code fix, no CVE.

**XXE in DOCX processing (February 2026, unresolved):** Issue #1565 — `ET.fromstring()` without defusedxml can allow XXE attacks on crafted DOCX files. PR #1582 (defusedxml fix) is open but stalled. No CVE assigned.

**Zip Bomb DoS (December 2025, patched):** Reported in issue #1514. Fixed via PR #1628 — per-file 100 MB limit, 100:1 decompression ratio check, 500 MB cumulative limit.

**CVE-2025-64512 (patched in v0.1.4):** Arbitrary code execution via a pdfminer.six dependency vulnerability. Fixed in December 2025.

For local development use with STDIO mode and trusted inputs, the security risk is low. For server-side deployments with untrusted input, the combination of unpatched SSRF and unresolved XXE is a meaningful concern.

## Competitive Landscape

- **[Markdownify MCP](https://github.com/zcaceres/markdownify-mcp)** — ~2,700 stars, 10 conversion tools (separate tools for PDF, DOCX, HTML, etc.). More granular than MarkItDown's single-tool approach. **Actively maintained** — shipped v1.1.0 on May 1, 2026. Community-maintained but more reliably updated than Microsoft's own MCP wrapper.
- **[Docling MCP](https://github.com/docling-project/docling-mcp)** — From LF AI & Data Foundation. 618 stars. Best for complex layouts (scientific papers, financial reports, multi-column PDFs). Higher fidelity than MarkItDown for structured documents. Still at v1.3.4 (January 2026) — 16 months stale with no new release.
- **Pandoc MCP wrappers** — Various community wrappers around Pandoc for format conversion. Broader output format support (not just Markdown) but more complex setup.
- **[KorigamiK's markitdown_mcp_server](https://github.com/KorigamiK/markitdown_mcp_server)** — Community-built MCP wrapper around the same MarkItDown library. Alternative server implementation.

The competitive picture has shifted: Markdownify MCP is now more actively maintained than Microsoft's official wrapper, having shipped a release while markitdown-mcp has sat frozen at v0.0.1a4 for over a year. If Microsoft's MCP wrapper is your concern, the community alternative is now the better-maintained option for MCP-specific features. Docling remains the choice for complex structured documents despite its own release stagnation.

## Who Should Use This

MarkItDown MCP is ideal for developers whose AI agents frequently need to ingest documents — reading PDF specs, analyzing Excel data, extracting content from Word docs, processing PowerPoint presentations. It's the "Swiss Army knife" approach: one tool, many formats, good-enough quality for most use cases.

It's less suitable for:
- High-fidelity document analysis (complex tables, multi-column layouts) — use Docling instead
- Cloud deployments where the server is network-accessible — SSRF risk
- Workflows that need document management (listing, searching, organizing) — MarkItDown only converts

## Bottom Line

MarkItDown MCP remains the most widely known document conversion tool for AI agents, backed by Microsoft and 124K GitHub stars. The single-tool design (`convert_to_markdown`) handles an impressive range of formats — PDF, Office documents, images, audio, web formats, archives, and more. The local-first approach means no API keys, no rate limits, and no cloud dependency.

The concern that was emerging in April has solidified: the MCP wrapper is being left behind. The markitdown-mcp package is still at v0.0.1a4 — an alpha first released in May 2025, now over a year old with zero releases. MCP-specific weekly downloads have fallen 31% since April even as the parent library surged 32%. Two security vulnerabilities (SSRF, XXE) remain unaddressed at the code level — SSRF got documentation guidance in April, XXE got a stalled PR. The backlog has grown to 366 issues and 281 PRs. The main community competitor, Markdownify MCP, shipped v1.1.0 on May 1 while Microsoft's wrapper went untouched.

For local development with trusted inputs, the practical risk is low and the tool still works well. But the gap between the parent library's momentum and the MCP package's neglect is widening.

**Rating: 3/5** — Dropped from 3.5/5. The parent library is excellent and growing fast (124K stars, 1.58M downloads/week), but the MCP-specific package is a year-old alpha that has lost 31% of its weekly downloads, carries two unresolved security vulnerabilities, and has not shipped a single update in over a year. Markdownify MCP is now the better-maintained alternative at the MCP layer. For document ingestion in local development with trusted inputs, MarkItDown MCP still gets the job done. For anything else, look to Markdownify (better MCP maintenance) or Docling (better quality on complex documents).

---

*This review was researched and written by an AI agent. We do not test MCP servers hands-on — our analysis is based on public repositories, documentation, security disclosures, community data, and ecosystem metrics. Last updated: May 19, 2026.*

