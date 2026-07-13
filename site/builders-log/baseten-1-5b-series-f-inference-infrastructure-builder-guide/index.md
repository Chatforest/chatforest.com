# Baseten Raises $1.5B at $13B Valuation: What Inference Operations' Biggest Raise Means for Builders

> Baseten closed a $1.5B Series F at a $13B valuation on June 22, 2026 — processing 1B+ inference calls/day across 87 clusters on 18 cloud providers. This guide covers what Baseten does, who uses it, and how the inference infrastructure market affects where you should deploy your models.


Baseten closed a $1.5 billion Series F on June 22, 2026, valuing the company at $13 billion. The round was led by Altimeter Capital, Conviction, and Spark Capital, with co-leads from Sands Capital and Wellington Management, and participation from IVP, Greylock, 01A, Blackbird, D. E. Shaw Ventures, Battery Ventures, and others. Total capital raised now exceeds $2 billion.

The number matters less than what it signals: the inference operations layer — the software between your model weights and your production API endpoint — just got a $13 billion vote of confidence from some of the most disciplined capital allocators in the market.

## What Baseten Actually Does

Baseten is not a model provider and not a raw GPU rental shop. It occupies the layer between them: systems software that handles GPU orchestration, autoscaling, observability, caching, and developer tooling so that you can run any model at production scale without building that stack yourself.

The practical analogy is AWS Lambda for AI workloads. You bring a model — your own fine-tuned weights, an open-source model, a ComfyUI image workflow, a transcription pipeline — and Baseten handles everything from cold start optimization to cross-cloud routing. The open-source [Truss framework](https://github.com/basetenlabs/truss) is the packaging layer: you define your model's dependencies and serving logic, and Truss turns it into an autoscaling HTTPS endpoint.

Three deployment modes:

- **Baseten Cloud** — fully managed, single-tenant cluster options, 87 clusters across 18 cloud providers, 99.99% uptime SLA
- **Self-hosted** — bring the same tooling into your own VPC; for teams with data residency requirements or existing GPU capacity
- **Hybrid** — on-demand flex capacity that combines your VPC with burst capacity from Baseten Cloud

## The Scale Numbers That Matter

As of June 2026:

- **1 billion+ inference calls processed per day**
- **87 global clusters** across 18 cloud providers
- **~20x revenue growth** year-over-year
- Google Cloud documented **225% better cost-performance** for inference on Baseten's infrastructure

The customer roster reads like the stack that powers the best AI-native products in the ecosystem: Cursor, Notion, Abridge, Clay, Superhuman, World Labs, Decagon, Hex, HeyGen, Mercor, Wispr, Quora, Writer, Retool. When Cursor — the most widely used AI coding tool among professional developers — relies on your inference platform, that's strong production validation.

## What Changed to Make This Raise Possible

The thesis is straightforward: as model capability converges across open and closed weights, the differentiator in AI products shifts from "which model" to "how reliably and cheaply can you run it."

The inflection point Baseten's investors are betting on: **custom and post-trained models now account for 30–50% of model spending in production AI companies**. Off-the-shelf frontier APIs are the starting point; fine-tuned and task-specific variants are where production workloads live. Running those variants at scale — with proper caching, autoscaling, and observability — is not a solved problem, and it is not a commodity.

The competitive dynamics reinforce this. LongCat-2.0, DeepSeek V4, GLM 5.2, and Kimi K2.7 Code are all now available on Baseten's model library, and each one represents a workload that doesn't run optimally on Bedrock or Vertex without significant infrastructure work. Baseten's value proposition gets stronger the more capable open-source models proliferate.

## Model Support Surface

The platform covers more modalities than most builders expect:

- **LLMs** — DeepSeek V4, GLM 5.2, Kimi K2.7 Code, Llama family, Qwen
- **Image generation** — ComfyUI workflows with specialized hardware routing
- **Transcription and speaker diarization** — optimized for audio pipelines
- **Text-to-speech** — real-time audio streaming
- **Embeddings** — throughput-optimized for RAG and search workloads
- **Custom proprietary models** — bring your own weights via Truss

Baseten Training supports multi-node fine-tuning jobs that feed directly into deployment — a train-to-serve pipeline that removes the handoff friction most teams currently manage manually.

## Frontier Gateway

New in the 2026 platform: **Frontier Gateway** lets teams monetize their own models through Baseten's infrastructure. This is the long tail of the inference ecosystem — specialized models built on top of foundation weights, served to external customers. For AI companies building vertical applications, this removes a significant operational barrier to productizing fine-tuned models.

## Benchling Partnership

Baseten also announced a partnership with Benchling to bring inference infrastructure to biotech R&D workflows, a vertical where data residency requirements and specialized model types make the self-hosted option particularly relevant.

## What This Means for Builders

**If you're using AWS Bedrock or Vertex AI for open-source model serving**, compare Baseten's pricing directly. The 225% cost-performance figure from Google's own cloud blog suggests the optimization surface is real, not marketing. Use Baseten's savings calculator for your specific workload profile.

**If you need VPC deployment**, the self-hosted option gives you Baseten's tooling inside your own infrastructure. The comparison set here is Modal, Replicate, and RunPod — Baseten's differentiation is operational maturity (87 clusters, 99.99% SLA, forward-deployed engineers) rather than raw price.

**If you're fine-tuning**, Baseten Training plus one-click deployment is the cleanest train-to-serve pipeline available without building custom MLOps tooling. The Truss framework is worth learning even if you don't commit fully to the platform — it's a sensible model packaging standard.

**If you're building image generation pipelines with ComfyUI**, Baseten's native support and hardware routing for workflow graphs is a significant operational advantage over running ComfyUI on a raw GPU instance.

**If you're evaluating inference infrastructure for a production product**, the customer roster above is meaningful signal. Cursor and Notion are not running on Baseten because it was cheap to prototype on — they're there because it handles production-grade scale with acceptable operational overhead.

## The Broader Signal

The Baseten raise is the third large inference infrastructure round in 2026 after Together AI ($800M Series C) and the broader compute infrastructure surge. When capital this disciplined concentrates on a specific layer of the AI stack, it's worth asking whether your current inference setup is optimized or just the path of least resistance from your initial prototype.

The model is increasingly not the bottleneck. The operations around the model — latency, cost, reliability, scaling behavior, observability — are where production AI products succeed or fail. That layer is what $1.5 billion just bet on.

---

*Baseten's model library and Truss framework documentation are at [baseten.co](https://www.baseten.co) and [docs.baseten.co](https://docs.baseten.co).*

