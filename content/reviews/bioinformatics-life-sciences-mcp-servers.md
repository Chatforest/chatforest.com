---
title: "Bioinformatics & Life Sciences MCP Servers — Genomics, Proteomics, Drug Discovery, Clinical Trials, and Medical Imaging"
date: 2026-03-16T23:00:00+09:00
description: "Bioinformatics and life sciences MCP servers let AI agents query protein databases, run BLAST searches, explore clinical trials, analyze gene expression, and access drug discovery data."
og_description: "Bioinformatics MCP servers: genomoncology/biomcp (241 stars — biomedical queries), JackKuo666/PubMed-MCP-Server (105 stars — literature search), Augmented-Nature/ChEMBL-MCP-Server (78 stars — drug discovery). 40+ servers reviewed. Rating: 4/5."
content_type: "Review"
card_description: "Bioinformatics and life sciences MCP servers for AI-powered genomics, proteomics, drug discovery, clinical research, and medical data access. **Protein and chemical databases have the strongest MCP coverage** — Augmented-Nature maintains a comprehensive suite of servers covering ChEMBL (78 stars, 22 tools for drug discovery and ADMET analysis), PubChem (35 stars, 30 tools for 110M+ chemical compounds), UniProt (18 stars, 26 tools for protein research and comparative genomics), PDB (21 stars, structure search and quality metrics), STRING-db (4 stars, protein interaction networks), and more. Each server wraps a major biological database with specialized tools for AI-assisted research. **Biomedical literature search is well-served** — JackKuo666/PubMed-MCP-Server (105 stars, Python) provides keyword and advanced PubMed search with PDF download and deep paper analysis. cyanheads/pubmed-mcp-server (66 stars, TypeScript) offers production-grade NCBI E-utilities access with multi-format citation generation (APA, MLA, BibTeX, RIS), related article discovery, MeSH term exploration, and Cloudflare Workers deployment. vitorpavinato/ncbi-mcp-server adds analytics and performance monitoring. **Clinical research has strong coverage** — Cicatriiz/healthcare-mcp-public (102 stars, JS) is a multi-source healthcare MCP covering FDA drug info, PubMed, ClinicalTrials.gov, ICD-10, DICOM metadata, medRxiv, NCBI Bookshelf, and a medical calculator — all in one server with caching and Swagger UI. cyanheads/clinicaltrialsgov-mcp-server (59 stars, TypeScript) specializes in ClinicalTrials.gov v2 API with patient eligibility matching, trend analysis, and study comparison across 5,000+ studies. JackKuo666/ClinicalTrials-MCP-Server (15 stars, Python) adds CSV export for bulk data management. **Integrated biomedical platforms stand out** — genomoncology/biomcp (241 stars, Python) provides a single-binary CLI and MCP server querying PubTator3, PubMed, bioRxiv, medRxiv, Europe PMC, ClinicalTrials.gov, and NCI cancer trials with compact markdown output — the most popular standalone biomedical MCP. anthropics/life-sciences (259 stars) is Anthropic's official marketplace connecting Claude to PubMed, BioRender, Synapse.org, Wiley Scholar Gateway, and 10x Genomics Cloud, plus skills for single-cell RNA-seq QC, Nextflow development, and scvi-tools. **Sequence analysis and bioinformatics tools** — the bio-mcp organization maintains focused MCP servers for NCBI BLAST (8 stars, 7 tools with async queue for large searches), BWA sequence alignment, SeqKit FASTA/FASTQ manipulation, AMBER molecular dynamics, and InterPro protein domain analysis. longevity-genie/gget-mcp (27 stars, Python) wraps the gget library's ~15 tools — BLAST, AlphaFold structure prediction, COSMIC mutations, Ensembl gene info, and single-cell analysis — in a single MCP server supporting STDIO, HTTP, and SSE transport. **Systems biology and pathway analysis** — Augmented-Nature/Reactome-MCP-Server (11 stars, JS) provides 8 tools for Reactome pathway data including gene-to-pathway mapping, disease pathways, and molecular participants. Augmented-Nature/OpenTargets-MCP-Server (9 stars, JS) queries gene-drug-disease associations from 20+ databases. Augmented-Nature/BioThings-MCP-Server (5 stars, JS) integrates MyGene.info and MyVariant.info for gene/variant annotation across 32+ data sources with batch processing up to 1,000 items. Augmented-Nature/ProteinAtlas-MCP-Server (3 stars, TypeScript) provides 14 tools for Human Protein Atlas data — tissue/blood/brain expression, subcellular localization, pathology, and cancer prognostic markers. **Drug discovery has a complete pipeline** — ChEMBL MCP provides bioactivity data and target analysis, PubChem MCP covers chemical properties and safety, SureChEMBL-MCP-Server (7 stars, TypeScript, 15 tools) searches chemical patents with SMILES/InChI structure queries and patent family mapping, and OpenTargets connects genes to drugs to diseases. Combined, these enable end-to-end AI-assisted drug discovery from target identification through lead optimization. **Community efforts are expanding** — MCPmed (German research group) has published 10 repos providing MCP wrappers for GEO gene expression, STRING protein interactions, PLSDB plasmid database, UCSC Cell Browser, EMBL-EBI proteins, and PubMed/arXiv/bioRxiv literature — plus a cookiecutter template and LLM tracing breadcrumbs. Their work is backed by a published paper (arXiv:2507.08055) calling for community-wide adoption of MCP-enabled bioinformatics services. **Healthcare and EHR access is emerging** — jmandel/health-record-mcp uses SMART on FHIR for secure EHR data access. wso2/fhir-mcp-server exposes any FHIR server as an MCP server. xSoVx/fhir-mcp provides PHI protection, audit logging, and HL7 terminology services. AWS HealthLake MCP Server offers 11 tools for FHIR resource management. These represent early healthcare interoperability infrastructure. **Gaps remain** — no AlphaFold MCP exists for direct structure prediction, no Galaxy workflow MCP wrapper for established bioinformatics pipelines, no KEGG pathway MCP, limited medical imaging (only DICOM metadata, no radiology AI), no single-cell analysis pipeline MCP beyond basic QC, and no EHR-integrated clinical decision support MCP. The Augmented-Nature ecosystem is impressive but most repos have under 25 stars, suggesting early adoption."
last_refreshed: 2026-03-16
---

Bioinformatics and life sciences MCP servers let AI agents query protein databases, run sequence analysis, explore clinical trials, access drug discovery data, and interact with medical records. Instead of manually navigating database web interfaces or writing API scripts, AI assistants can directly search biological databases, analyze sequences, and synthesize research findings through natural language. Part of our **[Science & Research MCP category](/categories/science-research/)**.

This review covers **bioinformatics and life sciences MCP servers** — protein/chemical databases, biomedical literature, clinical research, sequence analysis, systems biology, drug discovery, and healthcare interoperability. For related servers, see our [Scientific Research review](/reviews/science-research-mcp-servers/), [Data Science & Machine Learning review](/reviews/ai-ml-model-serving-mcp-servers/), and [Digital Twins & Simulation review](/reviews/digital-twins-3d-simulation-mcp-servers/).

The headline findings: **Protein and chemical databases have the strongest MCP coverage** — Augmented-Nature maintains 10+ servers wrapping every major biological database. **Integrated platforms lead adoption** — genomoncology/biomcp (241 stars) and Anthropic's official life-sciences marketplace (259 stars) provide one-stop biomedical querying. **Literature search is mature** — multiple PubMed MCPs exist with 60–105 stars. **Drug discovery has end-to-end coverage** — from target identification through patent search. **Clinical trials are well-served** with patient matching and trend analysis. **Gaps remain in medical imaging, AlphaFold, and Galaxy workflows.**

---

## Integrated Biomedical Platforms

### genomoncology/biomcp — Single-Binary Biomedical MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [biomcp](https://github.com/genomoncology/biomcp) | 241 | Python | MIT | 12 entities |

**The most popular standalone biomedical MCP server** — a single-binary CLI and MCP server querying multiple authoritative data sources:

- **PubTator3 / PubMed** — peer-reviewed biomedical literature with entity annotations
- **bioRxiv / medRxiv** — preprint servers for biology and health sciences
- **Europe PMC** — open science platform including preprints
- **ClinicalTrials.gov** — clinical trial registry and results database
- **NCI Clinical Trials Search API** — curated cancer trials
- **Genomic variants** — variant-level data for precision oncology
- **Compact markdown output** — optimized for LLM token efficiency
- **MCPHub certified** — follows MCP best practices

One command grammar, 12 entities across 15+ data sources. The best choice if you want a single server covering the breadth of biomedical research.

### anthropics/life-sciences — Official Anthropic Marketplace

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [life-sciences](https://github.com/anthropics/life-sciences) | 259 | Python | — | Marketplace |

**Anthropic's official life sciences launch for Claude Code** — a marketplace registry providing remote MCP servers and skills:

- **Remote MCP servers** — PubMed, BioRender, Synapse.org, Wiley Scholar Gateway
- **Local MCP server** — 10x Genomics Cloud
- **Skills** — Single-Cell RNA-seq QC (scverse best practices, MAD-based filtering), Instrument Data to Allotrope, Nextflow Development, scvi-tools
- **Marketplace format** — installable through Claude Code Marketplace

Not a standalone MCP server but a curated collection of life sciences tools. Significant because Anthropic is directly investing in bioinformatics MCP infrastructure.

---

## Protein & Chemical Databases

### Augmented-Nature/ChEMBL-MCP-Server — Drug Discovery Research

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server) | 78 | TypeScript | MIT | 22 |

**The most popular protein/chemical database MCP** — 22 specialized tools for drug discovery via ChEMBL's REST API:

- **Chemical search** — compound lookup, similarity search, substructure queries
- **Target analysis** — protein target information and bioactivity data
- **ADMET properties** — absorption, distribution, metabolism, excretion, toxicity
- **Drug development** — clinical candidate tracking, mechanism of action
- **Cross-database integration** — links to PubChem, DrugBank, PDB

The go-to server for AI-assisted drug discovery workflows.

### Augmented-Nature/PubChem-MCP-Server — 110M+ Chemical Compounds

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server) | 35 | TypeScript | MIT | 30 |

**Most comprehensive chemical database MCP** — 30 tools covering PubChem's 110M+ compounds:

- **Chemical search** — name, CID, SMILES, InChI, similarity search
- **Structure analysis** — 2D/3D coordinates, molecular properties
- **Bioassay data** — bioactivity profiles across assays
- **Safety/toxicity** — GHS classifications, hazard data
- **Batch processing** — up to 200 compounds per request
- **ADMET predictions** — pharmacokinetic property estimation

### Augmented-Nature/UniProt-MCP-Server — Protein Research

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [UniProt-MCP-Server](https://github.com/Augmented-Nature/Augmented-Nature-UniProt-MCP-Server) | 18 | TypeScript | MIT | 26 |

**26 specialized bioinformatics tools** for protein research through UniProt's REST API:

- **Core protein analysis** — search, retrieve, characterize proteins
- **Comparative/evolutionary analysis** — cross-species comparisons
- **Structure/function** — InterPro, Pfam, SMART domain annotations
- **Biological context** — pathways, interactions, disease associations
- **Batch processing** — bulk protein data retrieval
- **Data export** — structured output for downstream analysis

### Augmented-Nature/PDB-MCP-Server — Protein Data Bank

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server) | 21 | JavaScript | MIT | 5 |

**Access the worldwide repository of 3D protein structures** — search, retrieve, and download structures from the RCSB Protein Data Bank:

- **Structure search** — query by keyword, organism, resolution
- **Detail retrieval** — full structure information and metadata
- **Multiple formats** — PDB, mmCIF, mmTF, XML
- **UniProt integration** — search structures by UniProt accession
- **Quality metrics** — resolution, R-factor, validation data

### Augmented-Nature/STRING-db-MCP-Server — Protein Interaction Networks

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [STRING-db-MCP-Server](https://github.com/Augmented-Nature/STRING-db-MCP-Server) | 4 | JavaScript | MIT | 6 |

**Protein-protein interaction networks** — query the STRING database covering 5,000+ organisms:

- **Interaction networks** — known and predicted protein-protein interactions
- **Functional enrichment** — GO terms, KEGG pathways, Pfam domains
- **Comparative genomics** — find homologs across species
- **Protein annotations** — functional descriptions and classifications

---

## Biomedical Literature

### JackKuo666/PubMed-MCP-Server — PubMed Search with Deep Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PubMed-MCP-Server](https://github.com/JackKuo666/PubMed-MCP-Server) | 105 | Python | MIT | 5 |

**Most popular PubMed MCP server** — keyword and advanced search with document retrieval:

- **Keyword search** — simple PubMed queries
- **Advanced search** — field-specific queries (author, journal, date range)
- **Article metadata** — full bibliographic information
- **PDF download** — retrieve full-text PDFs when available
- **Deep paper analysis** — AI-assisted summary and analysis of papers
- **Smithery integration** — marketplace deployment

### cyanheads/pubmed-mcp-server — Production-Grade NCBI E-utilities

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server) | 66 | TypeScript | MIT | 7 |

**Production-grade biomedical literature server** — comprehensive NCBI E-utilities integration:

- **Multi-format citations** — APA, MLA, BibTeX, RIS
- **Batch metadata** — retrieve multiple articles at once
- **Full-text retrieval** — access complete article content
- **Related articles** — discover connected research
- **MeSH exploration** — navigate Medical Subject Headings hierarchy
- **Spell-check** — correct biomedical query terms
- **Cloudflare Workers** — edge deployment option
- **OpenTelemetry** — built-in tracing and monitoring

### vitorpavinato/ncbi-mcp-server — NCBI with Analytics

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ncbi-mcp-server](https://github.com/vitorpavinato/ncbi-mcp-server) | 8 | Python | — | 7 |

**NCBI/PubMed MCP for life sciences researchers** — 35M+ articles with analytics:

- **Search and retrieval** — PubMed search with article details
- **MeSH terms** — medical subject heading queries
- **Related articles** — discover connected research
- **Analytics** — search performance monitoring and summaries
- **Docker support** — containerized deployment

---

## Clinical Research & Healthcare

### Cicatriiz/healthcare-mcp-public — Multi-Source Healthcare Server

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public) | 102 | JavaScript | — | 9 |

**The most comprehensive healthcare MCP** — 9 tools spanning multiple authoritative medical sources:

- **FDA Drug Info** — drug labels, interactions, adverse events
- **PubMed Research** — biomedical literature search
- **Clinical Trials** — ClinicalTrials.gov search and retrieval
- **ICD-10** — medical terminology and coding
- **DICOM Metadata** — medical imaging metadata access
- **medRxiv** — health sciences preprints
- **NCBI Bookshelf** — open-access medical textbooks
- **Medical Calculator** — clinical calculations
- **Health Topics** — consumer health information

All in one server with built-in caching, HTTP/SSE web interface, and Swagger UI documentation. DXT extension for one-click install.

### cyanheads/clinicaltrialsgov-mcp-server — ClinicalTrials.gov v2 API

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server) | 59 | TypeScript | MIT | 7 |

**Specialized clinical trials server** — full ClinicalTrials.gov v2 API access:

- **Study search** — query across 5,000+ studies with filters
- **Study details** — complete protocol and results data
- **Patient eligibility matching** — match patients to eligible trials
- **Trend analysis** — research trends across trial data
- **Study comparison** — side-by-side trial analysis
- **Field values** — enumerate available filter options
- **Cloudflare Workers** — edge deployment

### JackKuo666/ClinicalTrials-MCP-Server — Clinical Trials with CSV Export

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ClinicalTrials-MCP-Server](https://github.com/JackKuo666/ClinicalTrials-MCP-Server) | 15 | Python | MIT | 7 |

**ClinicalTrials.gov with data management** — search plus CSV export for bulk analysis:

- **Search and save** — query trials and export results to CSV
- **Full study details** — complete study protocol retrieval
- **Statistics** — aggregate trial statistics
- **Bulk operations** — save multiple studies at once
- **CSV management** — load, list, and manage exported datasets

### Healthcare Data Access — FHIR and EHR

Several MCP servers are emerging for electronic health records access:

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [health-record-mcp](https://github.com/jmandel/health-record-mcp) | — | — | SMART on FHIR EHR access |
| [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) | — | — | Expose any FHIR server as MCP |
| [xSoVx/fhir-mcp](https://github.com/xSoVx/fhir-mcp) | — | — | PHI protection, audit logging, HL7 |
| [the-momentum/fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server) | — | — | Full CRUD for FHIR resources |

Early-stage but important — these represent the foundation for AI-assisted clinical workflows with proper security, PHI protection, and healthcare interoperability standards.

---

## Sequence Analysis & Bioinformatics Tools

### bio-mcp Organization — Focused Bioinformatics Tools

The [bio-mcp](https://github.com/bio-mcp) organization maintains specialized MCP servers for core bioinformatics tools:

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [bio-mcp-blast](https://github.com/bio-mcp/bio-mcp-blast) | 8 | Python | NCBI BLAST sequence similarity |
| bio-mcp-bwa | — | — | BWA sequence alignment |
| bio-mcp-seqkit | — | — | SeqKit FASTA/FASTQ manipulation |
| bio-mcp-amber | — | — | AMBER molecular dynamics |
| bio-mcp-interpro | — | — | InterPro protein domains |
| bio-mcp-evo2 | — | — | Evo2 DNA language model |

**bio-mcp-blast** is the standout — 7 tools for NCBI BLAST with async queue for large-scale searches:

- **blastn / blastp** — nucleotide and protein sequence search
- **makeblastdb** — create custom BLAST databases
- **Async mode** — queue jobs for long-running searches
- **Job management** — check status and retrieve results
- **Docker deployment** — containerized BLAST+ installation
- **Multiple output formats** — tabular, XML, JSON

### longevity-genie/gget-mcp — Multi-Tool Bioinformatics Wrapper

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [gget-mcp](https://github.com/longevity-genie/gget-mcp) | 27 | Python | — | ~15 |

**Wraps the gget bioinformatics library** for comprehensive genomics queries:

- **BLAST** — sequence similarity search via NCBI BLAST
- **AlphaFold** — protein structure prediction
- **COSMIC** — cancer mutation analysis
- **Ensembl** — gene info, search, and sequence retrieval
- **Expression analysis** — gene expression data from ARCHS4
- **Single-cell** — cell type annotations via CellXGene
- **Multiple transports** — STDIO, HTTP, SSE

The best single-server option for broad bioinformatics capability — covers genomics, proteomics, and cancer research in one package.

---

## Systems Biology & Pathway Analysis

### Augmented-Nature Pathway Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [Reactome-MCP-Server](https://github.com/Augmented-Nature/Reactome-MCP-Server) | 11 | JavaScript | 8 | Biological pathways |
| [OpenTargets-MCP-Server](https://github.com/Augmented-Nature/OpenTargets-MCP-Server) | 9 | JavaScript | 6 | Gene-drug-disease associations |
| [BioThings-MCP-Server](https://github.com/Augmented-Nature/BioThings-MCP-Server) | 5 | JavaScript | 16 | Gene/variant annotation |
| [ProteinAtlas-MCP-Server](https://github.com/Augmented-Nature/ProteinAtlas-MCP-Server) | 3 | TypeScript | 14 | Protein expression data |

**Reactome MCP** provides pathway search, gene-to-pathway mapping, disease pathways, molecular participants, and protein interactions via Reactome Content Service API.

**OpenTargets MCP** queries gene-drug-disease associations from 20+ integrated databases — excellent for target validation and drug repurposing research.

**BioThings MCP** integrates MyGene.info and MyVariant.info for gene/variant annotation across 32+ data sources with batch processing up to 1,000 items — useful for annotating variant lists from sequencing studies.

**ProteinAtlas MCP** provides 14 tools for Human Protein Atlas data including tissue/blood/brain expression, subcellular localization, pathology data, cancer prognostic markers, and antibody validation information.

---

## Drug Discovery Pipeline

### End-to-End Drug Discovery with MCP Servers

Combining multiple Augmented-Nature servers creates a complete AI-assisted drug discovery pipeline:

| Stage | Server | What it does |
|-------|--------|-------------|
| Target identification | OpenTargets MCP | Gene-disease associations from 20+ databases |
| Target validation | Reactome MCP + BioThings MCP | Pathway context, variant annotation |
| Lead discovery | ChEMBL MCP | Bioactivity data, compound search |
| Chemical optimization | PubChem MCP | Properties, ADMET, safety data |
| Structural biology | PDB MCP + UniProt MCP | Protein structures, binding sites |
| Patent landscape | SureChEMBL MCP | Chemical patent search, family mapping |
| Literature evidence | PubMed MCP + BioMCP | Published research, preprints |
| Clinical development | ClinicalTrials MCP | Existing trial data, competitor analysis |

### Augmented-Nature/SureChEMBL-MCP-Server — Chemical Patent Intelligence

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [SureChEMBL-MCP-Server](https://github.com/Augmented-Nature/SureChEMBL-MCP-Server) | 7 | TypeScript | MIT | 15 |

**Chemical patent database access** — 15 tools for patent intelligence:

- **Patent/document search** — query chemical patents by keyword, structure, date
- **SMILES/InChI search** — structure-based patent lookup
- **Patent family mapping** — trace patent families across jurisdictions
- **Bulk export** — CSV and XML data export
- **Advanced analysis** — patent landscape visualization data

---

## Community Initiatives

### MCPmed — Academic Bioinformatics MCP Ecosystem

The [MCPmed](https://github.com/MCPmed) organization (Germany) is building an academic ecosystem of bioinformatics MCP servers backed by a published paper (arXiv:2507.08055):

| Server | Stars | Focus |
|--------|-------|-------|
| GEOmcp | 8 | Gene Expression Omnibus via NCBI E-Utils |
| STRINGmcp | 3 | STRING protein interactions |
| PLSDBmcp | 2 | PLSDB plasmid database |
| EMBL-EBI-Protein-mcp | 2 | EMBL-EBI protein database |
| UCSCCBmcp | 1 | UCSC Cell Browser |
| paperscraperMCP | 1 | PubMed/arXiv/bioRxiv scraping |
| Cookiecutter-MCPmed | 5 | Project template for new servers |
| breadcrumbs/breadcrumbsMCP | 1 | LLM tracing for reproducibility |

MCPmed's vision is systematic MCP-enabling of existing bioinformatics web services, with breadcrumbs for reproducibility and a cookiecutter template for creating new servers. Early-stage but conceptually important for the field.

### BioinfoMCP — Automated Tool Conversion

The BioinfoMCP platform automatically converts existing bioinformatics tools into MCP servers using LLMs — achieving a 94.7% success rate across 38 tools in benchmark tests. This could dramatically accelerate MCP adoption across the thousands of existing bioinformatics tools.

---

## What's Missing

Despite strong coverage, notable gaps remain:

- **AlphaFold** — no direct MCP server for AlphaFold structure prediction (gget-mcp wraps it indirectly)
- **Galaxy workflows** — no MCP wrapper for the Galaxy bioinformatics platform
- **Single-cell pipelines** — no comprehensive scRNA-seq pipeline MCP (only QC skills via Anthropic marketplace)
- **KEGG** — no MCP server for this widely-used pathway database
- **Medical imaging AI** — DICOM metadata access exists, but no radiology AI or pathology MCP servers
- **Nextflow/Snakemake** — no workflow engine MCP for orchestrating bioinformatics pipelines
- **EHR clinical decision support** — FHIR access exists but no clinical reasoning MCP
- **Multi-omics integration** — no MCP server combining genomics, transcriptomics, proteomics, and metabolomics data

## The Bottom Line

Bioinformatics and life sciences is one of the most active and well-organized MCP server categories. The Augmented-Nature ecosystem alone covers 10+ major biological databases. Combined with BioMCP's unified interface, robust PubMed and clinical trials servers, and an emerging FHIR/EHR infrastructure, researchers can build sophisticated AI-assisted biomedical workflows today. The drug discovery pipeline — from target identification through patent search — is particularly complete. The main gaps are in medical imaging, workflow orchestration, and multi-omics integration. **Rating: 4/5.**

*This review was last edited on 2026-03-16 using Claude Opus 4.6 (Anthropic).*
