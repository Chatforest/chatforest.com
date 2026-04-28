---
title: "Bioinformatics & Life Sciences MCP Servers — Genomics, Proteomics, Drug Discovery, Clinical Trials, and Medical Imaging"
date: 2026-03-16T23:00:00+09:00
description: "Bioinformatics and life sciences MCP servers let AI agents query protein databases, run BLAST searches, explore clinical trials, analyze gene expression, and access drug discovery data."
og_description: "Bioinformatics MCP servers: genomoncology/biomcp (497 stars — biomedical queries), anthropics/life-sciences (321 stars — official marketplace), cyanheads/pubmed-mcp-server (88 stars — literature search), Augmented-Nature/ChEMBL-MCP-Server (83 stars — drug discovery). NEW: AlphaFold MCP (33 stars, 25+ tools — fills gap), KEGG MCP (9 stars, 30 tools — fills gap), LangCare FHIR (31 stars, enterprise-grade). 55+ servers reviewed. Rating: 4.5/5."
content_type: "Review"
card_description: "Bioinformatics and life sciences MCP servers for AI-powered genomics, proteomics, drug discovery, clinical research, and medical data access. **Integrated biomedical platforms lead** — genomoncology/biomcp surged 106% to 497 stars (from 241), now 13 entities across 15+ data sources with 1,152 commits. anthropics/life-sciences grew to 321 stars (from 259), added Scientific Problem Selection skill, and Anthropic acquired Coefficient Bio for $400M (April 2026) to build specialized drug discovery tools. **Two major gaps filled** — Augmented-Nature/AlphaFold-MCP-Server (33 stars, TypeScript, MIT, 25+ tools) provides structure retrieval, confidence scoring, batch processing, comparative analysis, and PyMOL/ChimeraX export. Augmented-Nature/KEGG-MCP-Server (9 stars, JS, MIT, 30 tools) covers pathways, genes, compounds, reactions, enzymes, diseases, and drugs. Both were identified as key gaps in our March review. **Protein and chemical databases have the strongest MCP coverage** — Augmented-Nature now maintains 15+ servers including ChEMBL (83 stars, 22 tools), PubChem (36 stars, 30 tools), PDB (24 stars), UniProt (18 stars, 26 tools), NCBI-Datasets (13 stars, 31 tools — NEW), Reactome (12 stars), OpenTargets (10 stars), BioOntology (9 stars, 1,200+ ontologies — NEW), KEGG (9 stars, 30 tools — NEW), GeneOntology (8 stars — NEW), STRING-db (4 stars), ProteinAtlas (3 stars, 14 tools), Ensembl (2 stars, 25 tools — NEW). **Biomedical literature search surged** — cyanheads/pubmed-mcp-server grew 33% to 88 stars (from 66), now 9 tools (from 7), v2.6.4, added Streamable HTTP transport and Unpaywall fulltext fallback. JackKuo666/PubMed-MCP-Server stable at 108 stars. **Clinical research growing** — Cicatriiz/healthcare-mcp-public grew to 111 stars (from 102). cyanheads/clinicaltrialsgov-mcp-server grew to 67 stars (from 59), v2.4.2, 263 commits. **Medical imaging breakthrough** — Owkin Pathology Explorer launched with Anthropic's Claude for Healthcare (Jan 2026), the first pathology AI agent via MCP trained on data from 800+ hospitals. fluxinc/dicom-mcp-server (3 stars, Python) adds PACS/VNA DICOM connectivity. **Healthcare interoperability maturing** — NEW langcare/langcare-mcp-fhir (31 stars, Go, MIT) provides enterprise-grade FHIR with 40+ clinical skills, supports EPIC/Cerner/OpenEMR/GCP Healthcare API, OAuth2/mTLS security, HIPAA audit logging, and interactive MCP Apps. **Genomics expanding** — NEW longevity-genie/alphagenome-mcp (2 stars, Python, Apache 2.0) wraps DeepMind's AlphaGenome API for regulatory variant effect predictions. NEW Augmented-Nature/Ensembl-MCP-Server (2 stars, TypeScript, 25 tools) provides Ensembl REST API access for genomic data and comparative genomics. **Community validated** — MCPmed paper published in Briefings in Bioinformatics (Jan 2026, Oxford Academic), elevating from preprint to peer-reviewed journal. snap-stanford/Biomni (3,000 stars, Apache 2.0) is a Stanford biomedical AI agent platform that uses MCP for tool integration. **Remaining gaps** — no Galaxy workflow MCP, no comprehensive single-cell pipeline MCP beyond QC skills, limited multi-omics integration, Nextflow/Snakemake workflow orchestration still absent."
last_refreshed: 2026-04-28
---

Bioinformatics and life sciences MCP servers let AI agents query protein databases, run sequence analysis, explore clinical trials, access drug discovery data, and interact with medical records. Instead of manually navigating database web interfaces or writing API scripts, AI assistants can directly search biological databases, analyze sequences, and synthesize research findings through natural language. Part of our **[Science & Research MCP category](/categories/science-research/)**.

This review covers **bioinformatics and life sciences MCP servers** — protein/chemical databases, biomedical literature, clinical research, sequence analysis, systems biology, drug discovery, and healthcare interoperability. For related servers, see our [Scientific Research review](/reviews/science-research-mcp-servers/), [Data Science & Machine Learning review](/reviews/ai-ml-model-serving-mcp-servers/), and [Digital Twins & Simulation review](/reviews/digital-twins-3d-simulation-mcp-servers/).

The headline findings: **Integrated platforms surging** — genomoncology/biomcp doubled to 497 stars with 13 entities across 15+ data sources. **Anthropic is going all-in on life sciences** — life-sciences marketplace at 321 stars, plus $400M acquisition of Coefficient Bio for drug discovery (April 2026), plus Owkin Pathology Explorer launched as first pathology AI via MCP. **Two major gaps filled** — AlphaFold MCP (33 stars, 25+ tools) and KEGG MCP (9 stars, 30 tools) now exist, both from Augmented-Nature. **Protein and chemical databases have the strongest MCP coverage** — Augmented-Nature now maintains 15+ servers. **Literature search is mature and growing** — cyanheads/pubmed surged 33% to 88 stars with Streamable HTTP. **Healthcare interoperability maturing** — LangCare FHIR (31 stars, Go) brings enterprise-grade EHR access with 40+ clinical skills. **Drug discovery has end-to-end coverage** from target identification through patent search. **Remaining gaps: Galaxy workflows, comprehensive single-cell pipelines, multi-omics integration.**

---

## Integrated Biomedical Platforms

### genomoncology/biomcp — Single-Binary Biomedical MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [biomcp](https://github.com/genomoncology/biomcp) | 497 | Python | MIT | 13 entities |

**The most popular standalone biomedical MCP server — surged 106% from 241 to 497 stars** — a single-binary CLI and MCP server querying multiple authoritative data sources:

- **PubTator3 / PubMed** — peer-reviewed biomedical literature with entity annotations
- **bioRxiv / medRxiv** — preprint servers for biology and health sciences
- **Europe PMC** — open science platform including preprints
- **ClinicalTrials.gov** — clinical trial registry and results database
- **NCI Clinical Trials Search API** — curated cancer trials
- **Genomic variants** — variant-level data for precision oncology
- **Cross-entity helpers** — pivot between related data types
- **Local study analytics** — cBioPortal-style dataset analysis
- **Compact markdown output** — optimized for LLM token efficiency
- **1,152 commits** — rapid iteration cadence

One command grammar, 13 entities across 15+ data sources. The best choice if you want a single server covering the breadth of biomedical research.

### anthropics/life-sciences — Official Anthropic Marketplace

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [life-sciences](https://github.com/anthropics/life-sciences) | 321 | Python | — | Marketplace |

**Anthropic's official life sciences marketplace — grew 24% from 259 to 321 stars** — a marketplace registry providing remote MCP servers and skills:

- **Remote MCP servers** — PubMed, BioRender, Synapse.org, Wiley Scholar Gateway
- **Local MCP server** — 10x Genomics Cloud
- **Skills** — Single-Cell RNA-seq QC, Instrument Data to Allotrope, Nextflow Development, scvi-tools, Scientific Problem Selection (NEW)
- **Marketplace format** — installable through Claude Code Marketplace
- **v1.1.1** (January 2026) — Benchling removed (incompatible with plugin system)

Anthropic is going all-in on life sciences: acquired Coefficient Bio for $400M (April 3, 2026) to build specialized drug discovery and clinical workflow tools. The Coefficient Bio team joined Anthropic's Healthcare & Life Sciences group. Additionally, Owkin's Pathology Explorer launched with Claude for HCLS (January 2026) — the first pathology AI agent via MCP, trained on histopathology data from 800+ hospitals across 104 healthcare centers.

---

## Protein & Chemical Databases

### Augmented-Nature/ChEMBL-MCP-Server — Drug Discovery Research

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [ChEMBL-MCP-Server](https://github.com/Augmented-Nature/ChEMBL-MCP-Server) | 83 | TypeScript | MIT | 22 |

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
| [PubChem-MCP-Server](https://github.com/Augmented-Nature/PubChem-MCP-Server) | 36 | TypeScript | MIT | 30 |

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
| [PDB-MCP-Server](https://github.com/Augmented-Nature/PDB-MCP-Server) | 24 | JavaScript | MIT | 5 |

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

### Augmented-Nature/AlphaFold-MCP-Server — Protein Structure Prediction (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [AlphaFold-MCP-Server](https://github.com/Augmented-Nature/AlphaFold-MCP-Server) | 33 | TypeScript | MIT | 25+ |

**Fills the biggest gap from our March review** — comprehensive access to the AlphaFold Protein Structure Database:

- **Structure retrieval** — AlphaFold predictions by UniProt ID in PDB, CIF, BCIF, JSON formats
- **Confidence analysis** — per-residue pLDDT scores with threshold filtering and region-specific quality assessment
- **Batch processing** — analyze up to 50 proteins simultaneously
- **Comparative analysis** — side-by-side structure comparison across protein sets
- **Visualization export** — PyMOL and ChimeraX scripts with confidence-based coloring
- **Coverage tools** — organism and proteome coverage statistics

AlphaFold MCP was the most requested missing server in bioinformatics. Its arrival means the drug discovery pipeline is now truly end-to-end — from target identification through 3D structure analysis.

---

## Biomedical Literature

### JackKuo666/PubMed-MCP-Server — PubMed Search with Deep Analysis

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [PubMed-MCP-Server](https://github.com/JackKuo666/PubMed-MCP-Server) | 108 | Python | MIT | 5 |

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
| [pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server) | 88 | TypeScript | Apache 2.0 | 9 |

**Production-grade biomedical literature server — surged 33% from 66 to 88 stars** — comprehensive NCBI E-utilities integration:

- **Multi-format citations** — APA, MLA, BibTeX, RIS
- **Batch metadata** — retrieve multiple articles at once
- **Full-text retrieval** — with Unpaywall fallback for open-access copies (NEW)
- **Related articles** — discover connected research
- **MeSH exploration** — navigate Medical Subject Headings hierarchy
- **Spell-check** — correct biomedical query terms
- **Streamable HTTP transport** — STDIO or hosted endpoint (NEW)
- **v2.6.4** — 244 commits, 9 tools (was 7), built on @cyanheads/mcp-ts-core

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
| [healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public) | 111 | JavaScript | — | 9 |

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
| [clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server) | 67 | TypeScript | MIT | 7 |

**Specialized clinical trials server — grew to 67 stars (from 59)** — full ClinicalTrials.gov v2 API access:

- **Study search** — full-text and field-specific queries (condition, intervention, sponsor, location)
- **Study details** — complete protocol and results data
- **Patient eligibility matching** — match patients to eligible trials
- **Summary mode** — reduces study result payloads from ~200KB to ~5KB (NEW)
- **Study comparison** — side-by-side trial analysis
- **v2.4.2** — 263 commits, STDIO or Streamable HTTP transport

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

Healthcare interoperability is maturing rapidly, led by a new enterprise-grade entrant:

### langcare/langcare-mcp-fhir — Enterprise-Grade FHIR (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [langcare-mcp-fhir](https://github.com/langcare/langcare-mcp-fhir) | 31 | Go | MIT | 40+ clinical skills |

**The most comprehensive healthcare MCP server to date** — enterprise-grade FHIR access:

- **Generic FHIR operations** — read, search, create, update across any FHIR R4 server
- **40+ clinical skills** — medication management, labs, care coordination, population health
- **Multi-EHR support** — EPIC, Cerner, OpenEMR, GCP Healthcare API
- **Security** — OAuth2, mTLS, HIPAA audit logging
- **Interactive MCP Apps** — React-based UIs embedded in Claude Desktop
- **Voice agent** — Pipecat integration for voice-driven clinical workflows

A significant step beyond the early FHIR servers — this is production-ready clinical infrastructure.

Other FHIR MCP servers continue to mature:

| Server | Stars | Language | Focus |
|--------|-------|----------|-------|
| [health-record-mcp](https://github.com/jmandel/health-record-mcp) | — | — | SMART on FHIR EHR access |
| [wso2/fhir-mcp-server](https://github.com/wso2/fhir-mcp-server) | — | — | Expose any FHIR server as MCP |
| [xSoVx/fhir-mcp](https://github.com/xSoVx/fhir-mcp) | — | — | PHI protection, audit logging, HL7 |
| [the-momentum/fhir-mcp-server](https://github.com/the-momentum/fhir-mcp-server) | — | — | Full CRUD for FHIR resources |
| [azure-fhir-mcp-server](https://github.com/erikhoward/azure-fhir-mcp-server) | — | — | Azure AHDS FHIR (NEW) |

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

### Augmented-Nature/NCBI-Datasets-MCP-Server — Genomic Data (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [NCBI-Datasets-MCP-Server](https://github.com/Augmented-Nature/NCBI-Datasets-MCP-Server) | 13 | TypeScript | MIT | 31 |

**Comprehensive NCBI Datasets API access** — 31 tools across nine categories:

- **Genome assemblies** — search, metadata, annotations, quality metrics
- **Gene data** — gene search, retrieval, ortholog identification
- **Taxonomy** — organism classification and lineage queries
- **Protein sequences** — retrieval and analysis
- **Viral genomes** — specialized viral data access
- **Rate limiting and caching** — 10 req/sec authenticated, 3 req/sec unauthenticated

### Augmented-Nature/Ensembl-MCP-Server — Genomic Data (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Ensembl-MCP-Server](https://github.com/Augmented-Nature/Ensembl-MCP-Server) | 2 | TypeScript | — | 25 |

**Ensembl REST API access** — 25 tools covering gene analysis, sequence operations, comparative genomics, variant data, regulatory features, and cross-references across 15+ organism groups.

### longevity-genie/alphagenome-mcp — DeepMind AlphaGenome (NEW)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [alphagenome-mcp](https://github.com/longevity-genie/alphagenome-mcp) | 2 | Python | Apache 2.0 | 3 |

**Google DeepMind's AlphaGenome API via MCP** — sequence analysis for DNA up to 1MB, genomic region predictions (gene expression, chromatin accessibility, 3D interactions), and variant assessment comparing reference/alternate sequences across 11 prediction types.

---

## Systems Biology & Pathway Analysis

### Augmented-Nature Pathway & Ontology Servers

| Server | Stars | Language | Tools | Focus |
|--------|-------|----------|-------|-------|
| [Reactome-MCP-Server](https://github.com/Augmented-Nature/Reactome-MCP-Server) | 12 | JavaScript | 8 | Biological pathways |
| [OpenTargets-MCP-Server](https://github.com/Augmented-Nature/OpenTargets-MCP-Server) | 10 | JavaScript | 6 | Gene-drug-disease associations |
| [KEGG-MCP-Server](https://github.com/Augmented-Nature/KEGG-MCP-Server) | 9 | JavaScript | 30 | KEGG pathways (NEW) |
| [BioOntology-MCP-Server](https://github.com/Augmented-Nature/BioOntology-MCP-Server) | 9 | JavaScript | — | 1,200+ biological ontologies (NEW) |
| [GeneOntology-MCP-Server](https://github.com/Augmented-Nature/GeneOntology-MCP-Server) | 8 | JavaScript | — | Gene Ontology terms & annotations (NEW) |
| [BioThings-MCP-Server](https://github.com/Augmented-Nature/BioThings-MCP-Server) | 5 | JavaScript | 16 | Gene/variant annotation |
| [ProteinAtlas-MCP-Server](https://github.com/Augmented-Nature/ProteinAtlas-MCP-Server) | 3 | TypeScript | 14 | Protein expression data |

**KEGG MCP (NEW)** fills our second major gap — 30 tools plus 8 resource templates covering pathways, genes, compounds, reactions, enzymes, diseases, drugs, modules, glycans, and BRITE hierarchies. The most-requested pathway database finally has MCP coverage.

**BioOntology MCP (NEW)** provides access to 1,200+ biological ontologies via the BioPortal API — medical/clinical (NCIT, DOID, HP, MESH), biological/chemical (GO, UBERON, CHEBI), plus specialized ontologies. Supports term search, text annotation, batch processing, and ontology metrics.

**GeneOntology MCP (NEW)** provides Gene Ontology term search, hierarchy navigation, gene annotation access, and GO identifier validation via QuickGO API.

**Reactome MCP** provides pathway search, gene-to-pathway mapping, disease pathways, molecular participants, and protein interactions via Reactome Content Service API.

**OpenTargets MCP** queries gene-drug-disease associations from 20+ integrated databases — excellent for target validation and drug repurposing research.

**BioThings MCP** integrates MyGene.info and MyVariant.info for gene/variant annotation across 32+ data sources with batch processing up to 1,000 items.

**ProteinAtlas MCP** provides 14 tools for Human Protein Atlas data including tissue/blood/brain expression, subcellular localization, pathology data, cancer prognostic markers, and antibody validation information.

---

## Drug Discovery Pipeline

### End-to-End Drug Discovery with MCP Servers

Combining multiple Augmented-Nature servers creates a complete AI-assisted drug discovery pipeline:

| Stage | Server | What it does |
|-------|--------|-------------|
| Target identification | OpenTargets MCP | Gene-disease associations from 20+ databases |
| Target validation | Reactome MCP + KEGG MCP (NEW) | Pathway context, metabolic networks |
| Lead discovery | ChEMBL MCP | Bioactivity data, compound search |
| Chemical optimization | PubChem MCP | Properties, ADMET, safety data |
| Structural biology | AlphaFold MCP (NEW) + PDB MCP + UniProt MCP | Structure prediction, binding sites |
| Variant annotation | BioThings MCP + GeneOntology MCP (NEW) | Gene/variant functional context |
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

MCPmed's vision is systematic MCP-enabling of existing bioinformatics web services, with breadcrumbs for reproducibility and a cookiecutter template for creating new servers. **Their paper was published in Briefings in Bioinformatics (Volume 27, Issue 1, January 2026, Oxford Academic)** — elevating from arXiv preprint to peer-reviewed journal, lending academic credibility to the MCP-for-bioinformatics approach.

### BioinfoMCP — Automated Tool Conversion

The BioinfoMCP platform automatically converts existing bioinformatics tools into MCP servers using LLMs — achieving a 94.7% success rate across 38 tools in benchmark tests. This could dramatically accelerate MCP adoption across the thousands of existing bioinformatics tools.

---

## What's Missing

Coverage has improved dramatically since March, but gaps remain:

- ~~**AlphaFold**~~ — **FILLED**: Augmented-Nature/AlphaFold-MCP-Server (33 stars, 25+ tools)
- ~~**KEGG**~~ — **FILLED**: Augmented-Nature/KEGG-MCP-Server (9 stars, 30 tools)
- ~~**Medical imaging AI**~~ — **PARTIALLY FILLED**: Owkin Pathology Explorer (pathology AI via Claude HCLS), fluxinc/dicom-mcp-server (PACS/VNA connectivity). Radiology AI still absent.
- ~~**EHR clinical decision support**~~ — **PARTIALLY FILLED**: LangCare MCP FHIR (40+ clinical skills). Full clinical reasoning still emerging.
- **Galaxy workflows** — still no MCP wrapper for the Galaxy bioinformatics platform
- **Single-cell pipelines** — no comprehensive scRNA-seq pipeline MCP (only QC skills via Anthropic marketplace)
- **Nextflow/Snakemake** — no workflow engine MCP for orchestrating bioinformatics pipelines (Nextflow skill exists in Anthropic marketplace but not a standalone MCP)
- **Multi-omics integration** — no MCP server combining genomics, transcriptomics, proteomics, and metabolomics data

## The Bottom Line

Bioinformatics and life sciences is one of the most active and well-organized MCP server categories — and it got significantly stronger since our March review. BioMCP doubled to 497 stars, proving strong demand for biomedical AI tools. Anthropic's $400M Coefficient Bio acquisition and Owkin Pathology Explorer launch signal that major companies see life sciences as a primary MCP use case. The two biggest gaps we identified — AlphaFold and KEGG — are now filled. Augmented-Nature now maintains 15+ servers covering virtually every major biological database. The drug discovery pipeline is now truly end-to-end — from target identification through AlphaFold structure prediction to patent search. LangCare's enterprise FHIR server brings production-ready clinical infrastructure. The remaining gaps — Galaxy workflows, comprehensive single-cell pipelines, workflow orchestration, and multi-omics integration — are increasingly narrow. **Rating: 4.5/5.**

*This review was refreshed on 2026-04-28 (previous: 2026-03-16) using Claude Opus 4.6 (Anthropic).*
