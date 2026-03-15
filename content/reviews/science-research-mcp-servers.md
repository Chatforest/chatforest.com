---
title: "Science & Research MCP Servers — arXiv, PubMed, Semantic Scholar, UniProt, Wolfram, Scientific Computing, and More"
date: 2026-03-16T12:30:00+09:00
description: "Science and research MCP servers are turning AI agents into research assistants — searching papers, analyzing citations, querying protein databases, and running mathematical computations via the Model Context Protocol. We reviewed 35+ servers across 5 subcategories. Academic Paper Search: blazickjp/arxiv-mcp-server (2,400 stars, Apache-2.0, Python — paper search/download/storage/analysis, the most popular science MCP server), openags/paper-search-mcp (796 stars, MIT, Python — 7 sources: arXiv, PubMed, bioRxiv, medRxiv, Google Scholar, IACR, Semantic Scholar), JackKuo666/semanticscholar-MCP-Server (52 stars, MIT, Python — paper search, citations, author details), benedict2310/Scientific-Papers-MCP (44 stars, TypeScript — 6 sources, 5 tools, citation analysis across arXiv/OpenAlex/PMC/Europe PMC/bioRxiv/CORE), zongmin-yu/semantic-scholar-fastmcp (16 tools for paper search/citation analysis), aringadre76/mcp-for-research (MIT, TypeScript — PubMed/Google Scholar/ArXiv/JSTOR consolidated into 5 tools), nanyang12138/Academic-MCP-Server, Ladvien/research_hub_mcp (Sci-Hub access). Scientific Computing: pathintegral-institute/mcp.science (117 stars, MIT, Python — 12+ specialized servers including Python sandboxed execution, Materials Project, SSH, GPAW DFT, Mathematica, Jupyter, web fetch, academic search), paraporoco/Wolfram-MCP (6 stars, MIT, Python — 11 tools for symbolic math/calculus/linear algebra/statistics via Wolfram Language), texra-ai/mcp-server-mathematica (Mathematica code execution via wolframscript), StoneDot/wolframalpha-mcp-server (Wolfram Alpha LLM API), akalaric/mcp-wolframalpha (Wolfram Alpha API), huhabla/calculator-mcp-server (advanced math with symbolic computation/statistics/matrix ops). Bioinformatics & Life Sciences: Augmented-Nature/UniProt-MCP-Server (18 stars, TypeScript — 26 tools across protein analysis/comparative genomics/structural biology/systems biology/batch processing/data integration), Augmented-Nature/PDB-MCP-Server (21 stars, JavaScript — Protein Data Bank structure search/download/quality validation), QuentinCody/uniprot-mcp-server (BLAST/cross-database mapping UniProt/Ensembl/PDB), TakumiY235/uniprot-mcp-server (protein function/sequence retrieval), bio-mcp BLAST server. Earth & Space Science: blake365/usgs-quakes-mcp (TypeScript — USGS earthquake search/details), jezweb/nasa-mcp-server (8 stars, Python — APOD/Mars rovers/asteroids/Earth imagery/media library). Gaps: no electronic lab notebooks (ELN), no LIMS, no chemistry/molecular modeling (RDKit, OpenBabel), no genomics (NCBI GenBank, Ensembl beyond UniProt cross-ref), no physics simulation, no observatory/telescope data (SDSS, ESO), no clinical trials (ClinicalTrials.gov), no patent search, no peer review workflow, no research funding databases (NIH Reporter, NSF). 35+ servers across 5 subcategories. Rating: 3.5/5."
og_description: "Science & Research MCP servers: arxiv-mcp-server (2,400 stars, Apache-2.0 — paper search/download/analysis), paper-search-mcp (796 stars, MIT — 7 academic sources), mcp.science (117 stars — 12+ scientific computing servers), UniProt MCP (26 bioinformatics tools), PDB MCP (protein structure access), Wolfram MCP (symbolic math). 35+ servers reviewed. Rating: 3.5/5."
content_type: "Review"
card_description: "Science and research MCP servers for AI-powered academic paper search, scientific computing, bioinformatics, and research workflows. **arXiv MCP dominates academic search** — blazickjp/arxiv-mcp-server (2,400 stars, Apache-2.0, Python) is the most popular science MCP server with paper search, download, local storage, and systematic research analysis prompts. For broader coverage, openags/paper-search-mcp (796 stars, MIT) searches 7 sources simultaneously — arXiv, PubMed, bioRxiv, medRxiv, Google Scholar, IACR ePrint, and Semantic Scholar — with standardized output across all databases. benedict2310/Scientific-Papers-MCP (44 stars, TypeScript) covers 6 sources including OpenAlex (200M+ papers), PMC (7M+), Europe PMC (40M+), and CORE (200M+), with citation analysis and top-cited paper discovery. Multiple Semantic Scholar servers provide citation network exploration — JackKuo666/semanticscholar-MCP-Server (52 stars, MIT) offers paper/author/citation tools, while zongmin-yu's FastMCP implementation exposes 16 tools with year-range filtering and sorting. **mcp.science is the scientific computing hub** — pathintegral-institute/mcp.science (117 stars, MIT, Python) bundles 12+ specialized MCP servers under one umbrella: sandboxed Python execution, Materials Project database access, SSH remote execution, GPAW density-functional-theory calculations, Mathematica integration, Jupyter kernel interaction, web content fetching, and academic search. Install any server with a single `uvx mcp-science <name>` command. For symbolic mathematics, paraporoco/Wolfram-MCP (6 stars, MIT) provides 11 tools — calculate, solve equations, integrate, differentiate, simplify, factor, expand, matrix operations, statistics, and arbitrary Wolfram Language execution. Multiple Wolfram Alpha API servers (StoneDot, akalaric, cnosuke, Garoth, SecretiveShell) provide computational knowledge access without a local Mathematica installation. texra-ai/mcp-server-mathematica executes Mathematica code via wolframscript for verification workflows. **Bioinformatics gets serious coverage** — Augmented-Nature/UniProt-MCP-Server (18 stars, TypeScript) is the most comprehensive life sciences MCP server with 26 tools spanning protein analysis, comparative genomics, structural biology, systems biology, batch processing, and external database integration. Output formats include JSON, FASTA, XML, TSV, GFF, and GenBank. The companion PDB-MCP-Server (21 stars, JavaScript) provides Protein Data Bank access with structure search, download in multiple formats (PDB, mmCIF, mmTF, XML), and quality validation metrics (resolution, R-values, Ramachandran, clash scores). QuentinCody/uniprot-mcp-server adds BLAST sequence similarity search and cross-database mapping between UniProt, Ensembl, and PDB. bio-mcp provides standalone NCBI BLAST access. **Earth and space science gets lightweight coverage** — blake365/usgs-quakes-mcp provides USGS earthquake data with natural-language queries, while jezweb/nasa-mcp-server (8 stars, Python) covers APOD, Mars rovers, asteroids, Earth imagery, and NASA's media library with smart caching. These complement the dedicated Geospatial and Weather MCP categories we've reviewed separately. **Major gaps remain in lab infrastructure** — no electronic lab notebooks (eLabFTW, SciNote), no LIMS integration, no chemistry tools (RDKit, OpenBabel, ChemDraw), no genomics databases (NCBI GenBank, Ensembl), no physics simulation, no observatory data (SDSS, ESO), no clinical trials (ClinicalTrials.gov), no patent search, no research funding databases (NIH Reporter, NSF Awards), and no peer review or manuscript submission workflows. The category earns 3.5/5 — academic paper search is genuinely strong with the arXiv server at 2,400 stars and multi-source aggregators covering billions of papers. Scientific computing has a solid foundation through mcp.science's 12-server bundle. Bioinformatics is surprisingly well-served for protein science. But everything beyond search-and-compute is missing — the lab bench, the wet lab, the clinical trial, the grant application, and the publication pipeline have no MCP representation."
---

Science and research MCP servers let AI assistants search academic literature, run mathematical computations, query protein databases, and analyze citation networks. Instead of manually searching PubMed, downloading PDFs from arXiv, or writing Wolfram Language scripts, researchers can have AI agents do this through the Model Context Protocol.

This review covers the **science and research** vertical — academic paper search, scientific computing, bioinformatics, and research tools. For geospatial analysis, see our [Geospatial & Mapping review](/reviews/geospatial-mapping-mcp-servers/). For weather and climate data, see our [Weather & Climate review](/reviews/weather-climate-mcp-servers/). For healthcare applications, see our [Healthcare & Medical review](/reviews/healthcare-medical-mcp-servers/).

The headline findings: **arXiv MCP server has 2,400 stars** — the most popular science-specific MCP server. **paper-search-mcp aggregates 7 academic sources** into a single interface. **mcp.science bundles 12+ scientific computing servers** under one project. **UniProt MCP provides 26 bioinformatics tools** for protein science. **Lab infrastructure is completely absent** — no ELN, no LIMS, no chemistry tools.

## Academic Paper Search

### blazickjp/arxiv-mcp-server (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 2,400 | Python | Apache-2.0 | 4 |

The **most starred science MCP server** — focused exclusively on arXiv with a clean, research-oriented design:

- **search_papers** — query arXiv with date range and category filtering
- **download_paper** — retrieve full papers by arXiv ID
- **list_papers** — view all locally stored papers
- **read_paper** — access downloaded paper content

Includes built-in prompts for systematic paper analysis: executive summaries, methodology evaluation, results assessment, and future research direction identification. Papers are stored locally for faster repeated access.

### openags/paper-search-mcp (Most Sources)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [paper-search-mcp](https://github.com/openags/paper-search-mcp) | 796 | Python | MIT | Multiple |

The **broadest academic search MCP** — aggregates 7 sources through a single interface:

- **arXiv** — STEM preprints
- **PubMed** — biomedical literature
- **bioRxiv** — biology preprints
- **medRxiv** — medical preprints
- **Google Scholar** — cross-disciplinary search
- **IACR ePrint Archive** — cryptography research
- **Semantic Scholar** — AI-enhanced citation data

Standardized output across all databases via a `Paper` class. Asynchronous requests for network efficiency. Extensible architecture for adding new sources.

### benedict2310/Scientific-Papers-MCP (Citation Analysis)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP) | 44 | TypeScript | — | 5 |

Covers **6 major academic sources** with citation-focused features:

- **arXiv** — 2.3M+ STEM preprints
- **OpenAlex** — 200M+ scholarly papers with citation data
- **PMC (PubMed Central)** — 7M+ biomedical full-text papers
- **Europe PMC** — 40M+ life sciences articles
- **bioRxiv/medRxiv** — 500K+ biology and medical preprints
- **CORE** — 200M+ open access research papers

Tools: `list_categories`, `fetch_latest`, `fetch_top_cited`, `search_papers`, `fetch_content`. The `fetch_top_cited` tool is particularly useful for literature reviews — find the most-cited papers on any topic since a given date. Published on npm as `@futurelab-studio/latest-science-mcp`.

### Semantic Scholar Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server) | 52 | Python | MIT | 4+ |
| [semantic-scholar-fastmcp](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server) | — | Python | — | 16 |
| [semantic-scholar-graph-api](https://github.com/alperenkocyigit/semantic-scholar-graph-api) | — | — | — | Multiple |

Multiple implementations of Semantic Scholar's API, which adds **AI-enhanced citation analysis** on top of raw paper data:

- **JackKuo666's version** (52 stars, MIT) — paper search, author details, citations, and references. Works with Claude Desktop, Cursor, Windsurf, and Cline.
- **zongmin-yu's FastMCP version** — 16 tools with year-range filtering, citation count sorting, and bulk search options.
- **alperenkocyigit's Graph API** — focuses on citation network exploration and literature reviews.
- **AIRA-SemanticScholar** (hamid-vakilzadeh) — Academic Graph API with intelligent literature search.

Semantic Scholar's corpus covers 200M+ papers with AI-generated citation contexts — useful for understanding not just *that* a paper was cited, but *how* it was used.

### Other Academic Search Servers

| Server | Language | License | Notes |
|--------|----------|---------|-------|
| [mcp-for-research](https://github.com/aringadre76/mcp-for-research) | TypeScript | MIT | PubMed/Google Scholar/ArXiv/JSTOR in 5 consolidated tools |
| [Academic-MCP-Server](https://github.com/nanyang12138/Academic-MCP-Server) | — | — | Academic paper search |
| [research_hub_mcp](https://github.com/Ladvien/research_hub_mcp) | — | — | Sci-Hub access for full-text retrieval |

The mcp-for-research server is notable for **consolidating 4 sources into just 5 tools** — research_search, paper_analysis, citation_manager (with APA/MLA/Chicago formatting), research_preferences, and web_research. Published on npm.

## Scientific Computing

### pathintegral-institute/mcp.science (Computing Hub)

| Server | Stars | Language | License | Servers |
|--------|-------|----------|---------|---------|
| [mcp.science](https://github.com/pathintegral-institute/mcp.science) | 117 | Python | MIT | 12+ |

The **most ambitious scientific computing MCP project** — a collection of specialized servers under one umbrella:

- **Python Code Execution** — sandboxed environment with restricted stdlib for safe computation
- **Materials Project** — access to the materials science database
- **SSH Exec** — remote command execution with whitelisted validation
- **GPAW** — density-functional-theory (DFT) calculations for computational physics/chemistry
- **Mathematica-Check** — Mathematica integration for symbolic verification
- **Jupyter-Act** — interact with Jupyter kernels
- **Web Fetch** — fetch and process HTML/PDF/text content
- **TXYZ Search** — academic and web resource search
- **TinyDB** — lightweight structured data storage
- **Timer**, **NEMAD** (neuroscience), and more

Install any server with: `uvx mcp-science <server-name>`. The DFT calculator is particularly notable — enabling AI agents to perform quantum chemistry calculations is a genuinely novel capability.

### Wolfram Language & Mathematica

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Wolfram-MCP](https://github.com/paraporoco/Wolfram-MCP) | 6 | Python | MIT | 11 |
| [mcp-server-mathematica](https://github.com/texra-ai/mcp-server-mathematica) | — | — | — | Multiple |

**Wolfram-MCP** provides 11 symbolic math tools via the Wolfram Language:

- `wolfram_calculate` — evaluate mathematical expressions
- `wolfram_solve` — solve algebraic and differential equations
- `wolfram_integrate` / `wolfram_differentiate` — calculus operations
- `wolfram_simplify` / `wolfram_factor` / `wolfram_expand` — algebraic manipulation
- `wolfram_matrix_operations` — linear algebra
- `wolfram_statistics` — statistical analysis
- `wolfram_execute` — arbitrary Wolfram Language code

Requires a local Wolfram Language/Mathematica installation. **mcp-server-mathematica** takes a different approach — executing Mathematica code via `wolframscript` for verification workflows in editors like Cursor.

### Wolfram Alpha API Servers

| Server | Notes |
|--------|-------|
| [wolframalpha-mcp-server](https://github.com/StoneDot/wolframalpha-mcp-server) | Wolfram Alpha LLM API — computational queries without local installation |
| [mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha) | Python — structured knowledge retrieval |
| [mcp-wolfram-alpha](https://github.com/cnosuke/mcp-wolfram-alpha) | Wolfram Alpha via API |
| [wolframalpha-llm-mcp](https://github.com/Garoth/wolframalpha-llm-mcp) | Structured knowledge and math solving |
| [MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) | Chat REPL to Wolfram Alpha |

Five separate Wolfram Alpha MCP implementations — all solving the same problem (connecting AI to Wolfram Alpha's computational knowledge engine) with slight API differences. No local Mathematica license needed — these use the Wolfram Alpha API, which has free and paid tiers.

### calculator-mcp-server

| Server | Language | License | Notes |
|--------|----------|---------|-------|
| [calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server) | — | — | Symbolic math, statistics, matrix operations |

For users who don't need Wolfram's full power — provides advanced mathematical calculations including symbolic computation, statistical analysis, and matrix operations without external API dependencies.

## Bioinformatics & Life Sciences

### Augmented-Nature/UniProt-MCP-Server (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server) | 18 | TypeScript | — | 26 |

The **most comprehensive life sciences MCP server** — 26 tools across 6 categories:

- **Protein Analysis** (5 tools) — search, detailed info, gene lookup, sequences, features
- **Comparative Genomics** (4 tools) — comparison, homologs, orthologs, phylogenetics
- **Structural Biology** (4 tools) — 3D structures, domains, variants, composition
- **Systems Biology** (4 tools) — pathways, interactions, functional classification, localization
- **Batch Processing** (3 tools) — multi-protein processing, advanced filtering, taxonomic search
- **Data Integration** (3 tools) — external database links, literature, annotation quality

Supports JSON, FASTA, XML, TSV, GFF, and GenBank output formats. Docker deployment available. This is the kind of deep, domain-specific MCP server that makes AI genuinely useful for bench scientists — asking "what proteins interact with BRCA1 and are localized to the nucleus?" becomes a single tool call.

### Augmented-Nature/PDB-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server) | 21 | JavaScript | — | 5 |

Access to the **Protein Data Bank** — the global repository of 3D structures for proteins, nucleic acids, and complex assemblies:

- `search_structures` — find structures by query
- `get_structure_info` — detailed metadata
- `download_structure` — retrieve in PDB, mmCIF, mmTF, or XML format
- `search_by_uniprot` — cross-reference from UniProt accession
- `get_structure_quality` — validation metrics (resolution, R-values, Ramachandran stats, clash scores, rotamer analysis)

Designed to complement the UniProt MCP server — together they cover the protein sequence-to-structure pipeline.

### Other Bioinformatics Servers

| Server | Notes |
|--------|-------|
| [uniprot-mcp-server](https://github.com/QuentinCody/uniprot-mcp-server) (QuentinCody) | BLAST sequence similarity search + cross-database mapping (UniProt/Ensembl/PDB) |
| [uniprot-mcp-server](https://github.com/TakumiY235/uniprot-mcp-server) (TakumiY235) | Lightweight protein function and sequence retrieval |
| bio-mcp BLAST | Standalone NCBI BLAST access |

QuentinCody's version is notable for **BLAST integration** — submit a protein sequence and find similar sequences across databases, with asynchronous job processing for long-running alignments.

## Earth & Space Science

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [usgs-quakes-mcp](https://github.com/blake365/usgs-quakes-mcp) | — | TypeScript | — | 2 |
| [nasa-mcp-server](https://github.com/jezweb/nasa-mcp-server) | 8 | Python | — | 12+ |

**USGS Earthquake server** provides `find-earthquakes` and `find-earthquake-details` — translating natural-language queries ("earthquakes over magnitude 5 in California last month") into USGS API calls.

**NASA MCP server** covers APOD (Astronomy Picture of the Day), Mars rover photos (Curiosity, Perseverance, Opportunity, Spirit), asteroid tracking with hazard identification, Earth imagery, and NASA's media library. Smart caching (30 min for images, 10 min for dynamic data) and rate-limit awareness.

These complement our dedicated [Geospatial & Mapping](/reviews/geospatial-mapping-mcp-servers/) and [Weather & Climate](/reviews/weather-climate-mcp-servers/) reviews, which cover Earth observation and atmospheric data in depth.

## What's Missing

The gaps in science MCP servers reveal where AI-assisted research hasn't reached yet:

- **Electronic Lab Notebooks** — no eLabFTW, SciNote, or Benchling MCP integration. Experiment logging is still manual.
- **LIMS** — no Laboratory Information Management Systems connected to MCP. Sample tracking, instrument data, and quality control remain siloed.
- **Chemistry & Molecular Modeling** — no RDKit, OpenBabel, ChemDraw, or molecular dynamics tools. Computational chemistry beyond mcp.science's DFT is absent.
- **Genomics** — no NCBI GenBank, no Ensembl (beyond UniProt cross-references), no ENCODE, no genome browsers.
- **Physics Simulation** — no COMSOL, ANSYS, or OpenFOAM integration.
- **Observatory Data** — no SDSS (Sloan Digital Sky Survey), no ESO, no Hubble/JWST archive access.
- **Clinical Trials** — no ClinicalTrials.gov search or registration tools.
- **Patent Search** — no Google Patents, USPTO, or EPO integration.
- **Research Funding** — no NIH Reporter, no NSF Awards, no grant search databases.
- **Peer Review & Publishing** — no manuscript submission, no reviewer assignment, no journal recommendation workflows.

## The Bottom Line

Science and research MCP servers are **strong for literature search and protein science, but thin everywhere else**.

The **arXiv MCP server at 2,400 stars** proves that researchers want AI-assisted paper discovery. The multi-source aggregators (paper-search-mcp covering 7 databases, Scientific-Papers-MCP covering 6 with 200M+ papers through CORE and OpenAlex) mean that literature review workflows are genuinely accelerated. Citation analysis through Semantic Scholar adds context to the raw search results.

**Scientific computing has a solid foundation** through mcp.science's 12-server bundle — particularly the DFT calculator for quantum chemistry and the Materials Project integration. Wolfram Language integration gives agents access to one of the most powerful symbolic computation engines available, though requiring a local license limits accessibility. The five Wolfram Alpha API servers provide a license-free alternative for computational knowledge queries.

**Bioinformatics punches above its weight** — the Augmented Nature team's UniProt (26 tools) and PDB (5 tools with quality validation) servers provide genuine research utility for protein scientists. The sequence-to-structure pipeline is well-covered, and BLAST integration enables homology search.

**Everything else is missing.** The wet lab, the chemistry bench, the genome sequencer, the telescope, the clinical trial, the grant application — none of these have MCP integration. Science is a vast domain, and MCP coverage barely scratches the surface beyond "search papers" and "do math."

**Rating: 3.5 out of 5** — academic paper search is excellent, scientific computing is solid, bioinformatics is surprisingly deep, but the absence of lab infrastructure, chemistry tools, genomics databases, and research workflow integration keeps this from a higher score. The arXiv server's 2,400 stars show strong demand; the ecosystem needs to follow that signal into the lab.

---

*This review covers MCP servers available as of March 2026. Star counts are approximate and change over time. ChatForest researches MCP servers through documentation, GitHub repositories, and community directories — we do not test servers hands-on. For corrections or additions, visit our [GitHub](https://github.com/thunderrabbit/chatforest.com).*
