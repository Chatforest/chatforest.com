---
title: "Genealogy & Family History MCP Servers — GEDCOM, Gramps, FamilySearch, WikiTree, and More"
date: 2026-03-15T23:30:00+09:00
description: "Genealogy MCP servers let AI agents explore family trees, parse GEDCOM files, and search historical records. We found 15+ servers across 6 subcategories. GEDCOM: reeeeemo/ancestry-mcp (33 stars, Python, MIT — read/parse/search .ged files), airy10/GedcomMCP (3 stars, Python, MIT — create, edit, and query GEDCOM files with relationship analysis and timeline creation). Gramps: cabout-me/gramps-mcp (25 stars, Python, AGPL-3.0, 16 tools — smart search, data management, tree analysis, relationship discovery via Gramps Web API), Genealogy-MCP/gramps-mcp (19 tools, 3 categories — search/retrieval, data management, analysis), nikkoxgonzales/mcp-grampsweb (TypeScript, MIT — GQL-based search), dsblank/gramps-ez-mcp (2 stars, Python, GPL-2.0 — simplified queries). FamilySearch: Genealogy-MCP/familysearch-mcp (Python, AGPL-3.0, 4 tools — place search, date standardization, Family Tree search). WikiTree: PeWu/wikitree-mcp (TypeScript, Apache-2.0 — profiles, ancestors, descendants, biographies), Genealogy-MCP/wikitree-mcp (Python, AGPL-3.0, 10 tools — profiles, trees, photos, categories). Research Sources: ibarrajo/research-sources-mcp (TypeScript, MIT — Library of Congress newspapers, WikiTree, OpenArch.nl, Find A Grave). Analysis: ibarrajo/tree-analyzer-mcp (Python, MIT — duplicate detection, chronological validation, missing sources). Infrastructure: peterdewit/genealogy-postgres-mcp (Python, MIT — PostgreSQL research database for AI agents). Gaps: no official servers from Ancestry.com, MyHeritage, or Findmypast; no DNA analysis servers; no cemetery/memorial database servers beyond Find A Grave search. Rating: 3.5/5."
og_description: "Genealogy MCP servers: ancestry-mcp (33 stars, GEDCOM files), gramps-mcp (25 stars, 16 tools, Gramps Web API), GedcomMCP (create/edit/query), FamilySearch MCP (4 tools), WikiTree MCP (10 tools), research-sources-mcp (newspapers, OpenArch.nl, Find A Grave). 15+ servers for family history research. Rating: 3.5/5."
content_type: "Review"
card_description: "Genealogy and family history MCP servers for AI-powered ancestor research — from parsing GEDCOM files to searching historical records across multiple platforms. This is a niche but surprisingly active category, driven by a dedicated **Genealogy-MCP GitHub organization** that maintains coordinated servers for FamilySearch, WikiTree, and Gramps. **GEDCOM file handling is the foundation** — reeeeemo/ancestry-mcp (33 stars, MIT) reads, parses, and searches .ged files exported from any genealogy platform, while airy10/GedcomMCP adds creation, editing, relationship analysis, and timeline generation. **Gramps Web is the best-served platform** with 4 independent implementations, led by cabout-me/gramps-mcp (25 stars, 16 tools) offering smart search across people, families, events, places, and sources, with data management and tree analysis. The Genealogy-MCP organization's fork adds 19 tools across 3 categories. The entire Gramps stack can be self-hosted, keeping sensitive family data private. **FamilySearch gets a dedicated MCP** (4 tools) for place search, date standardization, and Family Tree queries — useful since FamilySearch is the largest free genealogy platform with billions of records. **WikiTree has two implementations** — PeWu's TypeScript server (Apache-2.0, no auth required for public profiles) and Genealogy-MCP's Python version (10 tools including photos and categories). **The research-sources-mcp server is uniquely valuable** — it aggregates Library of Congress newspaper archives (Chronicling America), WikiTree, OpenArch.nl European records, and Find A Grave into a single search interface. The tree-analyzer-mcp catches data quality issues: duplicate persons via fuzzy matching, chronological inconsistencies, and missing source documentation. Major gaps: no official servers from the 'Big Four' genealogy platforms (Ancestry.com, FamilySearch, MyHeritage, Findmypast), no DNA/genetic genealogy analysis servers, no dedicated cemetery or memorial database integrations, no OCR tools for handwritten historical documents. The category earns 3.5/5 — impressive community organization around an open-source core (Gramps + GEDCOM), but limited by the lack of commercial platform integrations."
last_refreshed: 2026-03-15
---

Genealogy MCP servers let AI assistants explore family trees, parse GEDCOM files, search historical records, and analyze ancestral connections. Instead of manually navigating Gramps databases or exporting .ged files to different platforms, these servers let AI agents query your family history, discover relationships, validate data quality, and search across multiple genealogy platforms — all through the Model Context Protocol.

This review covers the **genealogy and family history** vertical — GEDCOM file handling, Gramps Web integration, FamilySearch access, WikiTree queries, historical record search, and data quality analysis. For DNA and genetic analysis tools, no dedicated MCP servers exist yet. For general document scanning and OCR, see our [PDF & Document MCP review](/reviews/pdf-document-mcp-servers/).

The headline findings: **Gramps Web is the best-served genealogy platform** with 4 independent MCP implementations, led by cabout-me/gramps-mcp (25 stars, 16 tools). **A dedicated Genealogy-MCP GitHub organization** maintains coordinated servers for FamilySearch, WikiTree, and Gramps. **GEDCOM remains the lingua franca** — ancestry-mcp (33 stars) handles the standard file format that every genealogy platform can export. **No major commercial genealogy platform has an official MCP server** — not Ancestry.com, MyHeritage, Findmypast, or even FamilySearch (the community built one instead).

## GEDCOM File Handling

### reeeeemo/ancestry-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) | 33 | Python | MIT | — |

The **most popular genealogy MCP server** by stars. Provides straightforward operations for working with GEDCOM (.ged) files — the universal format for genealogy data exchange. Key capabilities:

- **Read and parse** GEDCOM files exported from Ancestry.com, MyHeritage, FamilySearch, or any other platform
- **Search for individuals** and families within .ged files
- **Rename** GEDCOM files for organization
- **Security-restricted** directory operations — limits file access to configured directories

Available on PyPI as `mcp-server-ancestry`, making installation simple via pip. Works well as the first step in any genealogy workflow: export your tree as .ged from your platform, then let an AI agent query it.

### airy10/GedcomMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [airy10/GedcomMCP](https://github.com/airy10/GedcomMCP) | 3 | Python | MIT | — |

Goes beyond reading to **creating, editing, and querying** GEDCOM files. While ancestry-mcp focuses on search, GedcomMCP adds:

- **Relationship analysis** — identify how two individuals are connected
- **Family tree generation** — build visual tree structures from data
- **Timeline creation** — chronological event ordering for individuals and families
- **Data validation** — check for inconsistencies with backward compatibility for older GEDCOM formats
- **Automated documentation generation** — create reports from genealogical data

Good for researchers who need to both consume and produce GEDCOM files, or who want AI assistance in building new family trees from scratch.

## Gramps Web Integration

### cabout-me/gramps-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cabout-me/gramps-mcp](https://github.com/cabout-me/gramps-mcp) | 25 | Python | AGPL-3.0 | 16 |

The **most comprehensive genealogy MCP server** and the official community bridge to [Gramps](https://gramps-project.org/), the leading open-source genealogy application. Released September 2025, it connects AI assistants directly to your Gramps database through the Gramps Web API. The 16 tools span four categories:

- **Smart Search** — find people, families, events, places, and sources across your entire database with natural language queries
- **Data Management** — create and update genealogical records with proper validation
- **Tree Analysis** — trace descendants, ancestors, and family connections across generations
- **Relationship Discovery** — explore family connections and identify research gaps

The project name is inspired by "Kabouters" — helpful gnomes from Flemish folklore who work quietly behind the scenes. Fitting for a tool designed to do genealogical heavy lifting autonomously.

**Privacy advantage**: the entire stack can be self-hosted — your AI assistant, the MCP server, and the Gramps Web instance all run on your machine. No family data ever leaves your control. This matters for genealogy, where sensitive personal information about living relatives is common.

### Genealogy-MCP/gramps-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Genealogy-MCP/gramps-mcp](https://github.com/Genealogy-MCP/gramps-mcp) | — | Python | AGPL-3.0 | 19 |

A fork maintained by the **Genealogy-MCP organization** (more on them below) with 19 tools organized in 3 categories: Search & Retrieval, Data Management, and Analysis. Uses the FastMCP framework with httpx for async HTTP.

### Additional Gramps Servers

- **nikkoxgonzales/mcp-grampsweb** (1 star, TypeScript, MIT) — GQL-based search for genealogy entities (people, families, events, places), with record creation and family tree extraction
- **dsblank/gramps-ez-mcp** (2 stars, Python, GPL-2.0) — a simplified interface for querying Gramps data, designed for easy onboarding

Four independent Gramps MCP implementations make it the **best-served genealogy platform** — similar to how Home Assistant dominates the smart home MCP space.

## FamilySearch

### Genealogy-MCP/familysearch-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Genealogy-MCP/familysearch-mcp](https://github.com/Genealogy-MCP/familysearch-mcp) | — | Python | AGPL-3.0 | 4 |

Connects to [FamilySearch](https://www.familysearch.org/), the **world's largest free genealogy platform** with billions of historical records. The 4 tools cover:

- **Place search** — query the FamilySearch places database for standardized location names
- **Place details** — get detailed information about specific places (jurisdictions, coordinates, alternate names)
- **Date standardization** — convert informal date entries into standardized genealogical dates
- **Family Tree search** — search for individuals in the FamilySearch Family Tree

FamilySearch is operated by The Church of Jesus Christ of Latter-day Saints and provides free access to records that Ancestry.com charges for. Having MCP access to this data is significant for researchers who want AI-assisted discovery without paid subscriptions.

### dulbrich/familysearch-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| dulbrich/familysearch-mcp | — | TypeScript | — | 6 |

An alternative TypeScript implementation with broader FamilySearch API coverage:

- **Authentication** with FamilySearch credentials (stored locally in `~/.familysearch-mcp/config.json`)
- **User details** — retrieve authenticated user profile
- **Person search** — search the Family Tree by name, gender, birth/death dates and locations
- **Person details** — view detailed information by person ID
- **Ancestor exploration** — up to 8 generations of ancestors
- **Descendant exploration** — up to 3 generations of descendants
- **Historical record search** — search by surname, given name, dates, locations, or collection ID

Requires Node.js 16+ and a FamilySearch developer account with API credentials.

## WikiTree

### PeWu/wikitree-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PeWu/wikitree-mcp](https://github.com/PeWu/wikitree-mcp) | 1 | TypeScript | Apache-2.0 | — |

Integrates with the [WikiTree](https://www.wikitree.com/) API — a **free, collaborative genealogy platform** with over 38 million profiles. WikiTree's key differentiator is that profiles are public and collaboratively maintained (like Wikipedia for family trees). Capabilities:

- **Profile search** — find people across the WikiTree database
- **Ancestor/descendant lookup** — navigate family trees
- **Biography retrieval** — read biographical narratives
- **No authentication required** — public profiles are freely accessible

The developer notes the entire project was "vibe-coded" by Gemini CLI — an interesting meta-commentary on AI building tools for AI.

### Genealogy-MCP/wikitree-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Genealogy-MCP/wikitree-mcp](https://github.com/Genealogy-MCP/wikitree-mcp) | — | Python | AGPL-3.0 | 10 |

A more comprehensive WikiTree implementation with 10 tools:

- **Profile retrieval** and **person search**
- **Ancestor and descendant tree** navigation
- **Relative identification** — find how two profiles are connected
- **Biography and photo retrieval**
- **Category browsing** — explore WikiTree's organizational categories

Uses the FastMCP framework, consistent with the other Genealogy-MCP organization servers.

## Research Sources & Historical Records

### ibarrajo/research-sources-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ibarrajo/research-sources-mcp](https://github.com/ibarrajo/research-sources-mcp) | — | TypeScript | MIT | — |

The **most uniquely valuable server** in this category — it aggregates multiple historical record sources into a single search interface:

- **Library of Congress** — Chronicling America newspaper archives (millions of digitized US newspaper pages)
- **WikiTree** — collaborative family tree profiles
- **OpenArch.nl** — European historical records (primarily Dutch/Belgian civil and church records)
- **Find A Grave** — cemetery and memorial index search

No authentication required for most sources. This is the kind of multi-source aggregation that makes AI-powered research genuinely useful — instead of manually visiting four different websites, an AI agent can search them all at once and cross-reference results.

### robertefreeman/CLG-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robertefreeman/CLG-MCP](https://github.com/robertefreeman/CLG-MCP) | — | TypeScript | — | — |

Genealogy **resource discovery** through web scraping of [Cyndi's List](https://www.cyndislist.com/), one of the oldest and most comprehensive genealogy link directories. Search resources by names, locations, or keywords, browse category hierarchies, and filter results by multiple criteria. Designed for Cloudflare Workers' free tier — deployable at zero cost.

## Data Quality & Analysis

### ibarrajo/tree-analyzer-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ibarrajo/tree-analyzer-mcp](https://github.com/ibarrajo/tree-analyzer-mcp) | — | Python | MIT | — |

Focuses on **data quality** — a critical concern in genealogy where errors compound across generations:

- **Duplicate detection** — find duplicate persons through fuzzy matching (name variations, date approximations)
- **Chronological validation** — catch impossible dates (born after death, married before birth)
- **Missing source documentation** — locate unsourced claims that need evidence
- **Family tree error detection** — systematic quality checks

This is the kind of tool that becomes essential once a family tree grows past a few hundred people. Manual data validation at that scale is impractical.

## Research Infrastructure

### peterdewit/genealogy-postgres-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peterdewit/genealogy-postgres-mcp](https://github.com/peterdewit/genealogy-postgres-mcp) | — | Python | MIT | — |

A **persistent database backend** for AI-powered genealogical research. Stores people, relationships, events, locations, and evidence in PostgreSQL — providing a research memory and evidence store for AI agents. Supports HTTP streaming transport. Useful for long-running research projects where an AI agent needs to accumulate and retrieve findings across multiple sessions.

### ctrimm/local-mcp-server-ancestry

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ctrimm/local-mcp-server-ancestry](https://github.com/ctrimm/local-mcp-server-ancestry) | — | JavaScript | MIT | — |

Uses **browser automation** to interact with Ancestry.com directly — searching, extracting family tree data, and generating historical narratives. A scraping approach rather than API-based, which means it could break with site changes but provides access to Ancestry.com data without an official API.

## The Genealogy-MCP Organization

Worth highlighting: the [Genealogy-MCP](https://github.com/Genealogy-MCP) GitHub organization maintains coordinated MCP servers for FamilySearch, WikiTree, and Gramps Web — all using consistent architecture (Python, FastMCP, AGPL-3.0). This kind of organized, multi-platform approach is rare in the MCP ecosystem and gives genealogy researchers a coherent toolkit rather than disconnected one-off servers.

## What's Missing

The gaps in genealogy MCP are notable:

- **No official platform servers** — Ancestry.com, MyHeritage, Findmypast, and even FamilySearch have no official MCP servers
- **No DNA/genetic genealogy** — no servers for analyzing DNA matches, ethnicity estimates, haplogroups, or chromosome browsers from AncestryDNA, 23andMe, MyHeritage DNA, or FamilyTreeDNA
- **No OCR for historical documents** — handwritten church records, census forms, and vital records need specialized OCR that no genealogy MCP addresses
- **No cemetery/memorial databases** — only Find A Grave appears (via research-sources-mcp); no BillionGraves, Findagrave API, or memorial site integration
- **No newspaper archives** — beyond Library of Congress via research-sources-mcp, no Newspapers.com, British Newspaper Archive, or GenealogyBank servers
- **No immigration/ship records** — Ellis Island, Castle Garden, and passenger list databases are absent
- **No land/property records** — deed searches, land patents, and property records are a major genealogy source with no MCP coverage

## Bottom Line

Genealogy MCP servers earn **3.5 out of 5**. The category is niche but surprisingly well-organized — 15+ servers across GEDCOM handling, Gramps Web, FamilySearch, WikiTree, research aggregation, and data quality analysis.

**Gramps Web is the standout platform** with 4 independent implementations, led by cabout-me/gramps-mcp (25 stars, 16 tools). The self-hostable architecture means sensitive family data stays private. **The Genealogy-MCP organization** provides the most coherent multi-platform approach in the entire MCP ecosystem — coordinated servers for three major platforms using consistent tooling.

**GEDCOM support is solid** — ancestry-mcp (33 stars) handles the universal file format, and GedcomMCP adds creation and analysis capabilities. **The research-sources-mcp server** demonstrates the real power of AI-assisted genealogy: searching Library of Congress newspapers, WikiTree, OpenArch.nl, and Find A Grave simultaneously.

The category loses a point for the complete absence of DNA analysis tools, official platform integrations, and specialized OCR for historical documents. Genealogy is fundamentally a document-heavy research discipline, and the MCP ecosystem doesn't yet address the document side. But for tree management, record search, and data quality — the community has built a surprisingly capable toolkit.

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
