---
title: "NVIDIA DGX Station for Windows: Trillion-Parameter AI on Your Desk — Enterprise Builder Guide"
date: 2026-06-05
description: "NVIDIA announced DGX Station for Windows at COMPUTEX 2026 — a GB300 Grace Blackwell deskside supercomputer that runs 1-trillion-parameter AI models locally on Windows. Q4 2026 availability. Here's what enterprise builders need to know about the hardware, software stack, and when to choose it over cloud."
og_description: "NVIDIA DGX Station for Windows: 748GB coherent memory, 20 petaflops FP4, runs up to 1T parameter models locally on Windows. Built with Microsoft. NIM containers work unchanged on DGX Station and Azure. Q4 2026 from Dell, HP, ASUS, MSI, GIGABYTE, Supermicro. Builder guide to the hardware, software stack, and on-prem vs. cloud decision."
content_type: "Builder's Log"
categories: ["AI Infrastructure", "Hardware", "Enterprise AI"]
tags: ["nvidia", "dgx-station", "windows", "gb300", "grace-blackwell", "on-prem", "enterprise", "local-ai", "nim", "computex-2026", "inference", "builders-log"]
---

NVIDIA announced DGX Station for Windows on June 1, 2026, at COMPUTEX in Taipei. It is a deskside AI supercomputer powered by the GB300 Grace Blackwell Ultra Desktop Superchip, capable of running AI models up to one trillion parameters locally on Windows. Q4 2026 availability from six OEM partners.

The premise is straightforward: enterprise AI workloads have historically required Linux datacenter hardware. Most Fortune 500 companies run Windows. DGX Station closes that gap.

---

## Hardware Specifications

| Component | Spec |
|---|---|
| **Chip** | GB300 Grace Blackwell Ultra Desktop Superchip |
| **Architecture** | Blackwell Ultra GPU + 72-core Grace CPU, NVLink-C2C interconnect |
| **Memory** | Up to 748 GB coherent unified memory (GPU + CPU shared pool) |
| **AI Compute** | Up to 20 petaflops FP4 |
| **Networking** | NVIDIA ConnectX-8 SuperNIC, up to 800 Gb/s |
| **Optional GPU** | RTX PRO 6000 Blackwell Workstation GPU (adds ray-traced visualization and physical simulation) |
| **OS** | Windows 11 (native, not via virtualization layer) |
| **Availability** | Q4 2026 |
| **OEMs** | ASUS, Dell Technologies, GIGABYTE, HP, MSI, Supermicro |

The coherent memory design is the key hardware fact for builders. 748 GB of unified CPU/GPU memory means large models do not page between separate memory pools. A Llama 3.1 405B in FP16 requires roughly 810 GB — at FP8 or FP4 quantization it fits in the 748 GB pool with room for KV cache. Models in the 70B to 405B range run comfortably at full precision.

---

## What One Trillion Parameters Actually Means

"Up to 1 trillion parameters" is NVIDIA's headroom claim, not a model that currently exists in publicly available weights. Useful reference points:

| Model | Parameters | Fits in DGX Station? |
|---|---|---|
| Llama 3.1 8B | 8B | Yes, with large margin |
| Llama 3.1 70B | 70B | Yes, full FP16 |
| Llama 3.1 405B | 405B | Yes, FP8/FP4 quantization |
| Nemotron 3 Ultra | 550B total / 55B active (MoE) | Yes, MoE active weight fits easily |
| Hypothetical dense 1T | 1,000B | Yes, FP4 |

For most enterprise use cases, the practical ceiling is running Llama 3.1 405B, Nemotron 3 Ultra, or similar open frontier models locally without cloud egress.

---

## Software Stack

DGX Station for Windows was built in direct collaboration with Microsoft. The software integration matters as much as the hardware.

**NVIDIA AI Enterprise suite** — the full commercial software stack including CUDA, cuDNN, TensorRT, and RAPIDS. Licensed per device, not per cloud-hour.

**NVIDIA NIM microservices** — pre-packaged inference endpoints for popular models (Llama-4, Mistral Large, Nemotron-5, and others). The critical detail: the same NIM containers run on a local DGX Station and in Azure Kubernetes Service without modification. You write once, deploy to either.

**Windows Subsystem for Linux (WSL)** — NVIDIA contributed TensorRT-LLM optimizations and CUDA libraries to WSL. NIM containers run in WSL without a separate Linux OS or dual-boot setup.

**Azure AI Foundry integration** — in July 2026, Azure AI Foundry gains native NIM microservice support. Builders can develop locally on DGX Station, then drag and drop the same NIM endpoint configuration to Azure for cloud scaling.

**NVIDIA AgentKit** — agent orchestration framework that integrates with Microsoft Foundry's agent fabric. Agents built with AgentKit can bind directly to Windows applications and workflows (Outlook, Teams, SharePoint, OneDrive, enterprise line-of-business apps).

The Microsoft / NVIDIA framing at Build 2026 called this a "unified agentic fabric" — local compute and cloud compute run the same containers, speak the same APIs, and register with the same agent identities.

---

## Why Windows Matters (and Why This Took Until 2026)

Previous DGX systems (DGX A100, DGX H100, DGX B200) required Linux. That was fine for AI research teams and cloud infrastructure. It created friction for the broader enterprise:

- Enterprise developers working in Visual Studio and .NET toolchains
- Data scientists running Jupyter on Windows
- Engineers using AutoCAD, SolidWorks, MATLAB alongside AI workflows
- IT departments that provision Windows workstations to 95%+ of their users

DGX Station for Windows is not a different product for a different audience. It is the same GB300 compute running in a native Windows environment with direct access to the Win32 API, DXGI, and the Windows agent ecosystem that Microsoft is building with Project Solara, Scout Autopilots, and the Windows Agent Platform announced at Build 2026.

---

## On-Prem vs. Cloud: When to Buy vs. When to Rent

DGX Station is a capital purchase. Pricing has not been publicly disclosed, but the GB300 datacenter equivalent (DGX B300, 8-GPU system) runs $300K–$350K at list price. DGX Station is a single-chip deskside unit — estimate $100K–$200K range when OEM pricing is announced.

**DGX Station makes economic sense when:**

- Data cannot leave the building. Healthcare (HIPAA), defense (CUI/classified-adjacent), financial services (FCA, SEC data residency), legal (attorney-client privilege over training data).
- You need sustained high-throughput inference for internal APIs. At cloud rates for B300-class GPUs (~$6.80/hour dedicated), a DGX Station equivalent breaks even in 18–24 months of continuous use.
- You are running physically sensitive workloads. Robotics policy development with Cosmos 3, autonomous vehicle simulation, or physical AI workflows where latency to a remote cloud is a constraint.
- Your organization runs Windows-native development pipelines and wants agents to integrate directly with local workflows without a cloud intermediary.

**Cloud (Vera Rubin-era) makes sense when:**

- Workloads are bursty. You do not need 24/7 trillion-parameter inference.
- You need to scale to tens or hundreds of parallel agents for brief periods (Claude Code Dynamic Workflows style).
- You are pre-production and iterating on models. No capex commitment during R&D.
- Your data residency requirements are satisfied by AWS/Azure/GCP regional deployments.

**RTX Spark (laptop, fall 2026) makes sense when:**

- The developer — not the organization — is the unit of compute. Individual engineers who want 32B-70B model inference on a laptop without waiting for cloud quota.
- Latency is paramount and the task fits in a smaller model.

---

## What Builders Should Do Before Q4

DGX Station is Q4 2026. It is not orderable today. But the software stack is available now.

**Start with NIM containers locally.** NVIDIA NIM runs today on H100 and A100 hardware. If your organization has existing NVIDIA datacenter gear, you can build against the same NIM API contracts that DGX Station will use. Your code will not need to change.

**Review data residency requirements.** If your organization has not documented which model inference workloads require on-premises compute, start that inventory now. The purchase decision for DGX Station will move through procurement in Q3 2026 if your team wants Q4 delivery.

**Evaluate the NVIDIA AI Enterprise license.** DGX Station ships with NVIDIA AI Enterprise included. If you are running NVIDIA AI Enterprise in the cloud today (Azure, AWS, GCP), you can benchmark your actual cloud bill against a DGX Station amortized over three years.

**Pilot with Windows Agent Platform APIs.** Microsoft's WinAgent SDK (announced Build 2026) is available in preview now. Agents built against WinAgent SDK will be the primary consumers of DGX Station's local inference when the hardware ships.

---

## The Bigger Context: COMPUTEX 2026's Four-Tier Hardware Stack

DGX Station is one of four NVIDIA hardware tiers all announced or confirmed at COMPUTEX 2026 this week:

| Tier | Product | Form Factor | AI Capability | Timing |
|---|---|---|---|---|
| **Laptop** | RTX Spark | Notebook / compact desktop | 32B–70B models, 300+ tokens/sec | Fall 2026 |
| **Desk** | DGX Station for Windows | Deskside workstation | Up to 1T parameters, 748 GB | Q4 2026 |
| **Cloud rack** | Vera Rubin NVL72 | Datacenter rack | 5× inference/rack vs. Blackwell, 10× token cost reduction | H2 2026 (AWS, Azure, GCP, Oracle) |
| **Physical AI** | Cosmos 3 | Inference everywhere | Unified world model for robotics/AV | Available now (HuggingFace, NIM) |

The COMPUTEX message from Jensen Huang was not a single product announcement. It was a claim that NVIDIA hardware now covers every tier of enterprise AI deployment simultaneously, from the developer's bag to the hyperscaler rack.

DGX Station for Windows is the enterprise desk tier. It ships Q4 2026. The rest of the stack is already in motion.

---

*NVIDIA DGX Station for Windows was announced June 1, 2026, at COMPUTEX/GTC Taipei. OEM pricing and exact model configurations have not been publicly disclosed as of this writing. Related: [RTX Spark builder guide](/builders-log/nvidia-rtx-spark-computex-2026-local-ai-laptop-builder-guide/), [Cosmos 3 builder guide](/builders-log/nvidia-cosmos-3-physical-ai-omnimodel-computex-2026-builder-guide/), [Nemotron 3 Ultra guide](/builders-log/nvidia-nemotron-3-ultra-550b-moe-open-weights-computex-2026/).*
