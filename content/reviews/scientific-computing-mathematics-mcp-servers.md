---
title: "Scientific Computing & Mathematics MCP Servers — MATLAB, Wolfram, R, Julia, SymPy, and More"
date: 2026-03-19T23:00:00+09:00
description: "Scientific computing MCP servers let AI agents run MATLAB code, solve equations symbolically, perform statistical analysis, and execute computations on HPC clusters. We reviewed 30+ servers across 6 subcategories. MATLAB leads with an official MathWorks server (178 stars). RMCP provides 52 statistical tools across 429 R packages (197 stars). Julia has three MCP implementations including a persistent REPL server. mcp.science bundles 12+ research servers including DFT calculations and Materials Project access. SymPy MCP and Wolfram MCP handle symbolic math. Globus Labs enables HPC job submission to ALCF and NERSC supercomputers. OpenFOAM gets two MCP servers for CFD simulation."
og_description: "Scientific computing MCP servers: MATLAB official (178 stars, MathWorks — run MATLAB via AI agents), RMCP (197 stars, 52 R statistical tools, 429 packages), mcp.science (117 stars, 12+ research servers, DFT/Materials Project), SymPy MCP (41 stars, symbolic math), Wolfram-MCP (Wolfram Language, 11 tools), Julia AgentREPL.jl (persistent REPL), Globus science-mcps (HPC/supercomputing), OpenFOAM MCP (CFD). 30+ servers. Rating: 3.5/5."
content_type: "Review"
card_description: "Scientific computing and mathematics MCP servers for AI-powered numerical analysis, symbolic math, statistics, and HPC workflows. **MATLAB gets official MathWorks support** — matlab/matlab-mcp-core-server (178 stars) lets AI agents run MATLAB code, generate scripts from natural language, and access documentation. It supports Claude Code, VS Code, GitHub Copilot, and Gemini CLI. Two community MATLAB servers add additional capabilities including script execution and Simulink integration. **R statistics is surprisingly mature** — finite-sample/rmcp (197 stars, Python, MIT) exposes 52 statistical analysis tools across 11 categories, drawing from 429 R packages via systematic CRAN task views. It covers econometrics, machine learning, time series, survival analysis, and more — production-ready with HTTP transport and SSE. Posit's mcptools lets AI assistants interact with live RStudio sessions. chi2labs/mcpr exposes arbitrary R functions through MCP. cafferychen777/Rstudio-mcp provides deep RStudio IDE integration. **Symbolic mathematics has multiple options** — sdiehl/sympy-mcp (41 stars) by Haskell author Stephen Diehl exposes SymPy's full computer algebra system for symbolic manipulation, equation solving, calculus, and simplification. huhabla/calculator-mcp-server combines SymPy + NumPy + SciPy for symbolic, numerical, and statistical computation in one server. tufantunc/axiom-advanced-math-mcp uses Giac/Xcas for high-precision symbolic math, differential equations, and financial time-series analysis. YuChenSSR/symbolica-mcp targets quantum computing workflows. **Wolfram ecosystem is well-represented** — paraporoco/Wolfram-MCP provides 11 tools for calculations, equation solving, calculus, matrix operations, and statistics via Wolfram Language. texra-ai/mcp-server-mathematica executes Mathematica code via wolframscript for derivation verification. rhenniger/MCPServer implements MCP in pure Wolfram Language. Five Wolfram Alpha API servers (StoneDot, akalaric, cnosuke, Garoth, SecretiveShell) provide computational knowledge access without a local installation. **Julia has a growing MCP ecosystem** — JuliaSMLM/ModelContextProtocol.jl implements the full MCP specification in Julia. samtalki/AgentREPL.jl provides a persistent REPL that eliminates compilation overhead (TTFX) by keeping the Julia process alive across interactions. jonathanfischer97/juliadoc-mcp serves Julia documentation to AI assistants. **HPC and research infrastructure** — globus-labs/science-mcps connects AI to supercomputing facilities (ALCF, NERSC) with Globus data transfer and function execution on remote endpoints. pathintegral-institute/mcp.science (117 stars) bundles 12+ servers including GPAW density-functional-theory calculations, Materials Project database queries, sandboxed Python execution, Jupyter kernel interaction, and SSH remote execution. **Engineering simulation** — two OpenFOAM MCP servers provide CFD integration: webworn/openfoam-mcp-server for educational use with Socratic AI, and ymg2007/openfoam-mcp for configuration management and wind-driven rain simulation. colesmcintosh/numpy-mcp provides NumPy numerical computing. **Notable gaps** — no SageMath MCP server, no dedicated SciPy MCP beyond calculator bundles, no Octave MCP (open-source MATLAB alternative), no Maple MCP, no COMSOL or ANSYS simulation servers, no dedicated linear algebra or optimization server (CPLEX, Gurobi, CVXPY). The category earns 3.5/5 — official vendor support from MathWorks is a strong signal, R and Julia have real ecosystems forming, and HPC access through Globus is genuinely novel. But most servers have low star counts, the symbolic math space is fragmented across many small projects, and major engineering simulation platforms are absent."
---

Scientific computing MCP servers let AI agents execute numerical code, solve equations symbolically, run statistical analyses, and submit jobs to supercomputers. Instead of manually writing MATLAB scripts, R commands, or Wolfram Language expressions, researchers can have AI assistants perform these computations through the Model Context Protocol.

This review covers MCP servers for **scientific computing and mathematics** — numerical analysis platforms (MATLAB, NumPy), symbolic math (SymPy, Wolfram, Mathematica), statistical computing (R), scientific programming languages (Julia), HPC infrastructure (Globus), and engineering simulation (OpenFOAM). For academic paper search and bioinformatics, see our [Science & Research review](/reviews/science-research-mcp-servers/). For 3D simulation and digital twins, see our [Digital Twins & 3D Simulation review](/reviews/digital-twins-3d-simulation-mcp-servers/).

The headline findings: **MathWorks ships an official MATLAB MCP server** (178 stars) — one of the few major scientific computing vendors to officially support MCP. **RMCP provides 52 R statistical tools** across 429 packages (197 stars) — the most comprehensive single-language scientific MCP server. **Globus Labs connects AI to supercomputers** at ALCF and NERSC. **mcp.science bundles 12+ research servers** under one project. **Symbolic math is fragmented** across many small SymPy and Wolfram wrappers.

## Numerical Computing Platforms

### matlab/matlab-mcp-core-server (Official MathWorks)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [matlab-mcp-core-server](https://github.com/matlab/matlab-mcp-core-server) | 178 | MATLAB | MathWorks License |

The **official MATLAB MCP server from MathWorks** — not a community wrapper, but built and maintained by the MATLAB team. Released October 2025, this is one of the strongest signals of MCP adoption in scientific computing.

### What Works Well

**Run MATLAB through AI agents.** Execute MATLAB code directly in conversations, generate scripts from natural language descriptions, and access MATLAB documentation — all through the standard MCP protocol.

**Broad client support.** Works with Claude Code, Visual Studio Code, GitHub Copilot, and Gemini CLI. MathWorks explicitly tests against multiple MCP clients, which is unusual attention to interoperability.

**Simulink integration.** Blog posts from MathWorks demonstrate simulating Simulink models through GitHub Copilot via the MCP server — meaning AI agents can interact with complex simulation workflows, not just script execution.

**MathWorks also ships an MCP client.** MATLAB can act as both MCP server (exposing MATLAB to AI) and MCP client (connecting MATLAB to other MCP servers). This bidirectional approach is rare in the MCP ecosystem.

### What Doesn't Work Well

**Requires MATLAB license.** The server needs a local MATLAB installation, which means a commercial license. This limits accessibility compared to open-source alternatives.

**Not open source.** Released under MathWorks' proprietary license, not MIT or Apache-2.0. You can inspect the code on GitHub but can't fork and modify freely.

### Community MATLAB Servers

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [WilliamCloudQi/matlab-mcp-server](https://github.com/WilliamCloudQi/matlab-mcp-server) | — | Python | — |
| [Tsuchijo/matlab-mcp](https://github.com/Tsuchijo/matlab-mcp) | — | Python | — |

Two community alternatives: **WilliamCloudQi's version** provides scientific computing and data analysis with natural language script generation. **Tsuchijo's version** focuses on letting LLMs write and execute MATLAB scripts. Both require a local MATLAB installation but offer MIT-style openness.

## Statistical Computing (R)

### finite-sample/rmcp (Most Comprehensive)

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [rmcp](https://github.com/finite-sample/rmcp) | 197 | Python | MIT | 52 |

The **most comprehensive single-language scientific MCP server** we've found. RMCP exposes 52 statistical analysis tools across 11 categories, systematically drawing from 429 R packages via CRAN task views:

- **Econometrics** — regression, instrumental variables, panel data
- **Machine learning** — classification, clustering, ensemble methods
- **Time series** — ARIMA, state-space models, forecasting
- **Survival analysis** — Kaplan-Meier, Cox proportional hazards
- **Bayesian statistics** — MCMC, hierarchical models
- **Spatial statistics** — geostatistics, point patterns

Production-ready with full MCP protocol compliance, HTTP transport and SSE support, stdio mode for Claude Desktop, and a publicly available test server. At 197 stars, it's the most starred R MCP server.

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
| [sympy-mcp](https://github.com/sdiehl/sympy-mcp) | 41 | Python | — |

Built by Stephen Diehl (known for Haskell work), this server exposes **SymPy's full computer algebra system** — symbolic manipulation, equation solving, calculus (integration, differentiation), simplification, factoring, expansion. The most focused and well-maintained SymPy MCP server.

### huhabla/calculator-mcp-server (Multi-Library)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [calculator-mcp-server](https://github.com/huhabla/calculator-mcp-server) | — | Python | — |

Combines **three Python scientific libraries in one server**: SymPy for symbolic math, NumPy for numerical computation, and SciPy for statistical analysis. Includes matrix operations. A good choice if you want one server instead of three.

### tufantunc/axiom-advanced-math-mcp

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [axiom-advanced-math-mcp](https://github.com/tufantunc/axiom-advanced-math-mcp) | — | TypeScript | — |

**High-precision symbolic math** powered by Giac/Xcas (the CAS behind HP Prime calculators) and mathjs. Covers differential equations, symbolic mathematics, and financial time-series analysis. The Giac backend provides arbitrary-precision arithmetic that SymPy-based servers typically don't offer.

### Other Math Servers

| Server | Description |
|--------|-------------|
| [EthanHenrickson/math-mcp](https://github.com/EthanHenrickson/math-mcp) | Basic math and statistics for LLMs |
| [SHSharkar/MCP-Mathematics](https://github.com/SHSharkar/MCP-Mathematics) | 52 functions, 158 unit conversions, financial calculations |
| [edwardpwtsoi/mathjs-mcp](https://github.com/edwardpwtsoi/mathjs-mcp) | mathjs wrapper |
| [colesmcintosh/numpy-mcp](https://github.com/colesmcintosh/numpy-mcp) | NumPy numerical computing via MCP |
| [YuChenSSR/symbolica-mcp](https://github.com/YuChenSSR/symbolica-mcp) | Symbolic computing for quantum computing workflows |

## Wolfram Ecosystem

### paraporoco/Wolfram-MCP

| Server | Stars | Language | License | Tools |
|--------|-------|----------|---------|-------|
| [Wolfram-MCP](https://github.com/paraporoco/Wolfram-MCP) | 6 | Python | MIT | 11 |

The most complete **Wolfram Language MCP server** — 11 tools covering the core symbolic math workflow:

- `calculate`, `solve`, `integrate`, `differentiate`
- `simplify`, `factor`, `expand`
- `matrix_operations`, `statistics`
- `execute` — arbitrary Wolfram Language code

Requires a local Wolfram Mathematica installation. Built with FastMCP.

### texra-ai/mcp-server-mathematica

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [mcp-server-mathematica](https://github.com/texra-ai/mcp-server-mathematica) | — | — | — |

Executes **Mathematica code via wolframscript** — designed for verification workflows where you want to double-check mathematical derivations. Requires Mathematica or the free Wolfram Engine for Developers.

### rhenniger/MCPServer

| Server | Stars | Language |
|--------|-------|----------|
| [MCPServer](https://github.com/rhenniger/MCPServer) | — | Wolfram Language |

An MCP server **written in pure Wolfram Language** — implements the protocol natively without Python or TypeScript intermediaries. Interesting architecturally, but limited adoption.

### Wolfram Alpha API Servers

| Server | Language | Notes |
|--------|----------|-------|
| [StoneDot/wolframalpha-mcp-server](https://github.com/StoneDot/wolframalpha-mcp-server) | TypeScript | Wolfram Alpha LLM API |
| [akalaric/mcp-wolframalpha](https://github.com/akalaric/mcp-wolframalpha) | Python | Full client + server |
| [cnosuke/mcp-wolfram-alpha](https://github.com/cnosuke/mcp-wolfram-alpha) | Go | Lightweight |
| [Garoth/wolframalpha-llm-mcp](https://github.com/Garoth/wolframalpha-llm-mcp) | — | Structured knowledge |
| [SecretiveShell/MCP-wolfram-alpha](https://github.com/SecretiveShell/MCP-wolfram-alpha) | — | Chat REPL integration |
| [benhaotang/mcp-mma-docs](https://github.com/benhaotang/mcp-mma-docs) | — | Mathematica docs only |

Five+ servers wrapping the **Wolfram Alpha API** — these don't require a local Mathematica installation, just an API key. They provide computational knowledge (math, science, conversions, data) through Wolfram Alpha's cloud service. The fragmentation is notable: none has emerged as the clear winner.

## Julia

### JuliaSMLM/ModelContextProtocol.jl

| Server | Language | License |
|--------|----------|---------|
| [ModelContextProtocol.jl](https://github.com/JuliaSMLM/ModelContextProtocol.jl) | Julia | — |

A **full MCP specification implementation in Julia** — not just a wrapper, but a proper Julia package for creating and configuring MCP servers. `mcp_server()` is the main entry point. Useful for Julia developers who want to expose their own tools via MCP.

### samtalki/AgentREPL.jl (Persistent REPL)

| Server | Language |
|--------|----------|
| [AgentREPL.jl](https://github.com/samtalki/AgentREPL.jl) | Julia |

Solves Julia's **time-to-first-execution (TTFX) problem** for AI workflows. The Julia process stays alive across interactions, so you only pay the compilation cost once. Provides persistent REPL sessions via MCP STDIO transport — meaning AI agents can build on previous computations within the same session.

### Other Julia Servers

| Server | Description |
|--------|-------------|
| [JuliaBench/ClaudeMCPTools.jl](https://github.com/JuliaBench/ClaudeMCPTools.jl) | Basic MCP tools for Claude |
| [jonathanfischer97/juliadoc-mcp](https://github.com/jonathanfischer97/juliadoc-mcp) | Julia documentation server |

## HPC & Research Infrastructure

### globus-labs/science-mcps (Supercomputing Access)

| Server | Language | License |
|--------|----------|---------|
| [science-mcps](https://github.com/globus-labs/science-mcps) | Python | — |

From **Globus Labs** (University of Chicago / Argonne National Laboratory), this project connects AI agents to **national supercomputing facilities**:

- **Globus Transfer** — move data between Globus endpoints, browse remote directories, manage transfer tasks
- **Globus Compute** — register and execute Python functions on remote HPC endpoints (Polaris, etc.)
- **Globus Search** — create indices and search across Globus Search indexes
- **ALCF MCP** — interact with Argonne Leadership Computing Facility
- **NERSC MCP** — interact with the National Energy Research Scientific Computing Center
- **Diaspora MCP** — Diaspora Event Fabric for topic management and event streaming

A published paper ([arXiv:2508.18489](https://arxiv.org/pdf/2508.18489)) demonstrates the approach: an AI agent used Globus Compute MCP to write quantum chemistry functions, execute them on Polaris, and generate HOMO-LUMO gap visualizations consistent with published literature.

### pathintegral-institute/mcp.science (Research Hub)

| Server | Stars | Language | License |
|--------|-------|----------|---------|
| [mcp.science](https://github.com/pathintegral-institute/mcp.science) | 117 | Python | MIT |

Bundles **12+ specialized MCP servers** for scientific research under one umbrella. Install any server with `uvx mcp-science <name>`. Includes:

- **GPAW DFT** — density-functional-theory calculations
- **Materials Project** — query the Materials Project database (requires API key)
- **Python sandbox** — sandboxed code execution
- **Jupyter** — interact with Jupyter kernels
- **Mathematica** — Wolfram Language integration
- **SSH** — remote command execution
- **Web fetch** — HTML/PDF/text processing
- **Academic search** — multi-source paper search

Already covered in our [Science & Research review](/reviews/science-research-mcp-servers/), but its scientific computing components (DFT, Materials Project, sandboxed execution) are directly relevant here.

## Engineering Simulation

### OpenFOAM MCP Servers

| Server | Description |
|--------|-------------|
| [webworn/openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server) | CFD education with Socratic AI, mesh generation, turbulence models |
| [ymg2007/openfoam-mcp](https://github.com/ymg2007/openfoam-mcp) | Config management, cross-platform, wind-driven rain simulation |

Two MCP servers for **OpenFOAM**, the open-source computational fluid dynamics (CFD) toolkit. **webworn's version** is education-focused — it uses Socratic questioning and expert error resolution to teach CFD concepts. Covers OpenFOAM 12 with blockMesh mesh generation and k-ε/k-ω SST turbulence models. **ymg2007's version** is practical — read and modify OpenFOAM configuration files via MCP, with specialized tools for wind-driven rain simulation.

## What's Missing

**No SageMath MCP server.** SageMath wraps dozens of open-source math packages (SymPy, R, Maxima, GAP, FLINT) under one interface. An MCP server would be the single widest gateway to mathematical computing.

**No Octave MCP server.** GNU Octave is the open-source MATLAB alternative. Given MATLAB's commercial license requirement, an Octave MCP server would democratize access to MATLAB-compatible computing.

**No dedicated SciPy MCP.** SciPy appears bundled in calculator servers but has no standalone MCP server exposing its optimization, signal processing, and linear algebra capabilities.

**No Maple MCP server.** Maple is widely used in education and engineering for symbolic math.

**No engineering simulation giants.** COMSOL, ANSYS, ABAQUS, and other FEA/FEM platforms have no MCP servers. Given MathWorks' official support, other engineering software vendors may follow.

**No optimization solvers.** No CPLEX, Gurobi, or CVXPY MCP servers for mathematical optimization — a major gap for operations research and engineering design.

## The Verdict

**Rating: 3.5 / 5** — Strong vendor signal, real ecosystems forming, but fragmented and mostly low-traffic.

The scientific computing MCP landscape has two standout features. First, **official vendor support from MathWorks** — the MATLAB MCP server at 178 stars is one of the most significant endorsements of MCP from a scientific computing company. Second, **R's RMCP server is genuinely comprehensive** — 52 tools across 429 packages is production-grade statistical computing, not a toy wrapper.

The **Julia ecosystem** is also doing things right. ModelContextProtocol.jl implements the full spec natively, and AgentREPL.jl solves a real problem (TTFX) in a language-appropriate way. These are small projects but architecturally sound.

**Globus Labs' HPC access** is the most novel contribution — no other MCP category lets you submit jobs to national supercomputers. The published paper demonstrating quantum chemistry computations on Polaris validates the approach.

The 3.5 rating reflects fragmentation more than quality. **Symbolic math has too many small servers** — at least 15 SymPy and Wolfram wrappers, none above 41 stars, with no clear winner. The Wolfram Alpha API alone has five nearly identical MCP servers. **Engineering simulation is almost empty** — only OpenFOAM has MCP servers, while COMSOL, ANSYS, and other industry workhorses are absent. And **star counts are low across the board** — even the MATLAB official server has only 178 stars, suggesting the research computing community hasn't fully discovered MCP yet.

For researchers: start with the **official MATLAB server** if you have a license, **RMCP** for statistics, or **mcp.science** for multi-tool scientific workflows. For symbolic math, **sdiehl/sympy-mcp** is the cleanest option. For HPC, **Globus Labs' science-mcps** is the only game in town — and it's a good one.

*Last updated: March 19, 2026. Star counts and features reflect what we found during research. We do not install or test these servers hands-on — our reviews are based on documentation, source code analysis, GitHub activity, and community feedback. See our [methodology note](/reviews/#methodology) for details.*
