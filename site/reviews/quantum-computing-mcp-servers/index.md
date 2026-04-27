# Quantum Computing MCP Servers — IBM Qiskit, Conductor Quantum CODA, Amazon Braket, Stim QEC, and More

> Quantum computing MCP servers reviewed: IBM Qiskit official (6 servers, Apache 2.0, circuit creation+transpilation+runtime+docs+code assistant+gym), Conductor Quantum CODA MCP (commercial, multi-provider QPU access IBM+IonQ+Rigetti+IQM+AQT 1000+ qubits, cross-framework Qiskit+Cirq+PennyLane+Braket+CUDA-Q, $19-279/mo), Amazon Braket MCP (2 stars, Apache 2.0, Bell+GHZ+QFT pre-built), SpinQ (official vendor MCP for SpinQ Cloud hardware), quantum-simulator-mcp (10 stars, MIT, Docker, noise models depolarizing+thermal+readout, OpenQASM 2.0), Stim MCP (8 tools QEC surface+repetition+color codes error analysis), QML-MCP (quantum ML VQC+kernels Qiskit), QuantumArchitect-MCP (validation+scoring hardware profiles IBM+Rigetti+IonQ), Psi-MCP (QuTiP+OpenFermion 30 qubits circuits+chemistry+many-body+algorithms), IBM Quantum MCP (VQE molecular energy H2+HeH+ Heron R2 156 qubits), qsim-mcp (Stanford hackathon Qiskit Metal+OpenEMS EM simulation archived), post-quantum cryptography MCP (24 tools ML-KEM+ML-DSA+SLH-DSA NIST FIPS 203/204/205), QU3 quantum-safe MCP client (43 stars Kyber-768+SPHINCS+). Academic: arXiv 2604.08318 MCP for hybrid quantum-HPC. Rating: 3.0/5.


Quantum computing MCP servers connect AI assistants to quantum circuit design, simulation, and real quantum hardware execution. Instead of manually writing Qiskit or Cirq code, these servers let AI agents create circuits, transpile them for specific hardware, run simulations with noise models, submit jobs to quantum processors, and analyze results — all through the Model Context Protocol.

The landscape spans five areas: **circuit design & execution** (IBM Qiskit, Conductor Quantum CODA, Amazon Braket), **simulation & noise modeling** (quantum-simulator-mcp, Stim), **quantum machine learning** (QML-MCP, Psi-MCP), **quantum hardware design** (qsim-mcp for Qiskit Metal), and **post-quantum cryptography** (quantum-safe communication tools). A related but distinct concern — **post-quantum security for MCP itself** — is also emerging as quantum threats to classical encryption grow.

The headline findings: **IBM is the only major vendor with official MCP servers** — six Qiskit MCP servers covering circuit creation through hardware execution. **Conductor Quantum's CODA MCP is the most capable multi-provider platform** — access to IBM, IonQ, Rigetti, IQM, and AQT hardware (1,000+ qubits) through a single MCP interface, with cross-framework transpilation across Qiskit, Cirq, PennyLane, Braket, and CUDA-Q. **Academic research validates the approach** — arXiv paper 2604.08318 formalizes MCP server architecture for hybrid quantum-HPC environments. **The biggest gaps are vendor participation** — Google Quantum AI, Xanadu, Microsoft Azure Quantum, D-Wave, and Quantinuum have no official MCP servers. **Post-quantum cryptography is a separate but growing MCP concern** — both for securing MCP communications against future quantum attacks and for providing quantum-resistant crypto tools to AI agents.

**Category:** [Science & Research](/categories/science-research/)

## Circuit Design & Execution

### IBM Qiskit (Official)

| Server | Auth | Tools | Official |
|--------|------|-------|----------|
| [Qiskit MCP Server](https://github.com/Qiskit/mcp-servers) | None | Core circuits | Yes |
| [Qiskit Code Assistant](https://github.com/Qiskit/mcp-servers) | IBM Quantum token | Code completion | Yes |
| [Qiskit Runtime](https://github.com/Qiskit/mcp-servers) | IBM Quantum token | Job submission | Yes |
| [Qiskit IBM Transpiler](https://github.com/Qiskit/mcp-servers) | IBM Quantum token | AI optimization | Yes |
| [Qiskit Docs](https://github.com/Qiskit/mcp-servers) | None | Doc search | Yes |
| [Qiskit Gym](https://github.com/Qiskit/mcp-servers) | None | RL synthesis | Community |

**IBM is the only major quantum computing vendor with official MCP server support.** The [Qiskit/mcp-servers](https://github.com/Qiskit/mcp-servers) repository (26 stars, Apache 2.0, Python) contains **six MCP servers** — five official from IBM and one community contribution — covering the full quantum development workflow.

**Qiskit MCP Server** provides core circuit creation, manipulation, transpilation, and serialization (OpenQASM 3 and QPY formats) for local development. No authentication required. **Qiskit Code Assistant** delivers AI-powered quantum code completion integrated with MCP clients (requires IBM Quantum Premium Plan). **Qiskit Runtime** connects to IBM Quantum cloud services for backend discovery and job submission to real hardware. **Qiskit IBM Transpiler** offers AI-powered circuit optimization using advanced routing and optimization algorithms. **Qiskit Docs** provides searchable access to the complete Qiskit documentation ecosystem — the only server requiring no authentication at all.

The community-contributed **Qiskit Gym** adds reinforcement learning-based quantum circuit synthesis — an unusual but interesting addition to the official repository.

All servers are built on the **FastMCP** framework with async-first design, each distributed as an independent PyPI package. Python 3.10+ required (3.11+ recommended). Registered in the MCP Registry for automatic discovery. 749 commits indicate active, ongoing development.

**Separate unofficial implementation:** [barvhaim/qiskit-mcp-server](https://github.com/barvhaim/qiskit-mcp-server) (6 stars, Python) provides 13 tools — 8 core (circuit creation, gate operations, execution, visualization) and 6 advanced (state analysis, density matrix, optimization, variational circuits, QFT). Predates the official servers and takes a more interactive approach, translating natural language into gate sequences.

### Conductor Quantum — CODA MCP

| Feature | Detail |
|---------|--------|
| Provider | [Conductor Quantum](https://www.conductorquantum.com/coda) |
| QPU Access | IBM, IonQ (Aria/Forte), Rigetti (Ankaa-3), IQM (Garnet/Emerald), AQT (IBEX Q1) |
| Frameworks | Qiskit, Cirq, PennyLane, Braket, CUDA-Q, PyQuil, OpenQASM |
| Pricing | Free (5 daily credits) / Pro $19/mo / Ultra $279/mo / Enterprise custom |
| Transport | stdio (MCP clients) + web chat |

**CODA MCP** is the most capable quantum computing MCP server available — a commercial platform providing **multi-provider QPU access** (1,000+ qubits across 5 hardware vendors) and **cross-framework transpilation** (7 quantum frameworks) through a single MCP interface.

The workflow: generate or import a circuit → transpile to the target framework → simulate locally (up to 34 qubits via NVIDIA cuQuantum) → execute on real QPU hardware → retrieve and analyze results. Additional tools include resource estimation (qubit count, depth, gate counts), circuit splitting for distributed execution, OpenQASM 3 export, and quantum paper search/retrieval.

**Pricing is credit-based** — 1 credit = $1.00 in quantum compute value. Free tier gets 5 daily credits (reset at midnight UTC). QPU costs vary: IonQ $0.30 base + $0.03/shot, Rigetti $0.30 + $0.09/shot, IQM $0.30 + $0.01/shot, AQT $0.30 + $0.02/shot. Simulators are free. Paid plan credits never expire and roll over monthly.

Works with Claude Desktop, Claude Code, VS Code, Cursor, Zed, and any MCP client supporting stdio transport. Also accessible via web chat at coda.conductorquantum.com.

### Amazon Braket MCP

| Server | Stars | License | Language | Tools |
|--------|-------|---------|----------|-------|
| [petertilsen/amazon-braket-mcp-server](https://github.com/petertilsen/amazon-braket-mcp-server) | 2 | Apache 2.0 | Python | 10+ |

Community-built MCP server for **Amazon Braket** — AWS's quantum computing service. Provides circuit creation with gate operations (Hadamard, Pauli X/Y/Z, controlled gates, rotations, phase), pre-built algorithms (Bell pairs, GHZ states, Quantum Fourier Transform), multi-device support (simulators and real hardware), task execution with configurable shot counts, and result retrieval with measurement analysis. Compatible with **Amazon Q CLI** for natural language quantum interactions. Not officially supported by AWS but follows AWS MCP server architectural patterns. Results stored in S3.

**Separate wrapper:** [dougdotcon/QuantMCP](https://github.com/dougdotcon/QuantMCP) provides another Amazon Braket MCP integration focused on the intersection of AI and quantum processing.

### SpinQ Cloud MCP

| Server | Stars | License | Language |
|--------|-------|---------|----------|
| [SpinQTech/spinqit_mcp_tools](https://github.com/SpinQTech/spinqit_mcp_tools) | 2 | MIT | Python |

**SpinQ Technology** — a Chinese quantum computing company founded in 2018 specializing in superconducting and NMR quantum computers — provides an **official vendor MCP server** for their SpinQ Cloud platform. Submit quantum circuits in QASM format to real SpinQ hardware. Authentication via private key + username credentials. One-click installation scripts for Windows and macOS. Python 3.10+ required.

SpinQ raised several hundred million RMB in Series B funding (July 2025), indicating serious investment backing. The MCP server is minimal (2 stars, early-stage) but notable as one of only two quantum hardware vendors (alongside IBM) shipping official MCP support.

## Simulation & Error Correction

### Quantum Simulator MCP

| Server | Stars | License | Language | Tools |
|--------|-------|---------|----------|-------|
| [YuChenSSR/quantum-simulator-mcp](https://github.com/YuChenSSR/quantum-simulator-mcp) | 10 | MIT | Python | 5 |

The most popular standalone quantum simulator MCP server. **Docker-based** (supporting amd64 and arm64), providing circuit simulation with **realistic noise models** — depolarizing, thermal relaxation, and readout error — via the Qiskit backend. Accepts **OpenQASM 2.0** circuits.

Key features: result visualization through histogram generation, pre-loaded example circuits (Bell state, Grover's algorithm, Quantum Fourier Transform), cross-platform Docker deployment. Designed for integration with Claude Desktop and other MCP clients.

### Stim MCP (Quantum Error Correction)

| Server | Stars | License | Language | Tools |
|--------|-------|---------|----------|-------|
| [DeDuckProject/stim-mcp](https://github.com/DeDuckProject/stim-mcp) | 0 | — | Python | 8 |

Wraps **Google's Stim** — a high-performance quantum stabilizer circuit simulator — for MCP access. The niche here is **quantum error correction (QEC)**, which is critical for building fault-tolerant quantum computers.

Eight tools: `create_circuit` (validate and open sessions), `append_operation` (add Stim instructions), `sample_circuit` (simulate with measurement statistics), `analyze_errors` (build Detector Error Model, find shortest logical error paths), `inject_noise` (add depolarizing or X error noise), `get_circuit_diagram` (ASCII/SVG/timeline), `generate_circuit` (pre-built surface codes, repetition codes, color codes), and `hello_quantum` (health check).

v0.1.5 released April 2026, 44 commits. Experimental/beta. An important niche — QEC is the main bottleneck for practical quantum computing, and having AI agents that can design and analyze error correction codes is a genuine research use case.

### IBM Quantum VQE MCP

| Server | Stars | License | Language |
|--------|-------|---------|----------|
| [aaronsb/ibm-quantum-mcp](https://github.com/aaronsb/ibm-quantum-mcp) | 3 | MIT | Python |

Specialized MCP server for **Variational Quantum Eigensolver (VQE)** experiments — computing molecular ground-state energies on quantum hardware. Two servers: one for local simulation, one for real IBM Quantum processors.

Supports H₂ and HeH⁺ molecules with real-time convergence tracking and matplotlib visualizations. Accesses IBM's **Heron R2** processors (156 qubits) with built-in error mitigation and transpilation optimization. Example result: H₂ energy calculation at -1.728 Hartree on real hardware. A proof-of-concept demonstrating "how to make quantum computing accessible through conversational AI."

## Quantum Machine Learning

### QML-MCP

| Server | Stars | License | Language | Tools |
|--------|-------|---------|----------|-------|
| [des137/qml-mcp](https://github.com/des137/qml-mcp) | 0 | MIT | Python | 5 |

Quantum machine learning via Qiskit: **quantum circuit execution** with configurable shots, **quantum kernel computation** using ZZ feature maps, **Variational Quantum Classifier (VQC)** training, and **model evaluation** with accuracy metrics. Configurable safety limits on qubits (default 10) and shots (default 100,000). Uses Qiskit 1.4.5+ (Qiskit Machine Learning 0.8.4 requires Qiskit 1.x). Python 3.10+, MIT license, 7 commits.

### Psi-MCP (Advanced Quantum Systems)

| Server | Stars | License | Language |
|--------|-------|---------|----------|
| [manasp21/Psi-MCP](https://github.com/manasp21/Psi-MCP) | 0 | MIT | Python |

The most ambitious quantum MCP server in scope — covers **quantum circuits** (creation, simulation, optimization across Qiskit/Cirq/PennyLane backends), **open quantum systems** (master equation solving, decoherence analysis via QuTiP), **quantum chemistry** (molecular Hamiltonians, VQE, electronic structure via OpenFermion), **many-body physics** (DMRG simulations up to 100 sites, phase transitions), **quantum algorithms** (Shor's factoring, Grover search, VQE optimization), **quantum ML** (quantum neural networks, variational classifiers), and **visualization** (Bloch spheres, density matrices, Wigner functions).

Supports circuits up to 30 qubits (simulator dependent), molecular systems up to 20 orbitals with VQE, ML training up to 1,000 samples. Built on FastAPI, Python 3.11+, deployable via Docker or Smithery CLI. Impressive scope but 0 stars and 3 commits suggest early-stage development.

### QuantumArchitect-MCP

| Server | Stars | License | Language |
|--------|-------|---------|----------|
| [NLarchive/QuantumArchitect-MCP](https://github.com/NLarchive/QuantumArchitect-MCP) | 0 | MIT | Python |

Quantum circuit **validation and scoring** tool — generates circuits (Bell States, GHZ, QFT, Grover's, VQE Ansatz), validates them (syntax checking, hardware topology compatibility, unitarity verification), runs statevector simulation with noise estimation, and scores circuits on complexity metrics, expressibility, and **hardware fitness** for IBM, Rigetti, and IonQ topologies. Gradio web interface. 11 commits. Runs on Hugging Face Spaces.

## Quantum Hardware Design

### qsim-mcp (Stanford Hackathon)

| Server | Stars | License | Language |
|--------|-------|---------|----------|
| [PaulGoldschmidt/qsim-mcp](https://github.com/PaulGoldschmidt/qsim-mcp) | 4 | MIT | Python |

Built by Team Silicon Architects at the **Stanford MCP × Quantum Science Hackathon 2025**. A dual MCP server system for quantum hardware design: one server handles **quantum circuit design** via Qiskit Metal (transmon qubit creation, coupler design, CPW routing), while the other runs **electromagnetic simulation** via Octave/OpenEMS (S-parameter extraction, impedance verification, multi-format export). 25+ tools across both servers. GDS file export for fabrication.

**Repository archived** April 13, 2026 (read-only). 42 commits. Notable as the only MCP server targeting quantum hardware/chip design rather than circuit programming — a unique niche bridging AI agents with quantum device engineering.

## Post-Quantum Cryptography

### Post-Quantum MCP Server

| Server | Stars | License | Language | Tools |
|--------|-------|---------|----------|-------|
| [scottdhughes/post-quantum-mcp](https://github.com/scottdhughes/post-quantum-mcp) | 1 | MIT | Python | 24 |

Implements **NIST-standardized post-quantum cryptographic algorithms** as MCP tools — enabling AI agents to perform quantum-resistant key generation, encryption, signing, and verification. **24 tools** covering:

- **ML-KEM** (FIPS 203) — key encapsulation mechanism
- **ML-DSA** (FIPS 204) — digital signatures (ML-DSA-65)
- **SLH-DSA / SPHINCS+** (FIPS 205) — stateless hash-based signatures
- **Hybrid key exchange** — X25519 + ML-KEM-768 combined
- **Sealed-envelope encryption** — anonymous and authenticated modes
- **Signature replay protection** with configurable TTL
- **Security analysis and algorithm benchmarking**

115 commits — the most active community quantum MCP server by commit count. Built on **liboqs** (Open Quantum Safe library). Supports Falcon and additional KEMs via liboqs extensions. Session-scoped key handle management with optional secret redaction.

### QU3 — Quantum-Safe MCP Client

| Server | Stars | License | Language |
|--------|-------|---------|----------|
| [qu3ai/qu3-app](https://github.com/qu3ai/qu3-app) | 43 | — | Python |

The highest-starred project in the quantum MCP space (43 stars) — but it's a **client**, not a server. Provides quantum-safe communication for MCP interactions using **Kyber-768 KEM** (key encapsulation) and **SPHINCS+** (digital signatures) with **AES-256-GCM** encrypted payloads. Establishes secure sessions via KEM handshake, encrypts all request/response traffic, and verifies digital signatures. CLI commands for key generation, inference requests, agent workflows, and policy updates. Includes mock FastAPI server for testing.

Notable as the first project to address **securing MCP communications themselves** against future quantum computer attacks — a "harvest now, decrypt later" defense.

## Academic Research

The intersection of quantum computing and MCP has attracted formal academic attention:

**"A Model Context Protocol Server for Quantum Execution in Hybrid Quantum-HPC Environments"** ([arXiv 2604.08318](https://arxiv.org/abs/2604.08318), April 2026) — presents an MCP server architecture enabling LLM agents to autonomously execute quantum computing workflows. Key contributions: an MCP server for quantum execution, a pipeline for interpreting OpenQASM code, automated workflow integration with **CUDA-Q** for the **ABCI-Q** hybrid quantum-HPC platform (Japan), and asynchronous execution via the **Quantinuum** emulator. Funded by Japan's Council for Science, Technology and Innovation (CSTI) and NEDO.

**Post-Quantum Cryptographic Agility in MCP Proxies** (Gopher Security, April 2026) — a comprehensive framework for securing MCP infrastructure against quantum threats. Four pillars: Discovery (find all MCP connections), Defense (quantum-resistant tunnels), Detection (handshake anomalies), Deployment (hybrid environments). Proposes running "double wrap" — classical RSA alongside ML-KEM for fallback security.

## What's Missing

The quantum computing MCP ecosystem has significant gaps:

- **Google Quantum AI** — no official Cirq or Google quantum hardware MCP server, despite Cirq being one of the top quantum frameworks
- **Xanadu / PennyLane** — no official MCP server from Xanadu, though PennyLane is supported as a target framework in CODA MCP
- **Microsoft Azure Quantum** — no official MCP integration, despite Azure Quantum offering access to IonQ, Quantinuum, and Rigetti hardware
- **D-Wave** — no quantum annealing MCP server (D-Wave's approach differs fundamentally from gate-based quantum computing)
- **Quantinuum (H-Series)** — no direct MCP access to their trapped-ion processors (though CODA MCP and the arXiv paper use Quantinuum emulators)
- **IonQ, Rigetti** — no vendor-built MCP servers (accessible only through CODA MCP)
- **Quantum chemistry workflows** — limited to VQE; no servers for quantum dynamics, quantum Monte Carlo, or tensor network methods
- **Educational tools** — no MCP servers specifically designed for teaching quantum computing concepts to beginners
- **Quantum cloud cost management** — no tools for estimating and tracking QPU spending across providers

## Rating: 3.0 / 5

The quantum computing MCP ecosystem is **small but technically deep**. IBM's commitment is genuine — six official servers covering the full Qiskit workflow is the strongest vendor investment in any niche scientific computing category. Conductor Quantum's CODA MCP provides real multi-provider hardware access with a practical credit-based pricing model. The academic paper validates that MCP is being taken seriously as infrastructure for quantum-HPC integration.

But the category is clearly **early-stage**: most community servers have 0-10 stars, only two hardware vendors (IBM, SpinQ) ship official MCP support, and the target audience is quantum researchers rather than general developers. The absence of Google, Xanadu, Microsoft, D-Wave, and Quantinuum from the MCP ecosystem is the most significant gap — without these vendors, the ecosystem remains IBM-centric. Post-quantum cryptography is an important adjacent concern that's beginning to get MCP tooling, but it's a security category rather than a quantum computing category proper.

**Bottom line:** If you're already working with IBM Quantum or need multi-provider QPU access, the MCP tooling exists and works. If you're on any other quantum platform, you're waiting for vendor support or using CODA MCP as an intermediary. The category will likely grow as quantum computing matures and more vendors recognize MCP as a standard integration layer.

