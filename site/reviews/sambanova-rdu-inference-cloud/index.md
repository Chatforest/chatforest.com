# SambaNova Review: Custom RDU Silicon for Full-Precision Large-Model Inference

> SambaNova Systems builds custom Reconfigurable Dataflow Unit (RDU) chips and a public inference API optimized for massive models at full 16-bit precision. We review its cloud API, on-premise DataScale systems, SN50 architecture, and competitive positioning against Groq, Cerebras, and GPU clouds.


Most AI infrastructure companies rent you time on NVIDIA GPUs. SambaNova Systems builds its own chips. The Reconfigurable Dataflow Unit (RDU) is a purpose-built AI accelerator designed around a fundamentally different execution model — and in 2026, after nearly a decade of development, SambaNova is making a compelling case that custom silicon matters most for the largest models at full precision.

This review covers SambaNova's public cloud API (SambaCloud), its on-premise DataScale hardware, the SN50 chip architecture, pricing, and where it fits against GPU-first competitors like Groq, Cerebras, Together AI, and Fireworks AI.

---

## Company Background

SambaNova Systems was founded in 2017 in Palo Alto, California by Rodrigo Liang (CEO) and Kunle Olukotun (Chief Technologist). Olukotun is a Stanford professor known for pioneering chip multiprocessing research — the kind of credentials that signal a chip company built by people who understand computer architecture deeply, not just AI software stacked on commodity hardware.

The company has raised approximately $1.4 billion across known rounds: a $150M Series B (Intel Capital led, 2019), $250M Series C (BlackRock led, 2020), $676M Series D (2021, at a $5.1B valuation), and a $350M+ Series E announced in February 2026. Investors include Intel Capital, BlackRock, SoftBank, Google Ventures, Samsung, SK Telecom, Temasek, and Walden International. Lip-Bu Tan — former CEO of Cadence Design Systems and founder of Walden International — serves as Executive Chairman.

SambaNova does not publicly disclose ARR, but its 2025 annual report described "record bookings and revenue." Fast Company ranked it #4 in Computing on its 2025 Most Innovative Companies list, citing SambaNova's ability to run DeepSeek R1 671B at 231 tokens/second — three times faster than GPU-based providers at the time — at 5x better power efficiency. Fortune placed it on the Future 50 list in September 2025.

---

## The RDU: Dataflow vs. SIMD

To understand SambaNova's performance profile, you have to understand why it built a new chip category instead of optimizing GPU deployments.

Modern GPUs are SIMD processors. They excel at executing thousands of identical operations in parallel — ideal for matrix multiplication during training, when you know the workload in advance. But inference has a different character: data moves through a neural network sequentially, and GPUs spend significant time on kernel launch overhead, data movement between processing units, and reloading model weights from memory.

SambaNova's RDU uses a **dataflow architecture**: instead of a fixed array of execution units waiting for data, the chip configures itself to match the computational graph of the model being run. Data flows continuously through fused operations without being written back to memory between each layer. The SambaNova compiler can fuse an entire Llama 3.1 8B decoder into a single dataflow kernel — what would be dozens of separate GPU kernel launches becomes one continuous execution.

The SN40L (fourth generation, announced 2023) uses a three-tier memory hierarchy:
- **On-die SRAM**: For high-intensity operations
- **HBM** (High Bandwidth Memory): For active model weights
- **DDR DRAM**: For large-capacity storage, enabling hundreds of models to sit resident and hot-swap to HBM in microseconds

This memory architecture is the structural reason SambaNova can run 405-billion and 671-billion parameter models at production speeds without quantizing them. GPU-based providers serving models this large typically use FP4 or INT8 quantization to fit model weights into available HBM — reducing model size by 50-75%, with corresponding accuracy tradeoffs. SambaNova's DDR tier gives it enough capacity to hold full-precision weights.

### SN50: Fifth Generation (February 2026)

Announced alongside the Series E in February 2026, the SN50 delivers:
- **5x more compute** per accelerator vs SN40L
- **4x more network bandwidth**
- Scaling to 256 accelerators via multi-terabit/second interconnect
- Cloud-scale scaleout to 32,000 RDUs
- Support for models up to 10 trillion parameters with 10 million token context lengths

The SN50 is the first chip designed specifically with agentic AI workloads in mind — multi-step reasoning chains that require rapid sequential inference rather than batch throughput.

In April 2026, Intel announced a "Blueprint for Heterogeneous Inference" combining Intel GPUs for prefill (the prompt processing phase, naturally parallel), SambaNova RDUs for decode (the token-by-token generation phase, where dataflow excels), and Intel Xeon 6 processors for agentic tool execution. Production deployment is targeted for H2 2026. The collaboration signals that the industry is beginning to treat inference not as a monolithic GPU problem but as a multi-chip architecture problem.

---

## SambaCloud: The Public API

SambaNova's public inference API is available at cloud.sambanova.ai and is fully OpenAI-compatible — same endpoints, same client libraries. It bills per token, requires no credit card for signup, and offers $5 in free credits (valid for 30 days).

The platform states explicitly that it "never sees or collects any of your data or user prompts" — a meaningful claim for enterprises wary of training data harvesting, though as with any cloud service, this requires trusting the vendor's infrastructure controls.

### Model Catalog (May 2026)

SambaCloud's catalog is selective rather than exhaustive. As of this review:

| Model | Context | Notes |
|-------|---------|-------|
| DeepSeek-V3.1 | 131K | Full precision |
| DeepSeek-V3.1-cb | 32K | Higher output token limit (32K) |
| DeepSeek-V3.2 | 32K | Latest V3 generation |
| DeepSeek-R1-Distill-Llama-70B | — | Distilled reasoning |
| Llama-4-Maverick-17B-128E-Instruct | — | Vision + text, Llama 4 launch partner |
| Meta-Llama-3.3-70B-Instruct | — | — |
| gpt-oss-120b (low/high) | — | Two serving tiers |
| MiniMax-M2.5 / M2.7 | — | Exclusive or earliest availability |
| gemma-3-12b-it | — | Google Gemma |

Notably absent: image generation, audio generation (though audio transcription/translation is supported), and the sprawling 200-model catalogs of Together AI or Fireworks AI. SambaNova's catalog depth is roughly 10 models. What it offers instead is availability of the largest models at performance levels no GPU provider matches.

The platform also offers specialized agent APIs — a main agent plus coding, financial analysis, deep research, and data science subagents — with both multi-turn and fire-and-forget variants. This is a more opinionated product than a raw inference API, oriented toward developers building agentic applications.

Integrations include LangChain, LlamaIndex, CrewAI, AutoGen, OpenRouter, n8n, Hugging Face, Cline, AWS, and approximately 50 others.

---

## Performance: Where the RDU Actually Wins

The performance story for SambaNova is most compelling at model sizes where GPU providers struggle.

Per independent benchmarks from Artificial Analysis:

**Llama 3.1 405B**:
- SambaNova: **129 tokens/second** (full 16-bit precision)
- Most GPU providers: 10–25 tokens/second (quantized)
- Groq: Not offered
- Cerebras: Not offered

**DeepSeek R1 671B**:
- SambaNova: **231–255 tokens/second** (full 16-bit precision)
- GPU-based providers (average): ~19 tokens/second per user
- NVIDIA's GTC 2025 demo: Used FP4 quantization (50% reduced model size)

**Llama 3.1 70B**:
- SambaNova: 457 tokens/second
- Cerebras: 445 tokens/second
- Groq: 250 tokens/second

**gpt-oss-120b** (available on SambaCloud):
- SambaNova low tier: 728 tokens/second
- SambaNova high tier: 695 tokens/second

**MiniMax-M2.7** (as of May 2026):
- SambaNova: 434 tokens/second — claimed more than 3x faster than any other provider

**Small models (Llama 3.1 8B)**:
- SambaNova: 1,042 tokens/second
- Cerebras: 1,837 tokens/second
- Groq: 751 tokens/second

The gap between SambaNova and Cerebras inverts as model size grows. Cerebras's wafer-scale architecture delivers extreme throughput on models that fit entirely on a single chip. SambaNova's multi-tier memory hierarchy means it doesn't sacrifice accuracy or scale to fit larger models — it's the only production API offering both size and speed on 671B-parameter models.

SambaNova also published an accuracy comparison against Groq's quantized Llama 3 8B: 3.16% better average performance across 15 general tasks, with a 9+ percentage point advantage on conversational tasks (CoQA benchmark). The precision advantage matters more in specialized domains where quantization errors compound.

---

## Pricing

**Free tier**: $5 in credits, no credit card required, expires 30 days after signup.

**Paid tiers**: Developer (pay-as-you-go) and Enterprise (custom subscription with higher rate limits and dedicated support).

**Per 1M tokens (input / output)**:

| Model | Input | Output | Blended (3:1)* |
|-------|-------|--------|----------------|
| gpt-oss-120b | $0.22 | $0.59 | ~$0.31 |
| gemma-3-12b-it | $0.20 | $0.35 | ~$0.24 |
| MiniMax-M2.5 | $0.30 | $1.20 | ~$0.52 |
| Llama 3.3 70B | $0.60 | $1.20 | ~$0.75 |
| DeepSeek-R1-Distill-Llama-70B | $0.70 | $1.40 | ~$0.88 |
| MiniMax-M2.7 | $0.60 | $2.40 | ~$1.05 |
| Llama-4-Maverick | $0.63 | $1.80 | ~$0.92 |
| DeepSeek-V3.1 | $3.00 | $4.50 | ~$3.38 |
| DeepSeek-V3.2 | $3.00 | $4.50 | ~$3.38 |

*Blended at 3 input tokens per output token — adjust to your workload.

The gpt-oss-120b pricing at $0.31/1M blended is competitive for a 120B-parameter model. The DeepSeek V3 pricing is noticeably high compared to Together AI and Fireworks — likely reflecting the cost of running full-precision 671B weights rather than quantized versions.

There is no batch API discount publicly offered, and no fine-tuning pricing listed (fine-tuning is not a public cloud product).

---

## On-Premise: DataScale, SambaRack, and SambaManaged

SambaNova's enterprise product line targets organizations that cannot or will not route data through third-party cloud APIs — national laboratories, banks, government agencies, and sovereign AI initiatives.

**SambaRack**: 16 SN50 RDUs per rack. Scales to 256 accelerators via multi-terabit/second interconnect. Air-cooled; operates at approximately 10 kW per rack. No liquid cooling infrastructure required — significant for data centers built before liquid cooling was standard.

**SambaStack**: Full-stack inference (SambaRack + software + pre-loaded model bundles). Claims 4x energy savings vs GPUs and supports hot-swap model loading.

**SambaManaged**: Turnkey managed inference cloud. SambaNova operates the hardware in a customer's data center or a partner facility. Claims 90-day deployment. Available via AWS Marketplace. Designed for organizations that want inference-as-a-service without building the operational expertise internally.

Notable on-premise deployments:
- **SoftBank (Japan)**: One of Japan's largest LLM computing platforms. Also the first SN50 customer for next-generation AI data centers (announced February 2026).
- **Lawrence Livermore National Laboratory**: Multi-rack DataScale for Cognitive Simulation — combining AI with physics-based simulation for fusion energy research. Partnership since 2020.
- **Argonne National Laboratory**: DataScale in the ALCF AI Testbed, available to the scientific community.
- **OVHcloud (EU)**: Initial France deployment (year-end 2025). 99.8% uptime SLA. Targeting financial trading, cybersecurity, and industrial automation workloads.
- **Infercom (EU)**: Luxembourg-based, initial France deployment. GDPR and EU AI Act compliant. First EU sovereign AI inference service.
- **SouthernCrossAI (Australia)**: Claims 3x higher throughput vs GPU clouds and up to 10x lower energy cost per inference.
- **TEPCO Systems (Japan)**: Deploying SambaNova AI infrastructure within the TEPCO Group and for external customers. Selected for Japan's NEDO Post-5G R&D project (April 2026).

The sovereign AI angle is coherent strategy, not marketing gloss. Regulatory requirements, data residency laws, and national security considerations are real constraints that push enterprise and government buyers toward on-premise hardware — and SambaNova's air-cooled, energy-efficient rack is a practical fit for existing data centers.

---

## Competitive Positioning

**vs. Groq**: Groq's LPU excels at small-model throughput (sub-1000 token/s range for 7B-70B models). SambaNova beats Groq on 70B+ models and is the only option for 405B and 671B at production speed. Groq does not offer these massive models. Groq has a larger model catalog (~20+ models). Groq's recently announced acquisition by NVIDIA adds strategic uncertainty. SambaNova remains independent.

**vs. Cerebras**: The closest architectural competitor — both use custom silicon, both emphasize precision and throughput. Cerebras's wafer-scale engine (WSE-3) wins on small-model speed (1,837 t/s on 8B vs SambaNova's 1,042 t/s). SambaNova wins on large-model availability (Cerebras does not publicly offer 405B or 671B model inference). For 70B, they're roughly matched (445 vs 457 t/s). The choice depends on model size and whether on-premise hardware matters to you — SambaNova has a broader enterprise deployment network.

**vs. Together AI and Fireworks AI**: These are GPU-cloud providers with much larger model catalogs (200+ and ~50 models respectively), fine-tuning APIs, and more flexible developer tooling. SambaNova does not offer fine-tuning. For developers who need catalog breadth, fine-tuning, or want to switch models frequently, Together or Fireworks are more complete platforms. SambaNova wins only when you need the fastest large-model inference at full precision, or when data sovereignty requires on-premise hardware.

**vs. GPU clouds (AWS, GCP, Azure, Lambda Labs)**: GPU clouds offer the broadest flexibility but can't match SambaNova's throughput on large models without significant quantization tradeoffs. Energy costs heavily favor SambaNova for sustained inference workloads.

---

## Limitations

**No fine-tuning API.** SambaNova has no public fine-tuning service. If you need to fine-tune a model, you'll need to go elsewhere (Together AI, Fireworks AI, or a GPU cloud) and then potentially switch to SambaNova for inference.

**Narrow model catalog.** Approximately 10 models vs 50–200 at competitors. If you need a model SambaNova doesn't serve, you're running on a GPU cloud.

**Context window limitations.** DeepSeek-V3.1's standard tier is capped at 131K context with only 7K completion tokens. The extended context window variant (DeepSeek-V3.1-cb) gets 32K completion tokens but only 32K input context — a narrow slot. Long-context use cases may be constrained.

**High pricing on large models.** DeepSeek V3 at $3.00/$4.50 per 1M tokens is expensive relative to Together AI and Fireworks AI. The full-precision quality premium has a real cost.

**No image or video generation.** If you want Flux, SDXL, or video generation, SambaNova is not the platform.

**Enterprise-only for on-premise.** SambaRack and SambaStack require direct sales engagement. No self-serve hardware purchasing. 90-day deployment timeline means this is a multi-quarter procurement process.

**Revenue opacity.** SambaNova does not publicly disclose ARR or revenue. "Record bookings" in 2025 is encouraging but makes independent financial health assessment difficult. The Series E raise at presumably similar or lower valuation to the 2021 Series D ($5.1B) suggests that the company is still scaling toward a path that justifies its early capital raise.

**SN50 production timing.** The SN50 was announced February 2026. The Intel heterogeneous inference blueprint targets H2 2026. The cutting-edge hardware is not yet at full production maturity.

---

## Who Should Use SambaNova

**Strong fit:**
- Production applications running DeepSeek R1 671B, DeepSeek V3, or Llama 3.1 405B that require full-precision accuracy (not distilled or quantized variants)
- Enterprises deploying AI in air-cooled data centers with power constraints
- Organizations with data sovereignty requirements (EU GDPR, ITAR, national AI programs)
- Applications where quantization accuracy loss is measurable and matters (legal, medical, specialized domain Q&A)
- Developers needing fast agentic inference (SN50's core design target)

**Poor fit:**
- Developers who need to switch between many models frequently
- Teams that need fine-tuning as part of their workflow
- Applications requiring image or video generation
- Cost-sensitive workloads on small models (Cerebras or GPU clouds may be cheaper)
- Organizations unwilling to accept a narrow cloud model catalog

---

## Bottom Line

SambaNova's architecture bet — custom dataflow silicon optimized for inference rather than training — is paying off specifically at the frontier of model size. No GPU-based cloud provider runs DeepSeek R1 671B or Llama 3.1 405B at full 16-bit precision at production speed. SambaNova does. That's not a benchmark game; it's a structural consequence of having three tiers of memory and a compiler that fuses model graphs rather than scheduling them as discrete GPU kernels.

The public cloud API is a solid product for developers who want fast, accurate large-model inference with minimal DevOps friction. The enterprise on-premise story is compelling for the sovereign AI market that Europe, Japan, and Australia are actively building.

The limitations are real: no fine-tuning, a narrow model catalog, high prices on large models, and an on-premise purchasing process that takes months. If you need anything beyond inference — fine-tuning, image generation, a 200-model catalog — you'll need a different platform.

But for the specific use case SambaNova targets — running the largest open-weight models fast, accurately, and without accuracy-eroding quantization — it currently has no equal.

**Rating: 4.5 / 5**

*Half-point deduction for no fine-tuning API, narrow model catalog, and revenue opacity that makes long-term vendor stability harder to assess.*

---

*ChatForest reviews AI infrastructure based on publicly available documentation, benchmarks, press releases, and independent research. We do not have hands-on API access to the services we review. Pricing and model availability change frequently — verify current details at sambanova.ai before making purchasing decisions.*

