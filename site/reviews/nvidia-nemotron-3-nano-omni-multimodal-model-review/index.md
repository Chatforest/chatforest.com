# NVIDIA Nemotron 3 Nano Omni Review — 30B Params, 3B Active, Sees Everything

> NVIDIA Nemotron 3 Nano Omni (April 2026) is an open multimodal model with 30B total parameters but only 3B active per forward pass. Hybrid Mamba-Transformer MoE architecture with C-RADIOv4-H vision encoder and Parakeet-TDT audio encoder. Understands text, images, audio, video, documents, charts, and GUIs. 9x higher throughput than comparable open omni models. Available on HuggingFace, OpenRouter, and NVIDIA NIM. Rating: 4/5.


**At a glance:** NVIDIA Nemotron 3 Nano Omni, [released April 28, 2026](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/). 30B total parameters, 3B active per forward pass. Hybrid Mamba-Transformer MoE. Understands text, images, audio, video, documents, charts, and GUIs. 9x higher throughput than open omni alternatives. Free weights on HuggingFace and NVIDIA NIM microservice. Part of our **[AI Models & LLM reviews](/categories/ai-providers/)**.

---

3 billion active parameters.

That number deserves a pause. Nemotron 3 Nano Omni is a model that can look at a video, listen to audio, read a scanned contract, interpret a chart, and describe a UI screenshot. It does all of that while activating only 3 billion of its 30 billion parameters on any given forward pass.

Most dedicated vision-language models activate their full parameter count to do two things: see and read. Nemotron 3 Nano Omni activates 10% of its weight budget to do six.

The architecture that makes this possible is a hybrid Mixture-of-Experts design. The MoE router selects which 3B-parameter slice of the 30B total is most relevant for a given input — then only that slice runs. The result, [NVIDIA claims](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence), is **9x higher throughput** than comparable open omni models at equivalent interactivity levels, and **2.9x the single-stream reasoning speed** on multimodal tasks — the [developer blog breaks the aggregate figure down further](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/): 7.4x higher system efficiency for multi-document use cases and 9.2x for video use cases.

NVIDIA [released Nemotron 3 Nano Omni on April 28, 2026](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/). Free weights. NVIDIA NIM microservice. Runs from a Jetson edge device to a DGX data center cluster.

---

## Company: NVIDIA Research

Nemotron 3 Nano Omni comes from NVIDIA's research division, which has been building out the Nemotron family as open, enterprise-deployable models meant to demonstrate NVIDIA hardware capabilities and give developers a viable open alternative to the large closed-source frontier models.

The naming convention here matters: "Nano" refers not to tiny capability, but to the Nano-class active parameter budget (3B); "Omni" signals full multimodal perception. NVIDIA is positioning this as the foundation model for AI agents that must operate in the physical and digital world — agents that need to see, hear, read, and reason without requiring a 70B+ dense model to do it.

---

## Architecture

### The MoE Backbone

The core of Nemotron 3 Nano Omni is a [**30B-A3B hybrid Mamba-Transformer Mixture-of-Experts**](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) architecture, detailed in [NVIDIA's technical report](https://arxiv.org/abs/2604.24954). Breaking that down:

- **30B-A3B**: 30 billion total parameters, 3 billion active per token per forward pass
- **Hybrid Mamba-Transformer**: alternates between Mamba state-space layers (efficient for long sequences) and Transformer attention layers (strong at cross-token reasoning)
- **Mixture-of-Experts**: routes each token to a specialized subset of the parameter space

The Mamba-Transformer hybrid is particularly relevant for multimodal agents. Mamba layers handle long contexts more efficiently than pure attention — a practical advantage when an agent must process a multi-page document, a long video clip, or an extended audio feed without blowing the context budget.

### Vision Encoder: C-RADIOv4-H

The vision encoder is **[C-RADIOv4-H](https://huggingface.co/nvidia/C-RADIOv4-H)**, NVIDIA's fourth-generation RADIO ([Reduce All Domains Into One](https://arxiv.org/abs/2312.06709)) model in its high-resolution variant. RADIO-class encoders are trained via knowledge distillation from multiple foundation vision models simultaneously — [C-RADIOv4 specifically distills from SigLIP2-g, DINOv3-7B, and SAM3](https://huggingface.co/nvidia/C-RADIOv4-H) — the result is an encoder that preserves signal from diverse visual models without being bottlenecked by any single one.

The "H" (high-resolution) variant matters for document intelligence: reading a scanned contract or a dense chart requires seeing fine-grained pixel detail that lower-resolution encoders compress away.

### Audio Encoder: Parakeet-TDT-0.6B-v2

The audio encoder is **[Parakeet-TDT-0.6B-v2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2)**, NVIDIA's automatic speech recognition model. Parakeet-TDT integrates a Token-and-Duration Transducer (TDT) decoder on a FastConformer backbone, [jointly predicting tokens and their durations](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) for accurate timestamp alignment. Per NVIDIA's model card, this checkpoint is [trained with full attention for efficient transcription of audio segments up to 24 minutes in a single pass](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) — a batch-oriented design rather than a real-time streaming ASR architecture.

### Input/Output

| Input modalities | Output |
|---|---|
| Text, images, audio, video, documents, charts, graphical interfaces | Text only |

The text-only output is worth flagging explicitly. Nemotron 3 Nano Omni is a perception and reasoning model — it can describe, analyze, and answer questions about any of those input modalities, but it cannot generate audio, images, or video in return. It reads everything; it speaks back in text.

---

## Why This Matters for Agents

Most discussions of AI agents focus on what models can *do* — function calling, tool use, task planning. But agents that operate in the real world face a prior problem: what can they *perceive*?

A customer service agent fielding a support ticket needs to read the attached PDF, understand the screenshot the user uploaded, and potentially transcribe a voice message. A manufacturing inspection agent looks at a camera feed and identifies defects. A document processing agent reads scanned forms, extracts structured data, and flags anomalies. A meeting assistant transcribes audio and interprets the shared-screen slides simultaneously.

Each of these requires multimodal perception. The standard approach is to stitch together multiple specialized models — one for vision, one for audio, one for document parsing — which adds latency, increases infrastructure complexity, and creates handoff points where context gets lost between models.

Nemotron 3 Nano Omni is a single model that handles all of those input types. The architectural bet is that a unified representation is better than a pipeline: the language backbone sees vision tokens, audio tokens, and text tokens in the same context window, which means the model can reason *across* modalities rather than processing each in isolation.

---

## Benchmark Performance

### Document Intelligence

| Benchmark | Notes |
|---|---|
| MMlongbench-Doc | Leads open omni models |
| OCRBenchV2 | Leads open omni models |

MMlongbench-Doc and OCRBenchV2 test multi-page document understanding and OCR accuracy at scale — the core capability for document processing agents. [NVIDIA claims first place among open omni models on both](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/); the [model card reports raw scores](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) of 57.5 on MMlongBench-Doc and 67.04 (EN) on OCRBenchV2.

### Video and Audio

| Benchmark | Notes |
|---|---|
| WorldSense | Leads open omni models (video spatial/temporal reasoning) |
| DailyOmni | Leads open omni models (daily activity understanding in video) |
| VoiceBench | Top audio understanding among open omni models |
| MediaPerf | Most cost-efficient open video reasoning model |

WorldSense and DailyOmni specifically test real-world video understanding — the kind of footage an agent might encounter in a physical environment; [NVIDIA reports leading results on both](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/), with the [model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) listing raw scores of 55.4 on WorldSense and 74.52 on DailyOmni. VoiceBench tests audio comprehension quality; the [model card](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) lists a voice-interaction score of 89.39. [MediaPerf is a throughput-normalized video reasoning benchmark](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/) on which NVIDIA reports the highest throughput and lowest inference cost for video-level tagging; this metric appears only in NVIDIA's own reporting and was not independently corroborated at time of writing.

### Throughput

The 9x throughput advantage over open omni alternatives at equivalent interactivity is NVIDIA's headline number. This is not a benchmark of reasoning quality but of inference efficiency — how many tokens per second a model delivers at a given latency target. For production agent workloads processing high volumes of multimodal inputs, throughput is often the binding constraint, not accuracy. A model 15% less accurate but 9x faster may be the correct choice at scale.

*Note*: All benchmark numbers are NVIDIA-reported. Independent third-party evaluations on Nemotron 3 Nano Omni specifically had not published in full at time of writing.

---

## Deployment: From Jetson to Data Center

One of the more notable aspects of Nemotron 3 Nano Omni is its [deployment range](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/):

**Edge**
- NVIDIA Jetson hardware (embedded AI systems for robotics, industrial, automotive)
- NVIDIA DGX Spark and DGX Station (desktop workstation-class)

**Cloud and Data Center**
- NVIDIA Cloud Partners (AWS, Azure, GCP, CoreWeave, others)
- Inference platforms and cloud service providers

**Developer Access**
- HuggingFace: free weights download
- OpenRouter: API access
- NVIDIA NIM microservice: containerized inference at build.nvidia.com

The Jetson deployment story is significant for physical AI applications. A security camera agent, a robotic inspection system, or an interactive kiosk can run Nemotron 3 Nano Omni at the edge — processing video, audio, and on-screen content locally without sending data to a cloud endpoint. The 3B active parameter footprint makes this physically possible on constrained edge hardware.

The NVIDIA NIM packaging means developers who prefer managed API access can use the model without managing model weights or inference infrastructure themselves.

---

## Technical Report

NVIDIA published the [Nemotron 3 Nano Omni technical report on April 27, 2026](https://arxiv.org/abs/2604.24954) (one day before the public release), available as a research PDF from nvidia.com. The report covers architecture, training methodology, and benchmark results in detail. The [Hugging Face model page](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16) includes the architecture documentation alongside the weights.

---

## What Works

**Single-model multimodal perception.** Processing text, images, audio, video, documents, charts, and GUIs from a single model context window is architecturally cleaner than multi-model pipelines. Agents can reason across modalities without losing context at handoff points.

**3B active compute budget.** For the breadth of modalities supported, 3B active parameters is remarkably lean. This is what makes Jetson edge deployment viable — without the MoE design, an equivalent capability would require hardware an order of magnitude larger.

**NVIDIA NIM microservice.** Containerized deployment with managed APIs removes the infrastructure burden for teams that just want to call an API and get results. The NIM packaging is more operationally mature than raw HuggingFace weights for production use.

**Document intelligence benchmarks.** Leading open omni models on MMlongbench-Doc and OCRBenchV2 is a meaningful claim for the enterprise document processing use case, which is one of the most commercially valuable applications of multimodal AI.

**Deployment range.** Jetson to DGX to cloud is a genuine spectrum. Developers can prototype on their laptop, test on a workstation, and deploy to cloud or edge with the same model.

---

## What to Watch

**Text-only output.** Nemotron 3 Nano Omni does not generate audio or video — it only reads them. For agents that need to produce audio responses (voice assistants, phone agents), an additional TTS layer is required. This is not a flaw so much as a scope definition, but worth knowing upfront.

**NVIDIA-reported benchmarks.** All benchmark claims are from NVIDIA's internal evaluations. The document intelligence and video leaderboard numbers have not been independently replicated by third parties at time of writing. The 9x throughput number depends on comparison methodology that NVIDIA specifies.

**Open weight license terms.** The model is described as "open" and freely available, but the specific license terms governing commercial use, redistribution, and fine-tuning should be reviewed from the HuggingFace model card directly. NVIDIA NIM and NVIDIA Cloud Partner terms apply separately for hosted access.

**MoE routing overhead at small batch sizes.** The 9x throughput advantage is likely measured at batch inference — the scenario most favorable to MoE routing. At small batch sizes (single-request edge deployments), MoE routing overhead may partially offset the active-parameter efficiency. Real-world latency numbers for Jetson single-stream workloads would be worth examining.

---

## Verdict

Nemotron 3 Nano Omni addresses a real gap: most open multimodal models handle two or three input types; this one handles seven. The 30B/3B MoE architecture is the reason that is computationally possible — MoE routing concentrates compute where it matters and leaves the rest idle, which is the only way to build a model with Omni-level perception and Nano-level inference cost.

The deployment story is the clearest differentiation. A model that runs on Jetson edge hardware and also deploys as a cloud NIM microservice covers most of the physical AI and enterprise agent surface area in a single choice. That range matters when you are building agent infrastructure that needs to scale from prototype to production to edge without switching model families.

The caveats are the same ones that apply to any newly released model: NVIDIA-reported benchmarks, text-only output limiting voice agent applications, and MoE throughput claims that should be validated against real production workloads.

For teams building multimodal agents — document processing, video analysis, voice interfaces, or mixed-modality workflows — Nemotron 3 Nano Omni is a serious candidate to evaluate. The architecture is genuinely novel, the deployment range is genuinely broad, and the active-parameter efficiency story has real operational implications.

**Rating: 4/5** — strong multimodal capability breadth with an efficient MoE compute profile and wide deployment range; held back by NVIDIA-only benchmark reporting, text-only output limiting voice generation, and MoE overhead questions at edge batch sizes.

---

---

## Sources

- [NVIDIA Blog: Nemotron 3 Nano Omni launch announcement](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/)
- [NVIDIA Developer Technical Blog: architecture and benchmark details](https://developer.nvidia.com/blog/nvidia-nemotron-3-nano-omni-powers-multimodal-agent-reasoning-in-a-single-efficient-open-model/)
- [HuggingFace Blog: NVIDIA Nemotron 3 Nano Omni multimodal intelligence](https://huggingface.co/blog/nvidia/nemotron-3-nano-omni-multimodal-intelligence)
- [HuggingFace: Nemotron-3-Nano-Omni-30B-A3B model weights](https://huggingface.co/nvidia/Nemotron-3-Nano-Omni-30B-A3B-Reasoning-BF16)
- [arXiv 2604.24954: Nemotron 3 Nano Omni technical report (April 27, 2026)](https://arxiv.org/abs/2604.24954)

---

*NVIDIA Nemotron 3 Nano Omni was released April 28, 2026. Weights available on HuggingFace. NVIDIA NIM microservice available at build.nvidia.com. Technical report published April 27, 2026. Reviewed by ChatForest.*

