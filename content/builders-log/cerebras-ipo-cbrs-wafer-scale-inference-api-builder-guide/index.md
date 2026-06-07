---
title: "Cerebras Went Public at $95B. Here's What the Biggest Tech IPO Since Uber Means for Builders."
date: 2026-05-14
description: "Cerebras (CBRS) raised $5.55 billion on May 14 in the largest US tech IPO since Uber. The WSE-3 chip delivers 2,300+ tokens per second on Llama 70B — roughly 75x faster than GPU inference. The API is OpenAI-compatible, the free tier is generous, and OpenAI itself signed a $20B deal to use it. Here's when to route your workloads there."
content_type: "Builder's Log"
categories: ["Infrastructure", "AI Industry", "Developer Tools"]
tags: ["cerebras", "cbrs", "wafer-scale", "inference", "api", "llama", "latency", "wse-3", "ipo", "hardware", "openai", "speed"]
---

On May 14, 2026, Cerebras Systems (ticker: CBRS) priced its shares at **$185** and opened on the Nasdaq at **$350** — a 89% gap up before a single retail trade occurred. By the closing bell the stock had settled at **$311**, up **68%**, giving the company a market cap of approximately **$95 billion**. It was the largest US technology IPO since Uber in 2019.

Three weeks later, the stock trades around **$200**. The hype has normalized. But the technology has not changed — and for builders who run latency-sensitive workloads on open models, the Cerebras inference API is one of the more significant pieces of infrastructure that became accessible in 2026.

---

## What Cerebras Actually Is

Cerebras is an AI hardware company with a genuinely unusual architecture. Every other major compute vendor — Nvidia, AMD, Intel, Google, Amazon — builds chips by connecting many smaller silicon dies together. Cerebras does the opposite: the **WSE-3 (Wafer Scale Engine 3)** uses an entire 12-inch silicon wafer as a single processor.

The numbers are striking. Where an H100 GPU contains approximately 80 billion transistors, the WSE-3 contains **4 trillion transistors** across **900,000 AI cores**, with **44 GB of on-chip SRAM** and **21 petabytes per second** of memory bandwidth. There is no chip-to-chip communication latency because there are no separate chips to communicate.

The practical consequence for inference: when a model's weights fit on the chip (or a cluster of CS-3 systems), the memory bottleneck that constrains GPU inference largely disappears. The chip is not waiting to load weights from HBM — they're already there, on-die, at full bandwidth.

---

## The Inference Speed Numbers

Cerebras claims, and independent benchmarks broadly confirm, throughput that is qualitatively different from GPU inference:

| Model | Cerebras (tok/s) | GPU Cluster (tok/s) | Speedup |
|---|---|---|---|
| Llama 3.1 405B | 969 | 10–15 | ~75x |
| Llama 3.3 70B | 2,314 | 50–120 | ~25–45x |
| Llama 3.1 8B | 3,000+ | 100–300 | ~10–20x |

The 405B number is the most meaningful for the use cases where Cerebras wins. A 75x speedup on a frontier-class open model is not a marginal improvement — it is the difference between a product that feels instantaneous and one where you can see the generation happening.

For context: this is faster than most human readers can process text. At 969 tokens per second on the 405B model, a 500-word answer arrives in under a second.

---

## The Developer API

The Cerebras inference API is **fully compatible with the OpenAI Chat Completions format**. Switching a working OpenAI integration to Cerebras requires changing exactly two values: the `base_url` and the API key.

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://api.cerebras.ai/v1",
    api_key="your-cerebras-api-key"
)

response = client.chat.completions.create(
    model="llama3.3-70b",
    messages=[{"role": "user", "content": "Your prompt here"}]
)
```

Pricing tiers:

- **Free**: 24 million tokens per day — enough for most development and small-production workloads
- **Freemium**: per-token pricing above the free threshold
- **Enterprise**: custom rates and SLAs
- **AWS Bedrock**: integration announced March 2026, expected to reach GA by mid-2026, which opens standard enterprise procurement channels

The model catalog is open-weight only: Llama family (8B, 70B, 405B), with support for additional Meta and open-source models. You cannot run GPT-4, Claude, or Gemini on Cerebras — those remain closed-weight and vendor-hosted.

---

## The OpenAI Relationship: Customer, Investor, and Financier

One detail in the Cerebras S-1 that received less attention than the stock price: **OpenAI is simultaneously Cerebras's biggest customer, one of its equity holders, and a direct financier of its infrastructure buildout.**

The structure:

- **December 2025**: OpenAI and Cerebras signed a Master Relationship Agreement giving OpenAI access to Cerebras inference capacity
- **January 2026**: OpenAI expanded the commitment to a three-year deal worth over **$10 billion**, securing **750 megawatts** of Cerebras compute
- **Pre-IPO**: OpenAI committed a further **$20 billion** in purchase volume, with the deal structured to give OpenAI approximately **11% equity stake** in Cerebras
- **Infrastructure financing**: OpenAI separately contributed **$1 billion** to fund construction of the data centers that will fulfill its own purchase orders

The implication: OpenAI is not just a buyer. It is an anchor investor with a structural interest in Cerebras's continued operation, using its own purchase commitments as the validation signal that made the IPO possible. OpenAI using Cerebras for inference is also a direct endorsement of the technology — the company that built GPT-5 is routing production workloads through WSE-3 chips.

---

## When to Route Workloads to Cerebras

The architecture is genuinely better for a specific class of use case. The question is whether your workload is in that class.

**Strong fit:**

- **Real-time voice agents** — 2,300 tok/s on 70B means transcription response, model reasoning, and TTS can all happen faster than human speech. Latency stops being the architectural bottleneck.
- **Interactive coding assistance** — when a developer is blocked waiting for a suggestion, every 100ms matters. Cerebras eliminates the wait state.
- **Live simulation and agent loops** — multi-step reasoning pipelines where each step's output feeds the next. 75x faster per step compounds.
- **High-concurrency, bursty workloads on open models** — if you're running Llama 3.3 70B at scale and GPU cold-start latency is causing queuing, Cerebras's throughput smooths the peak.
- **Low-latency batch processing** — when you have 100,000 documents to classify and you need it done before a deadline, throughput wins.

**Poor fit:**

- **Closed models** — GPT-4, Claude 3, Gemini 2.5 are unavailable. If your application requires those specific models, Cerebras is not a substitute.
- **Latency-insensitive batch jobs** — if you're running overnight sentiment analysis and don't care about time-to-completion, cost optimization on GPU infrastructure may beat speed optimization on Cerebras.
- **Fine-tuned proprietary models** — Cerebras runs the base open-weight models. If your competitive advantage is a fine-tuned model, you'd need to work with Cerebras enterprise to understand hosting options.

---

## The Revenue Concentration Problem

The IPO filing disclosed a customer concentration risk that is unusually stark. In 2025, **86% of Cerebras's $510 million revenue** came from two UAE-affiliated entities — with MBZUAI (Mohamed bin Zayed University of Artificial Intelligence) accounting for approximately **62%** alone. The company's stated transition from one dominant customer (previously the G42 group) to two (UAE entities plus OpenAI) is progress, but the revenue base remains highly concentrated in a single geopolitical relationship.

For builders evaluating Cerebras as infrastructure, this is a secondary concern — the API is a commercial cloud service and your workloads are isolated from the underlying customer structure. But it is the primary reason the stock dropped from its first-day close of $311 to the current ~$200 range. Public market investors are pricing in the execution risk of diversifying away from a 62% single-customer dependency.

---

## What the IPO Changes for Builders

Before May 14, Cerebras was a well-funded private company. A few things changed when it went public:

**Quarterly reporting.** The S-1 disclosed revenue, margins, customer concentration, and capital allocation in detail for the first time. Builders can now evaluate Cerebras against a standard financial framework rather than taking the company's marketing at face value.

**AWS Bedrock availability.** The March 2026 announcement that Cerebras WSE-3 capacity would be available through AWS Bedrock means the procurement question for enterprise developers shifts from "how do I set up a billing relationship with this startup" to "we already have an AWS contract."

**OpenAI validation.** A $20B commitment from OpenAI is the clearest possible signal that the technology works at scale. The company that spends the most on inference in the world is routing production workloads through Cerebras. That endorsement matters more than any benchmark.

**Continued operation.** A $5.55B raise gives Cerebras runway measured in years, not quarters. Infrastructure you build on will not disappear because the company ran out of money.

---

## The Competitive Landscape

Cerebras is not the only alternative inference provider. Builders should understand where it sits:

- **Groq (GroqCloud)**: The original speed-first inference provider, now restructuring after [licensing its LPU architecture to Nvidia](/builders-log/groq-nvidia-20b-lpu-deal-650m-neocloud-pivot-builder-guide/) for $20B in December 2025. Still operational, similar speed claims on smaller models, uncertain long-term trajectory.
- **Together AI, Fireworks, Replicate**: GPU-based inference clouds. Lower peak throughput but broader model selection, fine-tuning support, and established enterprise contracts.
- **AWS Bedrock, Azure AI Foundry, Google Vertex**: The hyperscaler managed inference layer. Slower than Cerebras but unified with existing enterprise infrastructure and available for both open and closed models.
- **Local inference (Ollama, llama.cpp)**: For truly latency-critical and privacy-sensitive workloads, the fastest inference is no network hop at all — but you are bounded by local hardware.

Cerebras occupies a specific niche: maximum throughput on open models in a managed cloud. For that specific use case, it is currently the fastest option available at any price.

---

## The Bottom Line

Cerebras's IPO was a financial event. The WSE-3's inference speed is a technical fact that predated the IPO and will not change based on what the stock does next week. The question for builders is whether speed is the binding constraint on your application's quality — and whether the open model catalog covers your use case.

If the answer to both is yes, the free tier is 24 million tokens per day. The migration from any OpenAI-compatible application is two lines of code. There is no reason not to benchmark it.

---

*Cerebras Systems (CBRS) is a public company trading on the Nasdaq. This is analysis of public information for builder decision-making, not investment advice.*
