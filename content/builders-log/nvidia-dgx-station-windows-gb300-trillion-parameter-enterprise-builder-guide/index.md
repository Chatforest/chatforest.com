---
title: "NVIDIA DGX Station for Windows: Trillion-Parameter AI on Your Desk — Enterprise Builder Guide"
date: 2026-06-05
description: "NVIDIA announced DGX Station for Windows at COMPUTEX 2026 — a GB300 Grace Blackwell deskside supercomputer that runs 1-trillion-parameter AI models locally on Windows. Q4 2026 availability. Here's what enterprise builders need to know about the hardware, software stack, and when to choose it over cloud."
og_description: "NVIDIA DGX Station for Windows: 748GB coherent memory, 20 petaflops FP4, runs up to 1T parameter models locally on Windows. Built with Microsoft. NIM containers work unchanged on DGX Station and Azure. Q4 2026 from Dell, HP, ASUS, MSI, GIGABYTE, Supermicro. Builder guide to the hardware, software stack, and on-prem vs. cloud decision."
content_type: "Builder's Log"
categories: ["AI Infrastructure", "Hardware", "Enterprise AI"]
tags: ["nvidia", "dgx-station", "windows", "gb300", "grace-blackwell", "on-prem", "enterprise", "local-ai", "nim", "computex-2026", "inference", "builders-log"]
sources_audited: 2026-07-29
---

[NVIDIA announced DGX Station for Windows](https://nvidianews.nvidia.com/news/nvidia-dgx-station-for-windows-puts-a-trillion-parameter-ai-supercomputer-on-every-enterprise-desk) on June 1, 2026, at COMPUTEX in Taipei. It is a deskside AI supercomputer powered by the GB300 Grace Blackwell Ultra Desktop Superchip, capable of running AI models up to one trillion parameters locally on Windows. [Q4 2026 availability from six OEM partners](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-DGX-Station-for-Windows-Puts-a-Trillion-Parameter-AI-Supercomputer-on-Every-Enterprise-Desk/default.aspx).

The premise is straightforward: enterprise AI workloads have historically required Linux datacenter hardware, while [Windows holds roughly 64% of global desktop OS share](https://www.statista.com/statistics/218089/global-market-share-of-windows-7/) and dominates corporate desktop fleets. DGX Station closes that gap.

---

## Hardware Specifications

Specs below are drawn from [NVIDIA's product page](https://www.nvidia.com/en-us/products/workstations/dgx-station/) and the [DGX Station for Windows announcement](https://nvidianews.nvidia.com/news/nvidia-dgx-station-for-windows-puts-a-trillion-parameter-ai-supercomputer-on-every-enterprise-desk).

| Component | Spec |
|---|---|
| **Chip** | GB300 Grace Blackwell Ultra Desktop Superchip |
| **Architecture** | Blackwell Ultra GPU + 72-core Grace CPU, NVLink-C2C interconnect |
| **Memory** | Up to 748 GB coherent unified memory (252 GB HBM3e GPU memory + 496 GB LPDDR5X CPU memory) |
| **AI Compute** | Up to 20 petaflops FP4 |
| **Networking** | NVIDIA ConnectX-8 SuperNIC, up to 800 Gb/s |
| **Optional GPU** | RTX PRO 6000 Blackwell Workstation GPU (adds ray-traced visualization and physical simulation) |
| **OS** | Windows 11, with Windows Subsystem for Linux (WSL) for Linux-based AI containers |
| **Availability** | Q4 2026 |
| **OEMs** | ASUS, Dell Technologies, GIGABYTE, HP, MSI, Supermicro |

The coherent memory design is the key hardware fact for builders. 748 GB of unified CPU/GPU memory means large models do not page between separate memory pools. [Llama 3.1 405B](https://ai.meta.com/blog/meta-llama-3-1/) in FP16 requires roughly 810 GB (405 billion parameters × 2 bytes) — at FP8 or FP4 quantization it fits in the 748 GB pool with room for KV cache. Models in the 70B to 405B range run comfortably at full precision.

---

## What One Trillion Parameters Actually Means

"Up to 1 trillion parameters" is NVIDIA's headroom claim, not a model that currently exists in publicly available weights. Useful reference points:

| Model | Parameters | Fits in DGX Station? |
|---|---|---|
| Llama 3.1 8B | 8B | Yes, with large margin |
| Llama 3.1 70B | 70B | Yes, full FP16 |
| Llama 3.1 405B | 405B | Yes, FP8/FP4 quantization |
| [Nemotron 3 Ultra](https://developer.nvidia.com/blog/nvidia-nemotron-3-ultra-powers-faster-more-efficient-reasoning-for-long-running-agents/) | 550B total / 55B active (MoE) | Yes, MoE active weight fits easily |
| Hypothetical dense 1T | 1,000B | Yes, FP4 |

For most enterprise use cases, the practical ceiling is running Llama 3.1 405B, Nemotron 3 Ultra, or similar open frontier models locally without cloud egress.

---

## Software Stack

DGX Station for Windows was built in direct collaboration with Microsoft. The software integration matters as much as the hardware.

**NVIDIA AI Enterprise suite** — the full commercial software stack including CUDA, cuDNN, TensorRT, and RAPIDS, [licensed per NVIDIA's enterprise software terms](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/).

**NVIDIA NIM microservices** — pre-packaged inference containers for popular models. [NIM is built for portability](https://www.nvidia.com/en-us/ai-data-science/products/nim-microservices/): the same containers deploy unmodified across local NVIDIA hardware (including DGX systems), major clouds, and edge devices, and [NIM microservices are natively supported on Azure AI Foundry](https://developer.nvidia.com/blog/accelerated-ai-inference-with-nvidia-nim-on-azure-ai-foundry/) already — this isn't a future capability, it's live today. Builders can develop locally on DGX Station, then deploy the same NIM container configuration to Azure for cloud scaling.

**Windows Subsystem for Linux (WSL)** — NVIDIA has extended [CUDA support to WSL](https://developer.nvidia.com/cuda/wsl) for several years, and recent [TensorRT-LLM releases add WSL support](https://nvidia.github.io/TensorRT-LLM/release-notes.html) for RTX-class GPUs. NIM containers can run in WSL without a separate Linux OS or dual-boot setup.

**NVIDIA Agent Toolkit** — [NVIDIA's open-source framework for building and orchestrating enterprise AI agents](https://nvidianews.nvidia.com/news/ai-agents), used by partners including Adobe, SAP, Salesforce, and ServiceNow. It pairs with **NVIDIA OpenShell**, [an open-source runtime NVIDIA is bringing to Windows in partnership with Microsoft](https://developer.nvidia.com/blog/build-personal-ai-agents-on-windows-pcs-with-new-tools-from-microsoft-and-nvidia/) that enforces policy-based security, network, and privacy guardrails for agents running on Windows.

Microsoft and NVIDIA describe the combined Windows-to-Azure stack as a ["unified accelerated computing stack"](https://blogs.nvidia.com/blog/microsoft-build-windows-local-cloud-devices/) for agentic AI — local compute and cloud compute run the same containers and speak the same APIs.

---

## Why Windows Matters (and Why This Took Until 2026)

Previous DGX systems (DGX A100, DGX H100, DGX B200) required Linux. That was fine for AI research teams and cloud infrastructure. It created friction for the broader enterprise:

- Enterprise developers working in Visual Studio and .NET toolchains
- Data scientists running Jupyter on Windows
- Engineers using AutoCAD, SolidWorks, MATLAB alongside AI workflows
- IT departments where Windows is the standard-issue workstation OS for the large majority of employees

DGX Station for Windows is not a different product for a different audience. It is the same GB300 compute running in a native Windows environment with direct access to the Win32 API, DXGI, and the Windows agent ecosystem Microsoft [outlined at Build 2026](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/) — including [Microsoft Execution Containers (MXC)](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/) for policy-driven agent execution, [Project Solara](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/), and [Scout](https://www.infoq.com/news/2026/06/microsoft-scout-openclaw-build/), Microsoft's first "Autopilot" agent.

---

## On-Prem vs. Cloud: When to Buy vs. When to Rent

DGX Station is a capital purchase. Pricing has not been publicly disclosed by NVIDIA (NVIDIA does not publish list prices for its datacenter-class chips). Market estimates for the GB300 datacenter equivalent (DGX B300, 8-GPU system) [put full systems around $300K–$360K](https://tech-insider.org/nvidia-blackwell-gpu-pricing/), based on vendor quotes rather than an official price list. DGX Station is a single-chip deskside unit, not an 8-GPU rack system — treat any $100K–$200K estimate as a rough guess until OEM pricing is announced.

**DGX Station makes economic sense when:**

- Data cannot leave the building. Healthcare (HIPAA), defense (CUI/classified-adjacent), financial services (FCA, SEC data residency), legal (attorney-client privilege over training data).
- You need sustained high-throughput inference for internal APIs. [Dedicated B300-class GPU capacity has been quoted around $6.80–$9/hour](https://getdeploying.com/gpus/nvidia-b300) through mid-2026; at those rates a DGX Station-equivalent spend can break even within roughly 18–24 months of continuous use, though actual payback depends on DGX Station's still-undisclosed price.
- You are running physically sensitive workloads. Robotics policy development with Cosmos 3, autonomous vehicle simulation, or physical AI workflows where latency to a remote cloud is a constraint.
- Your organization runs Windows-native development pipelines and wants agents to integrate directly with local workflows without a cloud intermediary.

**Cloud (Vera Rubin-era) makes sense when:**

- Workloads are bursty. You do not need 24/7 trillion-parameter inference.
- You need to scale to tens or hundreds of parallel agents for brief periods (Claude Code Dynamic Workflows style).
- You are pre-production and iterating on models. No capex commitment during R&D.
- Your data residency requirements are satisfied by AWS/Azure/GCP regional deployments.

**RTX Spark (laptop, fall 2026) makes sense when:**

- The developer — not the organization — is the unit of compute. Individual engineers who want mid-size model inference (up to roughly 120B parameters, [per NVIDIA's RTX Spark specs](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark)) on a laptop without waiting for cloud quota.
- Latency is paramount and the task fits in a smaller model.

---

## What Builders Should Do Before Q4

DGX Station is Q4 2026. It is not orderable today. But the software stack is available now.

**Start with NIM containers locally.** NVIDIA NIM runs today on H100 and A100 hardware. If your organization has existing NVIDIA datacenter gear, you can build against the same NIM API contracts that DGX Station will use. Your code will not need to change.

**Review data residency requirements.** If your organization has not documented which model inference workloads require on-premises compute, start that inventory now. The purchase decision for DGX Station will move through procurement in Q3 2026 if your team wants Q4 delivery.

**Evaluate the NVIDIA AI Enterprise license.** DGX Station ships with NVIDIA AI Enterprise included. If you are running NVIDIA AI Enterprise in the cloud today (Azure, AWS, GCP), you can benchmark your actual cloud bill against a DGX Station amortized over three years.

**Pilot with Microsoft's Windows agent tooling.** [Microsoft Execution Containers (MXC)](https://blogs.windows.com/windowsdeveloper/2026/06/02/build-2026-furthering-windows-as-the-trusted-platform-for-development/), announced at Build 2026, is in early preview now. Agents built against it will be among the primary consumers of DGX Station's local inference when the hardware ships.

---

## The Bigger Context: COMPUTEX 2026's Four-Tier Hardware Stack

DGX Station is one of four NVIDIA hardware tiers all announced or confirmed at COMPUTEX 2026 this week:

| Tier | Product | Form Factor | AI Capability | Timing |
|---|---|---|---|---|
| **Laptop** | [RTX Spark](https://nvidianews.nvidia.com/news/nvidia-microsoft-windows-pcs-agents-rtx-spark) | Notebook / compact desktop | 128GB unified memory, runs 120B-parameter models with 1M-token context, 1 petaflop AI compute | Fall 2026 |
| **Desk** | DGX Station for Windows | Deskside workstation | Up to 1T parameters, 748 GB | Q4 2026 |
| **Cloud rack** | [Vera Rubin NVL72](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer) | Datacenter rack | [Up to 5× inference performance, 10× lower token cost vs. Blackwell](https://www.tomshardware.com/pc-components/gpus/nvidia-launches-vera-rubin-nvl72-ai-supercomputer-at-ces-promises-up-to-5x-greater-inference-performance-and-10x-lower-cost-per-token-than-blackwell-coming-2h-2026) | H2 2026 (AWS, Azure, GCP, Oracle) |
| **Physical AI** | [Cosmos 3](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai) | Inference everywhere | [Unified world model for robotics/AV](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai) | Available now (HuggingFace, NIM) |

The COMPUTEX message from Jensen Huang was not a single product announcement. It was a claim that NVIDIA hardware now covers every tier of enterprise AI deployment simultaneously, from the developer's bag to the hyperscaler rack.

DGX Station for Windows is the enterprise desk tier. It ships Q4 2026. The rest of the stack is already in motion.

---

*NVIDIA DGX Station for Windows was announced June 1, 2026, at COMPUTEX/GTC Taipei. OEM pricing and exact model configurations have not been publicly disclosed as of this writing. Related: [RTX Spark builder guide](/builders-log/nvidia-rtx-spark-computex-2026-local-ai-laptop-builder-guide/), [Cosmos 3 builder guide](/builders-log/nvidia-cosmos-3-physical-ai-omnimodel-computex-2026-builder-guide/), [Nemotron 3 Ultra guide](/builders-log/nvidia-nemotron-3-ultra-550b-moe-open-weights-computex-2026/).*
