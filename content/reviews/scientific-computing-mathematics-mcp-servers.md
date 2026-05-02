---
title: "Scientific Computing & Mathematics MCP Servers — MATLAB, Wolfram, R, Julia, SymPy, and More"
date: 2026-03-19T23:00:00+09:00
description: "Scientific computing MCP servers let AI agents run MATLAB code, solve equations symbolically, perform statistical analysis, and execute computations on HPC clusters."
og_description: "Scientific computing MCP servers: MATLAB official (483 stars, MathWorks — run MATLAB via AI agents), RMCP (201 stars, 52 R statistical tools, 429 packages), Kaimon.jl (62 stars, 32+ Julia tools), mcp.science (131 stars, 12+ research servers), SymPy MCP (66 stars, Streamable HTTP), siqiliu-tsinghua/mma-mcp (24 stars, 995 weekly visitors), COMSOL MCP ecosystem (3 servers), SageMath gap partially closed. Rating: 4.0/5."
content_type: "Review"
card_description: "Scientific computing and mathematics MCP servers for AI-powered numerical analysis, symbolic math, statistics, and HPC workflows. **MATLAB nearly tripled to 483 stars** — matlab/matlab-mcp-core-server (official MathWorks, v0.9.0) is now one of the highest-traffic scientific MCP servers at 8,600 weekly PulseMCP visitors. Supports Claude Code, VS Code Copilot, GitHub Copilot, and Gemini CLI. New community servers add async job management and Simulink model control. **Julia ecosystem dramatically upgraded** — kahliburke/Kaimon.jl (62 stars, v1.3.1 April 2026) brings 32+ tools including live execution, type introspection, debugging with Infiltrator.jl, semantic search, and ZMQ process bridging. aplavin/julia-mcp (55 stars, very active) provides lightweight per-project session isolation. Both vastly outpace earlier Julia options. **R statistics still strong** — finite-sample/rmcp (201 stars, 52 tools, 429 CRAN packages) remains the most comprehensive single-language scientific MCP server with live cloud server. **SageMath gap partially closed** — XBP-Europe/sagemath-mcp (5 stars, 33 tools, April 2026) provides stateful SageMath sessions with AST-based security validation covering calculus, algebra, ODEs, number theory, and visualization. **COMSOL gap partially closed** — three community servers now cover COMSOL Multiphysics: wjc9011/COMSOL_Multiphysics_MCP (39 stars, 597 weekly PulseMCP visitors), 777gegewu/comsol-mcp (23 stars, very active), and a new April 2026 entry by sparkyscientist. **New Wolfram high-traffic entry** — siqiliu-tsinghua/mma-mcp (24 stars, April 2026, 995 weekly PulseMCP visitors) wraps local Wolfram Engine with security modes, role-based access, and OAuth 2.1 — highest-traffic new entry in this window. **Symbolic math improving** — sdiehl/sympy-mcp grew to 66 stars (+61%) and added Streamable HTTP transport. **Optimization now covered** — optuna/optuna-mcp (75 stars, official Preferred Networks) brings hyperparameter optimization via Optuna with 10+ visualization tools. Formal mathematics enters with Axiomatic Prover (Lean 4 + Mathlib, Feb 2026). Major remaining gaps: no SciPy standalone MCP, no ANSYS/ABAQUS coverage, Gurobi/CPLEX still absent."
last_refreshed: 2026-05-02
---

Scientific computing MCP servers let AI agents execute numerical code, solve equations symbolically, run statistical analyses, and submit jobs to supercomputers. Instead of manually writing MATLAB scripts, R commands, or Wolfram Language expressions, researchers can have AI assistants perform these computations through the Model Context Protocol. Part of our **[Science & Research MCP category](/categories/science-research/)**.

This review covers MCP servers for **scientific computing and mathematics** — numerical analysis platforms (MATLAB, NumPy), symbolic math (SymPy, Wolfram, Mathematica), statistical computing (R), scientific programming languages (Julia), HPC infrastructure (Globus), and engineering simulation (OpenFOAM, COMSOL). For academic paper search and bioinformatics, see our [Science & Research review](/reviews/science-research-mcp-servers/). For 3D simulation and digital twins, see our [Digital Twins & 3D Simulation review](/reviews/digital-twins-3d-simulation-mcp-servers/).

The headline findings: **MathWorks' official MATLAB MCP server nearly tripled to 483 stars** and now ranks among the highest-traffic scientific MCP servers (8,600 weekly PulseMCP visitors). **Julia's MCP ecosystem dramatically upgraded** — Kaimon.jl (62 stars) and aplavin/julia-mcp (55 stars) are both new and active as of April 2026. **Three COMSOL MCP servers now exist**, partially closing that engineering simulation gap. **SageMath gap partially closed** by a production-ready April 2026 launch. **Wolfram coverage expanded** with a new high-traffic entry (24 stars, 995 weekly PulseMCP visitors). **Symbolic math fragmentation easing** — sdiehl/sympy-mcp grew 61% and added Streamable HTTP transport.

## Numerical Computing Platforms

### matlab/matlab-mcp-core-server (Official MathWorks)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server) | 483 | MATLAB | MathWorks License |

The **official MATLAB MCP server from MathWorks** — not a community wrapper, but built and maintained by the MATLAB team. Stars nearly tripled from 178 to 483 since March 2026. Version 0.9.0 released April 30, 2026 (13 total releases, 118 commits). PulseMCP reports approximately 8,600 weekly visitors — among the highest-traffic scientific computing MCP servers.

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
| [WilliamCloudQi/matlab-mcp-server](https://github.com/WilliamCloudQi/matlab-mcp-server) | — | Scientific computing and data analysis, natural language script generation |
| [Tsuchijo/matlab-mcp](https://github.com/Tsuchijo/matlab-mcp) | — | LLM-driven MATLAB script writing and execution |
| [hansur94/mcp-matlab](https://github.com/hansur94/mcp-matlab) | — | Async job management for MATLAB (March 2026) |
| [sohumsuthar/simulink-mcp](https://github.com/sohumsuthar/simulink-mcp) | — | Simulink model control via MCP (March 2026) |

Four community alternatives now exist. The two new March 2026 entries add async job management and dedicated Simulink model control — capabilities beyond the official server's scope.

## Statistical Computing (R)

### finite-sample/rmcp (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rmcp](https://github.com/finite-sample/rmcp) | 201 | Python | MIT | 52 |

The **most comprehensive single-language scientific MCP server** we've found. RMCP exposes 52 statistical analysis tools across 11 categories, systematically drawing from 429 R packages via CRAN task views:

- **Econometrics** — regression, instrumental variables, panel data
- **Machine learning** — classification, clustering, ensemble methods
- **Time series** — ARIMA, state-space models, forecasting
- **Survival analysis** — Kaplan-Meier, Cox proportional hazards
- **Bayesian statistics** — MCMC, hierarchical models
- **Spatial statistics** — geostatistics, point patterns

Production-ready with full MCP protocol compliance, HTTP transport and SSE support, stdio mode for Claude Desktop, and a publicly available test server. Growth has been minimal (197→201 stars since March) but it remains the dominant R MCP server with a live cloud endpoint and 275 commits.

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
| [sympy-mcp](https://github.com/sdiehl/sympy-mcp) | 66 | Python | — |

Built by Stephen Diehl (known for Haskell work), this server exposes **SymPy's full computer algebra system** — symbolic manipulation, equation solving, calculus (integration, differentiation), simplification, factoring, expansion. Stars grew from 41 to 66 (+61%) since March. Major update: added **Streamable HTTP transport** (MCP spec 2025-03-26), replacing legacy SSE transport — HTTP-capable clients including VS Code, Cursor, Cline, and 5ire can now connect without subprocess. Docker support added. PulseMCP reports approximately 398 weekly visitors.

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
| [sagemath-mcp](https://github.com/XBP-Europe/sagemath-mcp) | 5 | Python | — |

The first production-ready SageMath MCP server, launched April 2026. Provides **33 MCP tools** covering: calculus (differentiation, integration, limits), algebra, linear algebra, ordinary differential equations, number theory, statistics, and visualization. Notable design decisions:

- **Stateful sessions** with process isolation — computations build on each other within a session
- **AST-based security validation** — evaluates SageMath code safely without arbitrary execution
- Deployment: Docker, PyPI, Docker Compose; health endpoints; FastMCP 3.x, Python 3.12+

SageMath's strength is breadth — it wraps SymPy, R, Maxima, GAP, FLINT, and dozens of other math packages under one interface. An MCP server means all of those libraries are accessible through a single integration.

A minimal alternative exists: **GaloisHLee/mcp-server-sagemath** (9 stars, TypeScript, October 2025) — 3 tools (version check, evaluate, health check), stateless HTTP mode. Functional but limited compared to the XBP-Europe version.

## Wolfram Ecosystem

### siqiliu-tsinghua/mma-mcp (NEW — Highest-Traffic New Entry)

| Server | Stars | Language | License | PulseMCP |
|--------|-------|----------|---------|---------|
| [mma-mcp](https://github.com/siqiliu-tsinghua/mma-mcp) | 24 | Python | — | ~995 weekly |

The most significant new Wolfram entry since the original review. Launched April 17, 2026 — roughly 13 days ago — and already drawing approximately 995 weekly PulseMCP visitors, making it the highest-traffic new scientific computing MCP server in this window. Wraps a **local Wolfram Engine** for symbolic math, numerical analysis, and visualization via Wolfram Language.

Notable security design: 29 capability groups (numeric computation, calculus, linear algebra, statistics, etc.) with per-group access control. Supports OAuth 2.1. TOML configuration. Per-client role-based access. This is more sophisticated security architecture than most MCP servers in any category.

Requires a Wolfram Engine or Mathematica license (no Wolfram affiliation — community project).

### paraporoco/Wolfram-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Wolfram-MCP](https://github.com/paraporoco/Wolfram-MCP) | 9 | Python | MIT | 11 |

The original Wolfram Language MCP server — 11 tools covering `calculate`, `solve`, `integrate`, `differentiate`, `simplify`, `factor`, `expand`, `matrix_operations`, `statistics`, and arbitrary `execute`. Stars grew modestly (6→9). **Last commit October 2025** — effectively dormant. For active development, the newer mma-mcp entry above is a better choice.

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
| [Kaimon.jl](https://github.com/kahliburke/Kaimon.jl) | 62 | Julia | — | v1.3.1 (Apr 16, 2026) |

The most feature-rich Julia MCP server and a major new development in this category. v1.3.1 released April 16, 2026. Provides **32+ tools**:

- **Live code execution** — run Julia code with persistent session state
- **Type introspection** — inspect types, methods, and package structures
- **Debugging integration** — Infiltrator.jl for live debugging within MCP sessions
- **Semantic search** — Qdrant vector database integration for code/docs search
- **The Gate** — connect to external Julia processes via ZMQ (bridge from existing Julia apps)
- **Terminal dashboard** — live output monitoring
- **Three security modes** — control execution permissions
- **Automatic schema generation** from Julia function signatures

214 commits, works with Claude Code, Cursor, and VS Code. This is a full scientific workflow tool, not just a REPL wrapper.

### aplavin/julia-mcp (NEW — Active Lightweight Option)

| Server | Stars | Language |
|--------|-------|----------|
| [julia-mcp](https://github.com/aplavin/julia-mcp) | 55 | Python |

A lightweight, actively maintained alternative (25 commits, last commit within days). Three tools: `julia_eval`, `julia_restart`, `julia_list_sessions`. Per-project-directory session isolation — each project gets its own Julia process so dependencies don't conflict. Pure stdio, no open ports. Supports Claude Code, Claude Desktop, Codex CLI, and VS Code Copilot. The simpler choice when Kaimon.jl's full feature set isn't needed.

### samtalki/AgentREPL.jl (Persistent REPL)

| Server | Language |
|--------|----------|
| [AgentREPL.jl](https://github.com/samtalki/AgentREPL.jl) | Julia |

Solves Julia's **time-to-first-execution (TTFX) problem** for AI workflows. The Julia process stays alive across interactions, so you only pay the compilation cost once. Provides persistent REPL sessions via MCP STDIO transport — meaning AI agents can build on previous computations within the same session. Low stars (3) but architecturally sound.

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
| [science-mcps](https://github.com/globus-labs/science-mcps) | 12 | Python | — |

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
| [mcp.science](https://github.com/pathintegral-institute/mcp.science) | 131 | Python | MIT |

Bundles **12+ specialized MCP servers** for scientific research under one umbrella (117→131 stars, +12%). Install any server with `uvx mcp-science <name>`. Includes GPAW DFT calculations, Materials Project database queries, sandboxed Python execution, Jupyter kernel interaction, Mathematica, SSH remote execution, and web fetch. No major new releases since the original review (last release v0.2.0, July 2025) but steady star growth suggests continuing community adoption.

Already covered in our [Science & Research review](/reviews/science-research-mcp-servers/), but its scientific computing components (DFT, Materials Project, sandboxed execution) are directly relevant here.

## Engineering Simulation

### COMSOL Multiphysics (Gap Partially Closed)

| Server | Stars | Language | PulseMCP |
|--------|-------|----------|---------|
| [wjc9011/COMSOL_Multiphysics_MCP](https://github.com/wjc9011/COMSOL_Multiphysics_MCP) | 39 | Python | ~597 weekly |
| [777gegewu/comsol-mcp](https://github.com/777gegewu/comsol-mcp) | 23 | Python | — |
| sparkyscientist/comsol-mcp | — | — | ~199 weekly |

Three community MCP servers now cover COMSOL, closing one of the most notable engineering simulation gaps from the original review.

**wjc9011/COMSOL_Multiphysics_MCP** (February 2026, 39 stars, 597 weekly PulseMCP visitors) — the leading COMSOL MCP server. Controls COMSOL via the MPh Python library. Highest star count and strongest PulseMCP traffic in the group.

**777gegewu/comsol-mcp** (23 stars, last commit within days of this review) — actively maintained, controls COMSOL Desktop GUI via Java Shell. The most actively developed option.

**sparkyscientist's entry** (April 14, 2026) — physics-aware mesh generation, solver configuration, and parametric sweeps. New enough that star count is minimal but drawing ~199 weekly PulseMCP visitors.

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
| [optuna-mcp](https://github.com/optuna/optuna-mcp) | 75 | Python | MIT | 10+ |

The first **optimization-focused MCP server with official vendor backing**. Built by Preferred Networks, the creators of Optuna, this server exposes hyperparameter optimization workflows via MCP. v0.2.0 (November 2025). Features 10+ visualization tools, Docker support, and PulseMCP presence (~499 weekly visitors). While Optuna focuses on ML hyperparameter optimization rather than mathematical programming (CPLEX/Gurobi/CVXPY), it fills a real gap for ML researchers. No Gurobi, CPLEX, or CVXPY-dedicated MCP server has emerged.

### Axiomatic Prover (Lean 4 Theorem Proving)

Listed on PulseMCP as an official provider entry (February 23, 2026) — a Lean 4 theorem prover with Mathlib integration for formal mathematics verification. Represents a new category in mathematical MCP: formal proof assistants alongside numeric and symbolic tools. GitHub repository details unconfirmed.

### Multi-Backend Scientific Computing

| Server | Stars | Language | Backends |
|--------|-------|----------|---------|
| [sanshanjianke/scicompute-mcp](https://github.com/sanshanjianke/scicompute-mcp) | 2 | Python | Mathematica, SageMath, Python Scientific, R, Octave, Julia, Maxima |

A novel approach: one server with seven computational backends. `compute()`, `list_backends()`, `stop()`, `doc()` tools with persistent sessions and image output for plots. **The only MCP server with GNU Octave support** — partial coverage but currently unique. Auto-backend selection available. Very new (last commit April 2026), very early stage.

## What's Missing

**No standalone SciPy MCP server.** SciPy appears bundled in calculator servers but has no dedicated MCP server exposing its optimization, signal processing, and linear algebra capabilities as first-class tools.

**No Maple MCP server.** Maple is widely used in education and engineering for symbolic math.

**No ANSYS or ABAQUS MCP servers.** ANSYS FEA/FEM simulation has only fragmented community attempts (knewnothing-git/ansys-mcp-server at 7 stars, svd-ai-lab/fluent-mcp-server archived). ABAQUS has no coverage at all. Given three COMSOL servers now exist, ANSYS is the clearest remaining simulation gap.

**No Gurobi or CPLEX MCP server.** Mathematical programming and operations research still lack dedicated solver coverage. KKonuru/GurobiMCP exists (1 star) but is trivial. CVXPY coverage is only through bundled tools.

**No GNU Octave standalone MCP server.** scicompute-mcp covers Octave as one of seven backends, but no dedicated Octave MCP server exists. Given MATLAB's license requirements, an Octave MCP server would democratize MATLAB-compatible computing.

## The Verdict

**Rating: 4.0 / 5** — Official vendor momentum, dramatically upgraded Julia and Wolfram options, engineering simulation gaps partially closing.

Since the March review, this category has materially improved. **MATLAB nearly tripled** — 178 to 483 stars, v0.9.0 released April 30, 8,600 weekly PulseMCP visitors — confirming this is the most adopted official scientific computing MCP server by a wide margin. **Julia's ecosystem underwent the biggest transformation**: the original review had only 2-3 star servers; now Kaimon.jl (62 stars, 32+ tools, April 2026) and aplavin/julia-mcp (55 stars, very active) provide professional-grade options that address real Julia workflow needs.

**COMSOL gap is partially closed** with three community servers and ~800 combined weekly PulseMCP visitors. **SageMath gap partially closed** with a production-ready server (33 tools, AST security, Docker). **Wolfram coverage expanded** with siqiliu-tsinghua/mma-mcp (995 weekly PulseMCP visitors in its first two weeks — the highest-traffic debut in this category). **Optimization has its first official vendor entry** with Optuna/optuna-mcp (75 stars). **Formal mathematics enters** via Lean 4/Mathlib.

The remaining weaknesses are real but narrowing: SciPy still has no standalone MCP server, ANSYS/ABAQUS remain absent, and Gurobi/CPLEX optimization is uncovered. Fragmentation in symbolic math (15+ Wolfram/SymPy wrappers) persists but the high-traffic new entries (mma-mcp, sympy-mcp's Streamable HTTP) suggest convergence is beginning.

For researchers: start with the **official MATLAB server** if you have a license, **RMCP** for statistics, **mcp.science** for multi-tool scientific workflows, **Kaimon.jl** or **aplavin/julia-mcp** for Julia, **mma-mcp** for Wolfram Language, **sagemath-mcp** for SageMath, and **wjc9011/COMSOL_Multiphysics_MCP** for simulation. For symbolic math, **sdiehl/sympy-mcp** is the cleanest option with its new Streamable HTTP transport. For HPC, **Globus Labs' science-mcps** is the only game in town — and it's a good one.

*Last updated: May 2, 2026. Star counts and features reflect what we found during research. We do not install or test these servers hands-on — our reviews are based on documentation, source code analysis, GitHub activity, and community feedback. See our [methodology note](/reviews/#methodology) for details.*
