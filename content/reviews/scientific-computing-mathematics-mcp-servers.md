---
title: "Scientific Computing & Mathematics MCP Servers — MATLAB, Wolfram, R, Julia, SymPy, and More"
date: 2026-03-19T23:00:00+09:00
description: "Scientific computing MCP servers let AI agents run MATLAB code, solve equations symbolically, perform statistical analysis, and execute computations on HPC clusters."
og_description: "Scientific computing MCP servers: MATLAB official (~1,400 stars, MathWorks — run MATLAB via AI agents), RMCP (209 stars, 54 R statistical tools, 429 packages), Kaimon.jl (10 stars, 32+ Julia tools), mcp.science (147 stars, 12+ research servers), SymPy MCP (79 stars, Streamable HTTP), COMSOL MCP ecosystem (3 servers, one now 600+ stars), SageMath gap partially closed. Rating: 4.0/5."
content_type: "Review"
card_description: "Scientific computing and mathematics MCP servers for AI-powered numerical analysis, symbolic math, statistics, and HPC workflows. **MATLAB has grown roughly 3x since March** — [matlab/matlab-mcp-server](https://github.com/matlab/matlab-mcp-server) (official MathWorks, renamed from matlab-mcp-core-server) is now around 1,400 GitHub stars and remains one of the highest-traffic scientific MCP servers per [PulseMCP](https://www.pulsemcp.com/servers/mathworks-matlab). Supports Claude Code, VS Code Copilot, GitHub Copilot, and Gemini CLI. New community servers add async job management and Simulink model control. **Julia ecosystem mixed** — kahliburke/Kaimon.jl (now 10 stars, v1.3.1 April 2026) brings 32+ tools including live execution, type introspection, debugging with Infiltrator.jl, semantic search, and ZMQ process bridging. aplavin/julia-mcp (now 83 stars, very active) provides lightweight per-project session isolation. **R statistics still strong** — finite-sample/rmcp (209 stars, 54 tools, 429 CRAN packages) remains the most comprehensive single-language scientific MCP server with live cloud server. **SageMath gap partially closed** — XBP-Europe/sagemath-mcp (11 stars, 37 tools as of its latest release) provides stateful SageMath sessions with AST-based security validation covering calculus, algebra, ODEs, number theory, and visualization. **COMSOL gap partially closed** — three community servers now cover COMSOL Multiphysics: wjc9011/COMSOL_Multiphysics_MCP (now ~643 stars, with an associated 2026 *Neurocomputing* paper), 777gegewu/comsol-mcp (now 114 stars), and an April 2026 entry by juijunnarkar (submitted to PulseMCP under the handle sparkyscientist). **Wolfram: the new high-traffic community entry was short-lived** — siqiliu-tsinghua/mma-mcp was archived by its owner on August 4, 2026, deprecated in favor of Wolfram's own official [Wolfram Cloud/Local MCP](https://www.wolfram.com/artificial-intelligence/mcp/cloud/) support shipping in Mathematica 15. **Symbolic math improving** — sdiehl/sympy-mcp grew to 79 stars and added Streamable HTTP transport (Apache-2.0 licensed). **Optimization now covered** — optuna/optuna-mcp (84 stars, official Preferred Networks, confirmed via [PulseMCP's official-server listing](https://www.pulsemcp.com/servers/optuna)) brings hyperparameter optimization via Optuna with 10+ visualization tools. Formal mathematics enters with Axiomatic Prover (Lean 4 + Mathlib, Feb 2026). Major remaining gaps: no SciPy standalone MCP, no ABAQUS coverage, Gurobi/CPLEX still absent."
last_refreshed: 2026-08-16
sources_audited: 2026-08-16
---

Scientific computing MCP servers let AI agents execute numerical code, solve equations symbolically, run statistical analyses, and submit jobs to supercomputers. Instead of manually writing MATLAB scripts, R commands, or Wolfram Language expressions, researchers can have AI assistants perform these computations through the Model Context Protocol. Part of our **[Science & Research MCP category](/categories/science-research/)**.

This review covers MCP servers for **scientific computing and mathematics** — numerical analysis platforms (MATLAB, NumPy), symbolic math (SymPy, Wolfram, Mathematica), statistical computing (R), scientific programming languages (Julia), HPC infrastructure (Globus), and engineering simulation (OpenFOAM, COMSOL). For academic paper search and bioinformatics, see our [Science & Research review](/reviews/science-research-mcp-servers/). For 3D simulation and digital twins, see our [Digital Twins & 3D Simulation review](/reviews/digital-twins-3d-simulation-mcp-servers/).

The headline findings: **MathWorks' official MATLAB MCP server has grown roughly 3x since March**, to around 1,400 GitHub stars ([matlab/matlab-mcp-server](https://github.com/matlab/matlab-mcp-server), renamed from matlab-mcp-core-server), and remains among the highest-traffic scientific MCP servers per [PulseMCP](https://www.pulsemcp.com/servers/mathworks-matlab). **Julia's MCP ecosystem is mixed** — aplavin/julia-mcp grew to 83 stars, while kahliburke/Kaimon.jl now shows 10 stars, both active as of this audit. **Three COMSOL MCP servers now exist**, partially closing that engineering simulation gap, and the leading one (wjc9011/COMSOL_Multiphysics_MCP) has grown to roughly 643 stars with an accompanying 2026 *Neurocomputing* paper. **SageMath gap partially closed** by a production-ready April 2026 launch, now at 37 tools. *Correction (2026-08-16): the "new high-traffic Wolfram entry" flagged in the previous audit (siqiliu-tsinghua/mma-mcp) was archived by its owner on August 4, 2026 — deprecated because Wolfram now ships its own official [Wolfram Cloud/Local MCP](https://www.wolfram.com/artificial-intelligence/mcp/cloud/) support in Mathematica 15. It is removed from the recommendations below.* **Symbolic math fragmentation easing** — sdiehl/sympy-mcp grew to 79 stars and added Streamable HTTP transport.

## Numerical Computing Platforms

### matlab/matlab-mcp-server (Official MathWorks)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [matlab-mcp-server](https://github.com/matlab/matlab-mcp-server) | ~1,400 | Go | MathWorks License |

The **official MATLAB MCP server from MathWorks** — not a community wrapper, but built and maintained by the MATLAB team. *Correction (2026-08-16): the repo was renamed from matlab-mcp-core-server to matlab-mcp-server (old links redirect); stars have grown from 483 in May 2026 to roughly 1,400 now, and GitHub's language detection now reports the implementation as Go rather than MATLAB — corrected here from the earlier audit.* Version 0.9.0 released April 30, 2026. [PulseMCP tracks it](https://www.pulsemcp.com/servers/mathworks-matlab) as one of the highest-traffic scientific computing MCP servers, with an estimated 216k all-time visitors as of this audit.

### What Works Well

**Run MATLAB through AI agents.** Execute MATLAB code directly in conversations, generate scripts from natural language descriptions, and access MATLAB documentation — all through the standard MCP protocol.

**Broad client support.** Explicitly supports Claude Code, Claude Desktop, Visual Studio Code, and GitHub Copilot. MathWorks tests against multiple MCP clients, which is unusual attention to interoperability.

**Simulink integration.** MathWorks demonstrates simulating Simulink models through GitHub Copilot via the MCP server — AI agents can interact with complex simulation workflows, not just script execution.

**MathWorks also ships an MCP client.** MATLAB can act as both MCP server (exposing MATLAB to AI) and MCP client (connecting MATLAB to other MCP servers). This bidirectional approach is rare in the MCP ecosystem.

### What Doesn't Work Well

**Requires MATLAB license.** The server needs a local MATLAB installation and a commercial license. This limits accessibility compared to open-source alternatives.

**Not open source.** Released under MathWorks' proprietary license, not MIT or Apache-2.0.

### Community MATLAB Servers

| Server | Stars | Description |
|--------|-------|-------------|
| [WilliamCloudQi/matlab-mcp-server](https://github.com/WilliamCloudQi/matlab-mcp-server) | 55 | Scientific computing and data analysis, natural language script generation |
| [Tsuchijo/matlab-mcp](https://github.com/Tsuchijo/matlab-mcp) | 39 | LLM-driven MATLAB script writing and execution |
| [sohumsuthar/simulink-mcp](https://github.com/sohumsuthar/simulink-mcp) | 23 | Simulink model control via MCP (March 2026) |

*Correction (2026-08-16): hansur94/mcp-matlab (previously listed here for async job management) now returns a 404 on GitHub — the repo no longer exists at that path, so it has been removed rather than left as a dead citation.* Three community alternatives remain confirmed live; sohumsuthar/simulink-mcp adds dedicated Simulink model control beyond the official server's scope.

## Statistical Computing (R)

### finite-sample/rmcp (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rmcp](https://github.com/finite-sample/rmcp) | 209 | Python | MIT | 54 |

The **most comprehensive single-language scientific MCP server** we've found. RMCP exposes 54 statistical analysis tools *(corrected 2026-08-16 from 52 — the README now states 54 tools)* across 11 categories, systematically drawing from 429 R packages via CRAN task views:

- **Econometrics** — regression, instrumental variables, panel data
- **Machine learning** — classification, clustering, ensemble methods
- **Time series** — ARIMA, state-space models, forecasting
- **Survival analysis** — Kaplan-Meier, Cox proportional hazards
- **Bayesian statistics** — MCMC, hierarchical models
- **Spatial statistics** — geostatistics, point patterns

Production-ready with full MCP protocol compliance, HTTP transport and SSE support, stdio mode for Claude Desktop, and a publicly available test server. Growth has been modest (201→209 stars since the last audit) but it remains the dominant R MCP server with a live cloud endpoint.

### Other R Servers

| Server | Description |
|--------|-------------|
| [Posit mcptools](https://posit-dev.github.io/mcptools/) | Run R code in live RStudio sessions via MCP |
| [chi2labs/mcpr](https://github.com/chi2labs/mcpr) | Expose arbitrary R functions through MCP |
| [cafferychen777/Rstudio-mcp](https://github.com/cafferychen777/Rstudio-mcp) | Deep RStudio IDE integration |
| [IMNMV/ClaudeR](https://github.com/IMNMV/ClaudeR) | Connect RStudio to Claude Code, Codex, Gemini via MCP |

**Posit's mcptools** is notable — from the makers of RStudio and the tidyverse, it lets MCP-enabled tools interact with running R sessions. This isn't a wrapper; it connects AI directly to your active analysis environment.

## Symbolic Mathematics

### sdiehl/sympy-mcp

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [sympy-mcp](https://github.com/sdiehl/sympy-mcp) | 79 | Python | Apache-2.0 |

Built by Stephen Diehl (known for Haskell work), this server exposes **SymPy's full computer algebra system** — symbolic manipulation, equation solving, calculus (integration, differentiation), simplification, factoring, expansion. Stars have grown to 79 (from 66 at the last audit). Major update: added **Streamable HTTP transport** (MCP spec 2025-03-26), replacing legacy SSE transport — HTTP-capable clients including VS Code, Cursor, Cline, and 5ire can now connect without subprocess, per the [project README](https://github.com/sdiehl/sympy-mcp). Docker support added. [PulseMCP tracks its traffic](https://www.pulsemcp.com/servers/sdiehl-sympy) among the more-visited SymPy MCP servers.

### huhabla/calculator-mcp-server (Multi-Library)

| Server | Language | License |
|--------|----------|---------|
| [calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server) | Python | — |

Combines **three Python scientific libraries in one server**: SymPy for symbolic math, NumPy for numerical computation, and SciPy for statistical analysis. Includes matrix operations. A good choice if you want one server instead of three.

### tufantunc/axiom-advanced-math-mcp

| Server | Language | License |
|--------|----------|---------|
| [axiom-advanced-math-mcp](https://github.com/tufantunc/axiom-advanced-math-mcp) | TypeScript | — |

**High-precision symbolic math** powered by Giac/Xcas (the CAS behind HP Prime calculators) and mathjs. Covers differential equations, symbolic mathematics, and financial time-series analysis. The Giac backend provides arbitrary-precision arithmetic that SymPy-based servers typically don't offer.

### Other Math Servers

| Server | Description |
|--------|-------------|
| [EthanHenrickson/math-mcp](https://github.com/EthanHenrickson/math-mcp) | Basic math and statistics for LLMs |
| [SHSharkar/MCP-Mathematics](https://github.com/SHSharkar/MCP-Mathematics) | 52 functions, 158 unit conversions, financial calculations |
| [edwardpwtsoi/mathjs-mcp](https://github.com/edwardpwtsoi/mathjs-mcp) | mathjs wrapper |
| [colesmcintosh/numpy-mcp](https://github.com/colesmcintosh/numpy-mcp) | NumPy numerical computing via MCP |
| [YuChenSSR/symbolica-mcp](https://github.com/YuChenSSR/symbolica-mcp) | Symbolic computing for quantum computing workflows |

## SageMath

### XBP-Europe/sagemath-mcp (NEW — SageMath Gap Partially Closed)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [sagemath-mcp](https://github.com/XBP-Europe/sagemath-mcp) | 11 | Python | — |

The first production-ready SageMath MCP server, launched April 2026. Now at **37 MCP tools** *(updated 2026-08-16 from 33 — the [project's README](https://github.com/XBP-Europe/sagemath-mcp) shows continued growth: 18 tools in the v0.2.0 release, 33 in v0.3.0, 37 currently)* covering: calculus (differentiation, integration, limits), algebra, linear algebra, ordinary differential equations, number theory, statistics, and visualization. Notable design decisions:

- **Stateful sessions** with process isolation — computations build on each other within a session
- **AST-based security validation** — evaluates SageMath code safely without arbitrary execution
- Deployment: Docker, PyPI, Docker Compose; health endpoints; FastMCP 3.x, Python 3.12+

SageMath's strength is breadth — it wraps SymPy, R, Maxima, GAP, FLINT, and dozens of other math packages under one interface. An MCP server means all of those libraries are accessible through a single integration.

A minimal alternative exists: **GaloisHLee/mcp-server-sagemath** (11 stars, TypeScript, October 2025) — 3 tools (version check, evaluate, health check), stateless HTTP mode. Functional but limited compared to the XBP-Europe version.

## Wolfram Ecosystem

### siqiliu-tsinghua/mma-mcp (ARCHIVED — superseded by official Wolfram MCP support)

| Server | Stars | Language | License | Status |
|--------|-------|----------|---------|---------|
| [mma-mcp](https://github.com/siqiliu-tsinghua/mma-mcp) | 33 | Python | — | Archived Aug 4, 2026 |

*Correction (2026-08-16): this entry was flagged in the previous audit as "the highest-traffic new Wolfram entry" with ~995 weekly PulseMCP visitors shortly after its April 17, 2026 launch. As of this audit it is **archived and deprecated** — [GitHub shows it was archived by its owner on August 4, 2026](https://github.com/siqiliu-tsinghua/mma-mcp), and the README states: "This project is deprecated and no longer maintained. The code is kept on GitHub for reference only," citing that Mathematica 15 now ships [official Wolfram Cloud/Local MCP support](https://www.wolfram.com/artificial-intelligence/mcp/cloud/) and that the project's dependency on an older MCP Python SDK made it incompatible with current installations. It previously wrapped a **local Wolfram Engine** for symbolic math, numerical analysis, and visualization, with a notable security design (29 capability groups, OAuth 2.1, per-client role-based access) — but it is no longer a live recommendation and has been dropped from the verdict below.*

### paraporoco/Wolfram-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Wolfram-MCP](https://github.com/paraporoco/Wolfram-MCP) | 13 | Python | MIT | 11 |

The original Wolfram Language MCP server — 11 tools covering `calculate`, `solve`, `integrate`, `differentiate`, `simplify`, `factor`, `expand`, `matrix_operations`, `statistics`, and arbitrary `execute`. Stars have grown slowly (9→13 since the last audit) but the repo shows only a handful of total commits — effectively dormant. *(The mma-mcp entry formerly recommended above as the active alternative is now archived — see the correction there; for local Wolfram Engine access, [Wolfram's own official MCP support](https://www.wolfram.com/artificial-intelligence/mcp/cloud/) is now the better-maintained option.)*

### texra-ai/mcp-server-mathematica

| Server | Language |
|--------|----------|
| [mcp-server-mathematica](https://github.com/texra-ai/mcp-server-mathematica) | — |

Executes **Mathematica code via wolframscript** — designed for derivation verification workflows. Requires Mathematica or the free Wolfram Engine for Developers.

### Wolfram Alpha API Servers

| Server | Language | Notes |
|--------|----------|-------|
| [StoneDot/wolframalpha-mcp-server](https://github.com/StoneDot/wolframalpha-mcp-server) | TypeScript | Wolfram Alpha LLM API |
| [akalaric/mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha) | Python | Full client + server |
| [cnosuke/mcp-wolfram-alpha](https://github.com/cnosuke/mcp-wolfram-alpha) | Go | Lightweight |
| [Garoth/wolframalpha-llm-mcp](https://github.com/Garoth/wolframalpha-llm-mcp) | — | Structured knowledge |
| [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) | — | Chat REPL integration |
| [benhaotang/mcp-mma-docs](https://github.com/benhaotang/mcp-mma-docs) | — | Mathematica docs only |

Five+ servers wrapping the **Wolfram Alpha API** — these don't require a local Mathematica installation, just an API key. They provide computational knowledge through Wolfram Alpha's cloud service. Fragmentation persists: none has emerged as the clear winner.

## Julia

### kahliburke/Kaimon.jl (NEW — Most Feature-Rich Julia MCP)

| Server | Stars | Language | License | Version |
|--------|-------|----------|---------|---------|
| [Kaimon.jl](https://github.com/kahliburke/Kaimon.jl) | 10 | Julia | — | v1.3.1 (Apr 16, 2026) |

The most feature-rich Julia MCP server by tool count. *(Corrected 2026-08-16: GitHub currently shows 10 stars, down from the 62 reported at the previous audit — worth flagging as an unexplained drop rather than typical organic growth; the repo is not archived and shows 500+ commits, so it remains active.)* v1.3.1 released April 16, 2026. Provides **32+ tools**:

- **Live code execution** — run Julia code with persistent session state
- **Type introspection** — inspect types, methods, and package structures
- **Debugging integration** — Infiltrator.jl for live debugging within MCP sessions
- **Semantic search** — Qdrant vector database integration for code/docs search
- **The Gate** — connect to external Julia processes via ZMQ (bridge from existing Julia apps)
- **Terminal dashboard** — live output monitoring
- **Three security modes** — control execution permissions
- **Automatic schema generation** from Julia function signatures

500+ commits *(updated 2026-08-16 from 214)*, works with Claude Code, Cursor, and VS Code. This is a full scientific workflow tool, not just a REPL wrapper.

### aplavin/julia-mcp (NEW — Active Lightweight Option)

| Server | Stars | Language |
|--------|-------|----------|
| [julia-mcp](https://github.com/aplavin/julia-mcp) | 83 | Python |

A lightweight, actively maintained alternative (36 commits as of this audit). Three tools: `julia_eval`, `julia_restart`, `julia_list_sessions`. Per-project-directory session isolation — each project gets its own Julia process so dependencies don't conflict. Pure stdio, no open ports. Supports Claude Code, Claude Desktop, Codex CLI, and VS Code Copilot. The simpler choice when Kaimon.jl's full feature set isn't needed.

### samtalki/AgentREPL.jl (Persistent REPL)

| Server | Language |
|--------|----------|
| [AgentREPL.jl](https://github.com/samtalki/AgentREPL.jl) | Julia |

Solves Julia's **time-to-first-execution (TTFX) problem** for AI workflows. The Julia process stays alive across interactions, so you only pay the compilation cost once. Provides persistent REPL sessions via MCP STDIO transport — meaning AI agents can build on previous computations within the same session. Low stars (7, up from 3) but architecturally sound.

### Other Julia Servers

| Server | Description |
|--------|-------------|
| [JuliaSMLM/ModelContextProtocol.jl](https://github.com/JuliaSMLM/ModelContextProtocol.jl) | Full MCP specification implemented in Julia |
| [JuliaBench/ClaudeMCPTools.jl](https://github.com/JuliaBench/ClaudeMCPTools.jl) | Basic MCP tools for Claude |
| [jonathanfischer97/juliadoc-mcp](https://github.com/jonathanfischer97/juliadoc-mcp) | Julia documentation server |

**JuliaSMLM/ModelContextProtocol.jl** implements the full MCP spec natively in Julia — useful for Julia developers who want to expose their own tools via MCP rather than use a pre-built server.

## HPC & Research Infrastructure

### globus-labs/science-mcps (Supercomputing Access)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [science-mcps](https://github.com/globus-labs/science-mcps) | 14 | Python | — |

From **Globus Labs** (University of Chicago / Argonne National Laboratory), this project connects AI agents to **national supercomputing facilities**:

- **Globus Transfer** — move data between Globus endpoints, browse remote directories, manage transfer tasks
- **Globus Compute** — register and execute Python functions on remote HPC endpoints (Polaris, etc.)
- **Globus Search** — create indices and search across Globus Search indexes
- **ALCF MCP** — interact with Argonne Leadership Computing Facility
- **NERSC MCP** — interact with the National Energy Research Scientific Computing Center
- **Diaspora MCP** — Diaspora Event Fabric for topic management and event streaming
- **Garden MCP** — domain-specific AI-for-science models (new addition)

A published paper ([arXiv:2508.18489](https://arxiv.org/pdf/2508.18489)) demonstrates the approach: an AI agent used Globus Compute MCP to write quantum chemistry functions, execute them on Polaris, and generate HOMO-LUMO gap visualizations consistent with published literature. Note: last commit was June 2025 — development activity may have slowed.

### pathintegral-institute/mcp.science (Research Hub)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [mcp.science](https://github.com/pathintegral-institute/mcp.science) | 147 | Python | MIT |

Bundles **12+ specialized MCP servers** for scientific research under one umbrella (131→147 stars since the last audit). Install any server with `uvx mcp-science <name>`. Includes GPAW DFT calculations, Materials Project database queries, sandboxed Python execution, Jupyter kernel interaction, Mathematica, SSH remote execution, and web fetch. Steady star growth suggests continuing community adoption.

Already covered in our [Science & Research review](/reviews/science-research-mcp-servers/), but its scientific computing components (DFT, Materials Project, sandboxed execution) are directly relevant here.

## Engineering Simulation

### COMSOL Multiphysics (Gap Partially Closed)

| Server | Stars | Language | PulseMCP |
|--------|-------|----------|---------|
| [wjc9011/COMSOL_Multiphysics_MCP](https://github.com/wjc9011/COMSOL_Multiphysics_MCP) | ~643 | Python | [tracked](https://www.pulsemcp.com/servers/wjc9011-comsol-multiphysics) |
| [777gegewu/comsol-mcp](https://github.com/777gegewu/comsol-mcp) | 114 | Python | — |
| [juijunnarkar/comsol_multiphysics_mcp](https://github.com/juijunnarkar/comsol_multiphysics_mcp) | 17 | — | [tracked](https://www.pulsemcp.com/servers/sparkyscientist-comsol-multiphysics) |

Three community MCP servers now cover COMSOL, closing one of the most notable engineering simulation gaps from the original review.

**wjc9011/COMSOL_Multiphysics_MCP** (February 2026, now ~643 stars — up sharply from 39 at the last audit) — the leading COMSOL MCP server. Controls COMSOL via the MPh Python library. There is now an associated peer-reviewed paper, ["COMSOL-MCP: An open-source model context protocol interface for AI-assisted multiphysics simulation"](https://doi.org/10.1016/j.neucom.2026.134481) (Naiyin Zhang and Junchao Wang, *Neurocomputing*, vol. 703, article 134481, 2026), which likely explains the traffic and star growth. Highest star count and strongest PulseMCP traffic in the group.

**777gegewu/comsol-mcp** (now 114 stars, up from 23) — controls COMSOL Desktop GUI via Java Shell.

*Correction (2026-08-16): the third entry was previously listed as "sparkyscientist/comsol-mcp" with no working link. That GitHub path returns a 404. PulseMCP's listing under the "sparkyscientist" submission handle actually points to a different repo owner, [juijunnarkar/comsol_multiphysics_mcp](https://github.com/juijunnarkar/comsol_multiphysics_mcp) (17 stars) — corrected here.* This entry (April 14, 2026) — physics-aware mesh generation, solver configuration, and parametric sweeps.

All three require a COMSOL license. Official COMSOL support for MCP has not been announced.

### OpenFOAM MCP Servers

| Server | Description |
|--------|-------------|
| [webworn/openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server) | CFD education with Socratic AI, mesh generation, turbulence models |
| [ymg2007/openfoam-mcp](https://github.com/ymg2007/openfoam-mcp) | Config management, cross-platform, wind-driven rain simulation |

Two MCP servers for **OpenFOAM**, the open-source CFD toolkit. **webworn's version** is education-focused — Socratic questioning and expert error resolution for CFD learning. Covers OpenFOAM 12 with blockMesh and k-ε/k-ω SST turbulence models. **ymg2007's version** is practical — read and modify OpenFOAM configuration files, with specialized tools for wind-driven rain simulation.

## Optimization & Formal Mathematics

### optuna/optuna-mcp (Official Preferred Networks)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [optuna-mcp](https://github.com/optuna/optuna-mcp) | 84 | Python | MIT | 10+ |

The first **optimization-focused MCP server with official vendor backing**. Built by Preferred Networks, the creators of Optuna — confirmed as an [official server listing on PulseMCP](https://www.pulsemcp.com/servers/optuna). Exposes hyperparameter optimization workflows via MCP. Features 10+ visualization tools and Docker support. While Optuna focuses on ML hyperparameter optimization rather than mathematical programming (CPLEX/Gurobi/CVXPY), it fills a real gap for ML researchers. No Gurobi or CPLEX-dedicated MCP server has emerged with meaningful adoption; CVXPY coverage remains only through bundled tools.

### Axiomatic Prover (Lean 4 Theorem Proving)

Listed on PulseMCP as an official provider entry (February 23, 2026) — a Lean 4 theorem prover with Mathlib integration for formal mathematics verification. Represents a new category in mathematical MCP: formal proof assistants alongside numeric and symbolic tools. GitHub repository details unconfirmed.

### Multi-Backend Scientific Computing

| Server | Stars | Language | Backends |
|--------|-------|----------|---------|
| [sanshanjianke/scicompute-mcp](https://github.com/sanshanjianke/scicompute-mcp) | 4 | Python | Mathematica, SageMath, Python Scientific, R, Octave, Julia, Maxima |

A novel approach: one server with seven computational backends. `compute()`, `list_backends()`, `stop()`, `doc()` tools with persistent sessions and image output for plots. **The only MCP server with GNU Octave support** — partial coverage but currently unique. Auto-backend selection available. Very new (last commit April 2026), very early stage.

## What's Missing

**No standalone SciPy MCP server.** SciPy appears bundled in calculator servers but has no dedicated MCP server exposing its optimization, signal processing, and linear algebra capabilities as first-class tools.

**No Maple MCP server.** Maple is widely used in education and engineering for symbolic math.

**No ANSYS or ABAQUS MCP servers with real traction.** ANSYS FEA/FEM simulation has only fragmented community attempts — [knewnothing-git/ansys-mcp-server](https://github.com/knewnothing-git/ansys-mcp-server) has grown to 48 stars (up from 7 at the last audit, worth watching), while [svd-ai-lab/fluent-mcp-server](https://github.com/svd-ai-lab/fluent-mcp-server) remains archived (confirmed: archived by its owner on Nov 28, 2025). ABAQUS has no coverage at all. Given three COMSOL servers now exist, ANSYS is the clearest remaining simulation gap.

**No Gurobi or CPLEX MCP server.** Mathematical programming and operations research still lack dedicated solver coverage. KKonuru/GurobiMCP exists (1 star) but is trivial. CVXPY coverage is only through bundled tools.

**No GNU Octave standalone MCP server.** scicompute-mcp covers Octave as one of seven backends, but no dedicated Octave MCP server exists. Given MATLAB's license requirements, an Octave MCP server would democratize MATLAB-compatible computing.

## The Verdict

**Rating: 4.0 / 5** — Official vendor momentum, an actively-growing Julia option, engineering simulation gaps partially closing, tempered by one high-traffic Wolfram entry going dark.

This category has materially improved since the original review, though this re-audit (2026-08-16) found several numbers had drifted well beyond simple growth. **MATLAB has grown roughly 3x** — from 483 to around 1,400 stars — confirming this is the most adopted official scientific computing MCP server by a wide margin, per [PulseMCP's own listing](https://www.pulsemcp.com/servers/mathworks-matlab). **Julia's ecosystem is mixed rather than uniformly "dramatically upgraded" as previously stated**: aplavin/julia-mcp grew from 55 to 83 stars and remains a solid lightweight option, but kahliburke/Kaimon.jl's star count fell from 62 to 10 between audits even as its commit history kept growing — still functional and feature-rich (32+ tools), just worth watching rather than treating as an obvious first choice.

**COMSOL gap is partially closed** with three community servers; the leading one, wjc9011/COMSOL_Multiphysics_MCP, jumped from 39 to ~643 stars, likely on the strength of an accompanying [peer-reviewed *Neurocomputing* paper](https://doi.org/10.1016/j.neucom.2026.134481). **SageMath gap partially closed** with a production-ready server (now 37 tools, AST security, Docker). **Wolfram coverage regressed, not expanded**: siqiliu-tsinghua/mma-mcp, previously flagged as the highest-traffic new entry, was archived and deprecated by its own maintainer on August 4, 2026, in favor of [Wolfram's official Mathematica 15 MCP support](https://www.wolfram.com/artificial-intelligence/mcp/cloud/). **Optimization has its first official vendor entry** with Optuna/optuna-mcp (84 stars). **Formal mathematics enters** via Lean 4/Mathlib.

The remaining weaknesses are real but narrowing: SciPy still has no standalone MCP server, ANSYS/ABAQUS remain effectively absent (though the leading ANSYS attempt has grown from 7 to 48 stars), and Gurobi/CPLEX optimization is uncovered. Fragmentation in symbolic math (15+ Wolfram/SymPy wrappers) persists; sdiehl/sympy-mcp's Streamable HTTP transport and growth to 79 stars is the clearest sign of convergence.

For researchers: start with the **official MATLAB server** if you have a license, **RMCP** for statistics, **mcp.science** for multi-tool scientific workflows, **aplavin/julia-mcp** for a lightweight Julia option (or **Kaimon.jl** if you need its fuller toolset), **Wolfram's own official MCP support** or **wolframalpha-mcp-server** for Wolfram Language (mma-mcp is no longer maintained), **sagemath-mcp** for SageMath, and **wjc9011/COMSOL_Multiphysics_MCP** for simulation. For symbolic math, **sdiehl/sympy-mcp** is the cleanest option with its Streamable HTTP transport. For HPC, **Globus Labs' science-mcps** is the only game in town — and it's a good one.

*Last updated: May 2, 2026; citations and figures re-audited August 16, 2026. Star counts and features reflect what we found during research. We do not install or test these servers hands-on — our reviews are based on documentation, source code analysis, GitHub activity, and community feedback. See our [methodology note](/reviews/#methodology) for details.*
