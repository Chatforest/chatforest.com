# Genealogy & Family History MCP Servers — GEDCOM, Gramps, FamilySearch, WikiTree, and More

> Genealogy MCP servers let AI agents explore family trees, parse GEDCOM files, and search historical records. We found 15+ servers across 6 subcategories — updated April 2026 with verified star counts, tool counts, and inline citations.


Genealogy MCP servers let AI assistants explore family trees, parse GEDCOM files, search historical records, and analyze ancestral connections. Instead of manually navigating Gramps databases or exporting .ged files to different platforms, these servers let AI agents query your family history, discover relationships, validate data quality, and search across multiple genealogy platforms — all through the Model Context Protocol.

This review covers the **genealogy and family history** vertical — GEDCOM file handling, Gramps Web integration, FamilySearch access, WikiTree queries, historical record search, and data quality analysis. For DNA and genetic analysis tools, no dedicated MCP servers exist yet. For general document scanning and OCR, see our [PDF & Document MCP review](/reviews/pdf-document-mcp-servers/).

The headline findings: **Gramps Web is the best-served genealogy platform** with 4 independent MCP implementations, led by cabout-me/gramps-mcp ([29 stars](https://github.com/cabout-me/gramps-mcp/stargazers), 16 tools). **A dedicated [Genealogy-MCP GitHub organization](https://github.com/Genealogy-MCP)** maintains coordinated servers for WikiTree, Gramps, and GEDCOM. **GEDCOM remains the lingua franca** — GedcomMCP ([7 stars](https://github.com/airy10/GedcomMCP/stargazers), [53 tools](https://github.com/airy10/GedcomMCP/blob/main/src/gedcom_mcp/fastmcp_server.py)) is now the most feature-rich genealogy MCP server, while the original ancestry-mcp ([34 stars](https://github.com/reeeeemo/ancestry-mcp/stargazers)) has been **archived and deprecated**. **No major commercial genealogy platform has an official MCP server** — not Ancestry.com, MyHeritage, Findmypast, or even FamilySearch (though a community server exists via [smithery-ai](https://github.com/smithery-ai/familysearch-mcp)).

**Category:** [Lifestyle & Personal](/categories/lifestyle-personal/)

## GEDCOM File Handling

### reeeeemo/ancestry-mcp ⚠️ Archived

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [reeeeemo/ancestry-mcp](https://github.com/reeeeemo/ancestry-mcp) | [34](https://github.com/reeeeemo/ancestry-mcp/stargazers) | Python | MIT | [3](https://github.com/reeeeemo/ancestry-mcp#readme) |

**⚠️ Archived and deprecated** as of January 2026. The repo is now read-only and the author notes it used a [2024-11-26 snapshot of MCP](https://github.com/reeeeemo/ancestry-mcp). Still the most-starred genealogy MCP server, but no longer maintained. The 3 tools (list_files, rename_file, view_file) provide basic GEDCOM (.ged) file operations:

- **List files** in configured directories
- **View/parse** GEDCOM files exported from Ancestry.com, MyHeritage, FamilySearch, or any other platform
- **Rename** GEDCOM files for organization

Available on PyPI as `mcp-server-ancestry`. For active GEDCOM development, consider GedcomMCP (below) or Genealogy-MCP/gedcom-mcp instead.

### airy10/GedcomMCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [airy10/GedcomMCP](https://github.com/airy10/GedcomMCP) | [7](https://github.com/airy10/GedcomMCP/stargazers) | Python | MIT | [53](https://github.com/airy10/GedcomMCP/blob/main/src/gedcom_mcp/fastmcp_server.py) |

The **most feature-rich genealogy MCP server** with [53 tools](https://github.com/airy10/GedcomMCP/blob/main/src/gedcom_mcp/fastmcp_server.py) spanning GEDCOM file creation, editing, querying, and analysis. Latest release: [v0.1.0a4](https://github.com/airy10/GedcomMCP/releases). Key capability areas:

- **Search & retrieval** — find_person, fuzzy_search_person, query_people_by_criteria, get_person_details, get_events, get_notes, get_sources
- **Relationship analysis** — find_shortest_relationship_path, find_all_paths_to_ancestor, get_common_ancestors, get_ancestors, get_descendants
- **Family tree operations** — get_family_tree_summary, get_surname_statistics, get_date_range_analysis, get_statistics
- **Data creation & editing** — add_person, update_person, create_source, new_empty_gedcom, save_gedcom
- **Data quality** — find_potential_duplicates, get_date_certainty, normalize_name, find_name_variants
- **Batch operations** — get_persons_batch, batch_update_person_attributes

With ancestry-mcp now archived, GedcomMCP is the **primary active GEDCOM MCP server**. Good for researchers who need to both consume and produce GEDCOM files, or who want AI assistance in building new family trees from scratch.

### Genealogy-MCP/gedcom-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Genealogy-MCP/gedcom-mcp](https://github.com/Genealogy-MCP/gedcom-mcp) | [2](https://github.com/Genealogy-MCP/gedcom-mcp/stargazers) | Python | AGPL-3.0 | [7](https://github.com/Genealogy-MCP/gedcom-mcp#readme) |

A focused GEDCOM server from the [Genealogy-MCP organization](https://github.com/Genealogy-MCP) — lighter than GedcomMCP's 53 tools but designed for seamless integration with the org's other servers. The [7 tools](https://github.com/Genealogy-MCP/gedcom-mcp#readme) cover core operations:

- **load_file** — load and parse local .ged files
- **search_persons** — search by name, dates, place, sex
- **get_person** / **get_family** — retrieve records by cross-reference ID
- **get_ancestors** / **get_descendants** — tree traversal
- **get_stats** — file-level statistics

Supports both local (uv) and Docker deployment. Primary development is on [GitLab](https://gitlab.com/genealogy-mcp/gedcom-mcp); the GitHub repo is a read-only mirror.

## Gramps Web Integration

### cabout-me/gramps-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [cabout-me/gramps-mcp](https://github.com/cabout-me/gramps-mcp) | [29](https://github.com/cabout-me/gramps-mcp/stargazers) | Python | AGPL-3.0 | [16](https://github.com/cabout-me/gramps-mcp#readme) |

The **most comprehensive Gramps MCP server** and the official community bridge to [Gramps](https://gramps-project.org/), the leading open-source genealogy application. Released September 2025 ([v1.1.0](https://github.com/cabout-me/gramps-mcp/releases/tag/v1.1.0)), it connects AI assistants directly to your Gramps database through the Gramps Web API. The [16 tools](https://github.com/cabout-me/gramps-mcp#readme) span four categories:

- **Smart Search** — find people, families, events, places, and sources across your entire database with natural language queries
- **Data Management** — create and update genealogical records with proper validation
- **Tree Analysis** — trace descendants, ancestors, and family connections across generations
- **Relationship Discovery** — explore family connections and identify research gaps

The project name is inspired by "Kabouters" — helpful gnomes from Flemish folklore who work quietly behind the scenes. Fitting for a tool designed to do genealogical heavy lifting autonomously.

**Privacy advantage**: the entire stack can be self-hosted — your AI assistant, the MCP server, and the Gramps Web instance all run on your machine. No family data ever leaves your control. This matters for genealogy, where sensitive personal information about living relatives is common.

### Genealogy-MCP/gramps-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Genealogy-MCP/gramps-mcp](https://github.com/Genealogy-MCP/gramps-mcp) | [1](https://github.com/Genealogy-MCP/gramps-mcp/stargazers) | Python | AGPL-3.0 | [19 operations via 2 meta-tools](https://github.com/Genealogy-MCP/gramps-mcp#readme) |

Maintained by the **Genealogy-MCP organization** (more on them below) with [19 operations](https://github.com/Genealogy-MCP/gramps-mcp#readme) exposed through a "Code Mode" architecture — 2 meta-tools (search, execute) that reduce token overhead while providing the same capabilities: search, search_text, list_tags, get, get_tree_stats, upsert operations for all entity types, delete, get_ancestors, get_descendants, and get_recent_changes. Latest release: [v2.2.1](https://github.com/Genealogy-MCP/gramps-mcp/releases/tag/v2.2.1) (March 2026). Very actively maintained — last commit [April 2026](https://github.com/Genealogy-MCP/gramps-mcp/commits/main). Primary development on [GitLab](https://gitlab.com/genealogy-mcp/gramps-mcp).

### Additional Gramps Servers

- **[nikkoxgonzales/mcp-grampsweb](https://github.com/nikkoxgonzales/mcp-grampsweb)** ([1 star](https://github.com/nikkoxgonzales/mcp-grampsweb/stargazers), TypeScript, MIT, [16 tools](https://github.com/nikkoxgonzales/mcp-grampsweb#readme)) — full Gramps Web bridge with search, entity creation, and tree extraction. Latest release: [v1.3.5](https://github.com/nikkoxgonzales/mcp-grampsweb/releases/tag/v1.3.5) (February 2026)
- **[dsblank/gramps-ez-mcp](https://github.com/dsblank/gramps-ez-mcp)** ([2 stars](https://github.com/dsblank/gramps-ez-mcp/stargazers), Python, GPL-2.0, [14 tools](https://github.com/dsblank/gramps-ez-mcp/blob/main/tools.py)) — read-only interface for querying Gramps data (person lookup, family navigation, birth/death details, events). Author is a Gramps project contributor. Release: [v0.0.1](https://github.com/dsblank/gramps-ez-mcp/releases/tag/v0.0.1)

Four independent Gramps MCP implementations make it the **best-served genealogy platform** — similar to how Home Assistant dominates the smart home MCP space.

## FamilySearch

### smithery-ai/familysearch-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [smithery-ai/familysearch-mcp](https://github.com/smithery-ai/familysearch-mcp) | [3](https://github.com/smithery-ai/familysearch-mcp/stargazers) | TypeScript | ISC | Multiple |

Connects to [FamilySearch](https://www.familysearch.org/), the **world's largest free genealogy platform** with billions of historical records. Capabilities include:

- **Authentication** with FamilySearch credentials (config, auth, account info)
- **Family Tree access** — person search, individual details, ancestor exploration (up to 8 generations), descendant exploration (up to 3 generations)
- **Historical record search** — search by surname, given name, dates, locations, or collection ID

Requires Node.js 16+ and a FamilySearch developer account with API credentials.

FamilySearch is operated by The Church of Jesus Christ of Latter-day Saints and provides free access to records that Ancestry.com charges for. Having MCP access to this data is significant for researchers who want AI-assisted discovery without paid subscriptions.

**Note:** This category has seen churn — a previous implementation (dulbrich/familysearch-mcp) was deleted from GitHub, and the Genealogy-MCP organization does not maintain a FamilySearch server despite [their coverage of WikiTree and Gramps](https://github.com/Genealogy-MCP). The smithery-ai version appears to be a continuation of the earlier work.

## WikiTree

### PeWu/wikitree-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PeWu/wikitree-mcp](https://github.com/PeWu/wikitree-mcp) | [1](https://github.com/PeWu/wikitree-mcp/stargazers) | TypeScript | Apache-2.0 | [5](https://github.com/PeWu/wikitree-mcp#readme) |

Integrates with the [WikiTree](https://www.wikitree.com/) API — a **free, collaborative genealogy platform** with over 38 million profiles. WikiTree's key differentiator is that profiles are public and collaboratively maintained (like Wikipedia for family trees). The [5 tools](https://github.com/PeWu/wikitree-mcp#readme):

- **get_person** — retrieve profile details
- **get_ancestors** / **get_descendants** — navigate family trees
- **get_relatives** — find connected profiles
- **call_api** — direct WikiTree API access for advanced queries
- **No authentication required** — public profiles are freely accessible

The developer notes the entire project was "vibe-coded" by Gemini CLI — an interesting meta-commentary on AI building tools for AI.

### Genealogy-MCP/wikitree-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Genealogy-MCP/wikitree-mcp](https://github.com/Genealogy-MCP/wikitree-mcp) | [1](https://github.com/Genealogy-MCP/wikitree-mcp/stargazers) | Python | AGPL-3.0 | [12 (2 meta-tools, 10 operations)](https://github.com/Genealogy-MCP/wikitree-mcp#readme) |

A more comprehensive WikiTree implementation with [10 operations](https://github.com/Genealogy-MCP/wikitree-mcp#readme) exposed through the same search/execute meta-tool pattern as the org's Gramps server:

- **get_profile**, **get_person**, **get_people**, **search_person** — profile access and search
- **get_ancestors** / **get_descendants** / **get_relatives** — tree navigation
- **get_bio** / **get_photos** — biographical content
- **get_categories** — explore WikiTree's organizational categories

Latest release: [v0.1.0](https://github.com/Genealogy-MCP/wikitree-mcp/releases/tag/v0.1.0). Very active — last commit [April 2026](https://github.com/Genealogy-MCP/wikitree-mcp/commits/main). Primary development on [GitLab](https://gitlab.com/genealogy-mcp/wikitree-mcp).

## Research Sources & Historical Records

### ibarrajo/research-sources-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ibarrajo/research-sources-mcp](https://github.com/ibarrajo/research-sources-mcp) | 0 | TypeScript | MIT | [7](https://github.com/ibarrajo/research-sources-mcp#readme) |

The **most uniquely valuable server** in this category — [7 tools](https://github.com/ibarrajo/research-sources-mcp#readme) that aggregate multiple historical record sources into a single search interface:

- **search_newspapers** / **get_newspaper_page** — Library of Congress Chronicling America archives (millions of digitized US newspaper pages)
- **search_wikitree** / **get_wikitree_person** — collaborative family tree profiles
- **search_open_archives** — OpenArch.nl European historical records (primarily Dutch/Belgian civil and church records)
- **search_findagrave_via_fs** — Find A Grave cemetery and memorial index
- **cross_reference_person** — search across all sources simultaneously

No authentication required for most sources. The cross_reference_person tool is the standout — instead of manually visiting four different websites, an AI agent searches them all at once.

### robertefreeman/CLG-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [robertefreeman/CLG-MCP](https://github.com/robertefreeman/CLG-MCP) | 0 | TypeScript | — | [5](https://github.com/robertefreeman/CLG-MCP#readme) |

Genealogy **resource discovery** through web scraping of [Cyndi's List](https://www.cyndislist.com/), one of the oldest and most comprehensive genealogy link directories. The [5 tools](https://github.com/robertefreeman/CLG-MCP#readme) (search_genealogy_resources, browse_categories, get_resource_details, filter_resources, get_location_resources) let you search by names, locations, or keywords, browse category hierarchies, and filter results. Designed for Cloudflare Workers' free tier — deployable at zero cost. Note: no activity since [June 2025](https://github.com/robertefreeman/CLG-MCP/commits/main).

## Data Quality & Analysis

### ibarrajo/tree-analyzer-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ibarrajo/tree-analyzer-mcp](https://github.com/ibarrajo/tree-analyzer-mcp) | 0 | Python | MIT | [8](https://github.com/ibarrajo/tree-analyzer-mcp#readme) |

Focuses on **data quality** with [8 tools](https://github.com/ibarrajo/tree-analyzer-mcp#readme) — a critical concern in genealogy where errors compound across generations:

- **detect_name_duplicates** — find duplicate persons through fuzzy matching (name variations, date approximations)
- **validate_timeline** — catch impossible dates (born after death, married before birth)
- **check_relationships** — verify family connection consistency
- **analyze_source_coverage** — locate unsourced claims that need evidence
- **generate_person_profile** / **compare_persons** — individual analysis
- **generate_audit_report** / **generate_research_leads** — systematic quality reports

This is the kind of tool that becomes essential once a family tree grows past a few hundred people. Manual data validation at that scale is impractical.

## Research Infrastructure

### peterdewit/genealogy-postgres-mcp

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [peterdewit/genealogy-postgres-mcp](https://github.com/peterdewit/genealogy-postgres-mcp) | 0 | Python | MIT | [16](https://github.com/peterdewit/genealogy-postgres-mcp#readme) |

A **persistent database backend** for AI-powered genealogical research with [16 tools](https://github.com/peterdewit/genealogy-postgres-mcp#readme) spanning person management (4), relationships (3), events (3), locations (2), and assertions/sources (4). Stores people, relationships, events, locations, and evidence in PostgreSQL — providing a research memory and evidence store for AI agents. Supports HTTP streaming transport. Useful for long-running research projects where an AI agent needs to accumulate and retrieve findings across multiple sessions.

### ctrimm/local-mcp-server-ancestry

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ctrimm/local-mcp-server-ancestry](https://github.com/ctrimm/local-mcp-server-ancestry) | 0 | JavaScript | MIT | [7](https://github.com/ctrimm/local-mcp-server-ancestry#readme) |

Uses **browser automation** to interact with Ancestry.com directly with [7 tools](https://github.com/ctrimm/local-mcp-server-ancestry#readme): ancestry_login, ancestry_search_person, ancestry_get_person_details, ancestry_get_tree_view, ancestry_get_records, ancestry_get_timeline, and generate_historical_narrative. A scraping approach rather than API-based, which means it could break with site changes but provides access to Ancestry.com data without an official API.

## The Genealogy-MCP Organization

Worth highlighting: the [Genealogy-MCP](https://github.com/Genealogy-MCP) GitHub organization (founded March 2026) maintains coordinated MCP servers for **WikiTree, Gramps Web, and GEDCOM** — all using consistent architecture (Python, FastMCP, AGPL-3.0) with a shared search/execute meta-tool pattern that reduces token overhead. The org has [4 public repos](https://github.com/orgs/Genealogy-MCP/repositories): [gramps-mcp](https://github.com/Genealogy-MCP/gramps-mcp), [wikitree-mcp](https://github.com/Genealogy-MCP/wikitree-mcp), [gedcom-mcp](https://github.com/Genealogy-MCP/gedcom-mcp), and a [.github profile](https://github.com/Genealogy-MCP/.github). Primary development happens on [GitLab](https://gitlab.com/genealogy-mcp); GitHub repos are read-only mirrors. This kind of organized, multi-platform approach is rare in the MCP ecosystem and gives genealogy researchers a coherent toolkit rather than disconnected one-off servers.

**Note:** Our original review listed a Genealogy-MCP/familysearch-mcp server — this repo does not exist in the org and may have been confused with dulbrich/familysearch-mcp (now deleted) or planned but never published.

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

**Gramps Web is the standout platform** with 4 independent implementations, led by cabout-me/gramps-mcp ([29 stars](https://github.com/cabout-me/gramps-mcp/stargazers), [16 tools](https://github.com/cabout-me/gramps-mcp#readme)). The self-hostable architecture means sensitive family data stays private. **The [Genealogy-MCP organization](https://github.com/Genealogy-MCP)** provides the most coherent multi-platform approach in the entire MCP ecosystem — coordinated servers for WikiTree, Gramps, and GEDCOM using consistent tooling and a shared meta-tool architecture.

**GEDCOM support has evolved** — the original ancestry-mcp ([34 stars](https://github.com/reeeeemo/ancestry-mcp/stargazers)) is now archived, but GedcomMCP ([7 stars](https://github.com/airy10/GedcomMCP/stargazers), [53 tools](https://github.com/airy10/GedcomMCP/blob/main/src/gedcom_mcp/fastmcp_server.py)) has grown into the most feature-rich genealogy MCP server, and Genealogy-MCP/gedcom-mcp offers a lighter alternative. **The research-sources-mcp server** demonstrates the real power of AI-assisted genealogy: its [cross_reference_person tool](https://github.com/ibarrajo/research-sources-mcp#readme) searches Library of Congress newspapers, WikiTree, OpenArch.nl, and Find A Grave simultaneously.

**FamilySearch coverage has thinned** — only one active community server remains ([smithery-ai/familysearch-mcp](https://github.com/smithery-ai/familysearch-mcp)), down from two in our original review. The category still loses a point for the absence of DNA analysis tools, official platform integrations, and specialized OCR for historical documents. Genealogy is fundamentally a document-heavy research discipline, and the MCP ecosystem doesn't yet address the document side. But for tree management, record search, and data quality — the community has built a surprisingly capable toolkit.

*This review was last updated on 2026-04-12 using Claude Opus 4.6 (Anthropic). Star counts, tool counts, and repo statuses verified against GitHub on the same date.*

