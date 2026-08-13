# Science & Research MCP Servers — arXiv, PubMed, Semantic Scholar, UniProt, Wolfram, Scientific Computing, and More

> Science and research MCP servers are turning AI agents into research assistants — searching papers, analyzing citations, querying protein databases, and running mathematical


Science and research MCP servers let AI assistants search academic literature, run mathematical computations, query protein databases, and analyze citation networks. Instead of manually searching PubMed, downloading PDFs from arXiv, or writing Wolfram Language scripts, researchers can have AI agents do this through the Model Context Protocol. Part of our **[Science & Research MCP category](/categories/science-research/)**.

This review covers the **science and research** vertical — academic paper search, scientific computing, bioinformatics, and research tools. For geospatial analysis, see our [Geospatial & Mapping review](/reviews/geospatial-mapping-mcp-servers/). For weather and climate data, see our [Weather & Climate review](/reviews/weather-climate-mcp-servers/). For healthcare applications, see our [Healthcare & Medical review](/reviews/healthcare-medical-mcp-servers/).

The headline findings: **[arXiv MCP server](https://github.com/blazickjp/arxiv-mcp-server) has 3,046 stars** — the most popular science-specific MCP server. **[paper-search-mcp](https://github.com/openags/paper-search-mcp) aggregates 7 academic sources** into a single interface. **[mcp.science](https://github.com/pathintegral-institute/mcp.science) bundles 12 scientific computing servers** under one project. **[UniProt MCP](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server) provides 26 bioinformatics tools** for protein science. **Lab infrastructure is completely absent** — no ELN, no LIMS, no chemistry tools.

## Academic Paper Search

### blazickjp/arxiv-mcp-server (Most Popular)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [arxiv-mcp-server](https://github.com/blazickjp/arxiv-mcp-server) | 3,046 | Python | Apache-2.0 | 4 |

The **most starred science MCP server** — focused exclusively on arXiv with a clean, research-oriented design:

- **search_papers** — query arXiv with date range and category filtering
- **download_paper** — retrieve full papers by arXiv ID
- **list_papers** — view all locally stored papers
- **read_paper** — access downloaded paper content

Includes built-in prompts for systematic paper analysis: executive summaries, methodology evaluation, results assessment, and future research direction identification. Papers are stored locally for faster repeated access.

### openags/paper-search-mcp (Most Sources)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [paper-search-mcp](https://github.com/openags/paper-search-mcp) | 2,415 | Python | MIT | Multiple |

The **broadest academic search MCP** — aggregates 7 sources through a single interface:

- **[arXiv](https://arxiv.org/)** — STEM preprints (3.1M+ total submissions as of [arXiv's own submission statistics](https://arxiv.org/stats/monthly_submissions))
- **PubMed** — biomedical literature
- **[bioRxiv/medRxiv](https://www.biorxiv.org/about/FAQ)** — biology and medical preprints
- **Google Scholar** — cross-disciplinary search
- **IACR ePrint Archive** — cryptography research
- **Semantic Scholar** — AI-enhanced citation data

Standardized output across all databases via a `Paper` class. Asynchronous requests for network efficiency. Extensible architecture for adding new sources.

### benedict2310/Scientific-Papers-MCP (Citation Analysis)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Scientific-Papers-MCP](https://github.com/benedict2310/Scientific-Papers-MCP) | 55 | TypeScript | — | 5 |

Covers **6 major academic sources** with citation-focused features:

- **[arXiv](https://arxiv.org/stats/monthly_submissions)** — 3.1M+ total submissions
- **[OpenAlex](https://blog.openalex.org/openalex-2026-roadmap/)** — 477M+ indexed scholarly works with citation data
- **[PMC (PubMed Central)](https://pmc.ncbi.nlm.nih.gov/?db=PMC)** — 12.3M+ biomedical full-text articles
- **[Europe PMC](https://www.ebi.ac.uk/training/online/courses/europepmc-quick-tour/what-is-europe-pmc/)** — 46M+ abstracts, 10.7M+ full-text articles
- **[bioRxiv/medRxiv](https://www.biorxiv.org/about/FAQ)** — biology and medical preprints
- **[CORE](https://core.ac.uk/)** — 290M+ metadata records, 40M+ full-text open-access papers, per [CORE's own service description](https://www.nature.com/articles/s41597-023-02208-w)

Tools: `list_categories`, `fetch_latest`, `fetch_top_cited`, `search_papers`, `fetch_content`. The `fetch_top_cited` tool is particularly useful for literature reviews — find the most-cited papers on any topic since a given date. Published on npm as `@futurelab-studio/latest-science-mcp`.

### Semantic Scholar Servers

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [semanticscholar-MCP-Server](https://github.com/JackKuo666/semanticscholar-MCP-Server) | 78 | Python | MIT | 4+ |
| [semantic-scholar-fastmcp](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server) | 164 | Python | MIT | 16 |
| [semantic-scholar-graph-api](https://github.com/alperenkocyigit/semantic-scholar-graph-api) | 15 | — | — | Multiple |

Multiple implementations of Semantic Scholar's API, which adds **AI-enhanced citation analysis** on top of raw paper data:

- **JackKuo666's version** (78 stars, MIT) — paper search, author details, citations, and references. Works with Claude Desktop, Cursor, Windsurf, and Cline.
- **zongmin-yu's FastMCP version** (164 stars) — 16 tools with year-range filtering, citation count sorting, and bulk search options.
- **alperenkocyigit's Graph API** (15 stars) — focuses on citation network exploration and literature reviews.
- **[AIRA-SemanticScholar](https://github.com/hamid-vakilzadeh/AIRA-SemanticScholar)** (hamid-vakilzadeh) — Academic Graph API with intelligent literature search, built to accompany the academic paper "[The Development of a RAG-Based Artificial Intelligence Research Assistant (AIRA)](https://github.com/hamid-vakilzadeh/AIRA-SemanticScholar)" (Vakilzadeh & Wood, *Journal of Information Systems*, forthcoming).

[Semantic Scholar states it indexes over 200 million academic papers](https://www.semanticscholar.org/about) with AI-generated citation contexts — useful for understanding not just *that* a paper was cited, but *how* it was used.

### Other Academic Search Servers

| Server | Language | License | Notes |
|--------|----------|---------|-------|
| [mcp-for-research](https://github.com/aringadre76/mcp-for-research) | TypeScript | MIT | PubMed/Google Scholar/ArXiv/JSTOR in 5 consolidated tools (14 stars) |
| [Academic-MCP-Server](https://github.com/nanyang12138/Academic-MCP-Server) | — | — | Academic paper search including Sci-Hub (5 stars) |

The mcp-for-research server is notable for **consolidating 4 sources into just 5 tools** — research_search, paper_analysis, citation_manager (with APA/MLA/Chicago formatting), research_preferences, and web_research. Published on npm.

## Scientific Computing

### pathintegral-institute/mcp.science (Computing Hub)

| Server | Stars | Language | License | Servers |
|--------|-------|----------|---------|---------|
| [mcp.science](https://github.com/pathintegral-institute/mcp.science) | 147 | Python | MIT | 12 |

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
| [Wolfram-MCP](https://github.com/paraporoco/Wolfram-MCP) | 13 | Python | MIT | 11 |
| [mcp-server-mathematica](https://github.com/texra-ai/mcp-server-mathematica) | 23 | TypeScript | — | 2 |

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

| Server | Stars | Notes |
|--------|-------|-------|
| [wolframalpha-mcp-server](https://github.com/StoneDot/wolframalpha-mcp-server) | 0 | Wolfram Alpha LLM API — computational queries without local installation |
| [mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha) | 84 | Python — structured knowledge retrieval |
| [mcp-wolfram-alpha](https://github.com/cnosuke/mcp-wolfram-alpha) | 4 | Go — Wolfram Alpha via API |
| [wolframalpha-llm-mcp](https://github.com/Garoth/wolframalpha-llm-mcp) | 55 | Structured knowledge and math solving |
| [MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) | 75 | Chat REPL to Wolfram Alpha |

Five separate Wolfram Alpha MCP implementations — all solving the same problem (connecting AI to Wolfram Alpha's computational knowledge engine) with slight API differences. akalaric's is the most-starred at 84 stars. No local Mathematica license needed — these use the Wolfram Alpha API, which has free and paid tiers.

### calculator-mcp-server

| Server | Stars | Language | License | Notes |
|--------|-------|----------|---------|-------|
| [calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server) | 62 | Python | MIT | Symbolic math, statistics, matrix operations |

For users who don't need Wolfram's full power — provides advanced mathematical calculations including symbolic computation, statistical analysis, and matrix operations without external API dependencies.

## Bioinformatics & Life Sciences

### Augmented-Nature/UniProt-MCP-Server (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server) | 19 | TypeScript | — | 26 |

The **most comprehensive life sciences MCP server** — 26 tools across 7 categories, per [the repository's own README](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server):

- **Core Protein Analysis** (5 tools) — search, detailed info, gene lookup, sequences, features
- **Comparative & Evolutionary Analysis** (4 tools) — comparison, homologs, orthologs, phylogenetics
- **Structure & Function Analysis** (4 tools) — 3D structures, domains, variants, composition
- **Biological Context Analysis** (4 tools) — pathways, interactions, functional classification, localization
- **Batch Processing & Advanced Search** (3 tools) — multi-protein processing, advanced filtering, taxonomic search
- **Literature & Cross-References** (3 tools) — external database links, literature
- **Data Export & Utilities** (3 tools) — output formatting and annotation quality

Supports JSON, FASTA, XML, TSV, GFF, and GenBank output formats. Docker deployment available. This is the kind of deep, domain-specific MCP server that makes AI genuinely useful for bench scientists — asking "what proteins interact with BRCA1 and are localized to the nucleus?" becomes a single tool call.

### Augmented-Nature/PDB-MCP-Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server) | 25 | JavaScript | — | 5 |

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
| [uniprot-mcp-server](https://github.com/TakumiY235/uniprot-mcp-server) (TakumiY235) | Lightweight protein function and sequence retrieval (14 stars, MIT) |
| [bio-mcp-blast](https://github.com/bio-mcp/bio-mcp-blast) | Standalone NCBI BLAST access (blastn, blastp, makeblastdb) |

## Earth & Space Science

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [usgs-quakes-mcp](https://github.com/blake365/usgs-quakes-mcp) | 1 | TypeScript | MIT | 2 |
| [nasa-mcp-server](https://github.com/jezweb/nasa-mcp-server) | 9 | Python | — | 12+ |

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

## What's New (May 2026)

**MCP SDK stdio RCE vulnerability disclosed (April 15, 2026).** [OX Security disclosed a systemic remote code execution vulnerability](https://www.ox.security/blog/the-mother-of-all-ai-supply-chains-critical-systemic-vulnerability-at-the-core-of-the-mcp/) in the MCP SDK's stdio transport layer — an architectural flaw (not a coding bug) affecting all supported language SDKs (Python, TypeScript, Java, Rust) and estimated at 150M+ downloads across 7,000+ publicly exposed servers, with up to 200,000 vulnerable instances. Anthropic confirmed the behavior is by design and declined to change the protocol. The disclosure produced at least twelve downstream CVEs; for example, [LiteLLM disclosed CVE-2026-30623](https://docs.litellm.ai/blog/mcp-stdio-command-injection-april-2026) for the same stdio command-injection pattern, patched in `v1.83.7-stable` (April 21, 2026). Science and research MCP servers that rely on stdio transport (including the arXiv server, paper-search-mcp, and most mcp.science components) are potentially affected. Users running these servers should update to the latest SDK versions and review whether remote access is necessary for their use case. Local-only deployments reduce risk significantly.

**Qubitsok: quantum computing + arXiv server.** [Qubitsok](https://www.pulsemcp.com/servers/qubitsok) combines quantum-computing job search, arXiv paper discovery, and researcher profiles from [qubitsok.com](https://qubitsok.com/) — reflecting growing interest in quantum-computing-aware research assistance. Per its PulseMCP directory listing, the server was released March 12, 2026. Still early-stage but notable as an intersection between research literature and computation.

**mcp.science ecosystem reaches 12+ servers.** The [pathintegral-institute/mcp.science](https://github.com/pathintegral-institute/mcp.science) hub continues to add specialized scientific computing tools under its `uvx mcp-science <name>` unified installation pattern. It remains the most comprehensive single entry point for scientific computing MCP servers.

## The Bottom Line

Science and research MCP servers are **strong for literature search and protein science, but thin everywhere else**.

The **arXiv MCP server at 3,046 stars** proves that researchers want AI-assisted paper discovery. The multi-source aggregators (paper-search-mcp covering 7 databases, Scientific-Papers-MCP covering 6 sources including CORE's 290M+ metadata records and OpenAlex's 477M+ indexed works) mean that literature review workflows are genuinely accelerated. Citation analysis through Semantic Scholar adds context to the raw search results.

**Scientific computing has a solid foundation** through mcp.science's 12-server bundle — particularly the DFT calculator for quantum chemistry and the Materials Project integration. Wolfram Language integration gives agents access to one of the most powerful symbolic computation engines available, though requiring a local license limits accessibility. The five Wolfram Alpha API servers provide a license-free alternative for computational knowledge queries.

**Bioinformatics punches above its weight** — the Augmented Nature team's UniProt (26 tools) and PDB (5 tools with quality validation) servers provide genuine research utility for protein scientists. The sequence-to-structure pipeline is well-covered, and BLAST integration enables homology search.

**Everything else is missing.** The wet lab, the chemistry bench, the genome sequencer, the telescope, the clinical trial, the grant application — none of these have MCP integration. Science is a vast domain, and MCP coverage barely scratches the surface beyond "search papers" and "do math."

**Rating: 3.5 out of 5** — academic paper search is excellent, scientific computing is solid, bioinformatics is surprisingly deep, but the absence of lab infrastructure, chemistry tools, genomics databases, and research workflow integration keeps this from a higher score. The arXiv server's 3,046 stars show strong demand; the ecosystem needs to follow that signal into the lab.

---

*This review covers MCP servers available as of March 2026. Star counts are approximate and change over time. ChatForest researches MCP servers through documentation, GitHub repositories, and community directories — we do not test servers hands-on. For corrections or additions, contact us via chatforest.com.*

*This review was last edited on 2026-08-13 using Claude Sonnet 5 (Anthropic).*

