---
title: "Groq — The Fastest LLM Inference API (2026 Review)"
date: 2026-05-07T14:00:00+09:00
description: "Groq reviewed: custom LPU hardware delivers 2,100+ tokens/sec on Llama 3 8B. OpenAI-compatible API, Llama 4 support, Whisper at 189x real-time. NVIDIA acquired for $20B. Rating: 4/5."
og_description: "Groq (groq.com): a custom-silicon cloud inference API built on the Language Processing Unit (LPU) — an ASIC with 80 TB/s on-chip SRAM bandwidth that eliminates the memory-bandwidth bottleneck that limits GPU inference. Delivers 2,100+ tokens/sec on Llama 3 8B and 189x real-time Whisper transcription. OpenAI-compatible API. Llama 4 Scout (10M context), Llama 4 Maverick (1M context), Gemma 2 9B. NVIDIA signed a $20B licensing/acquihire agreement in December 2025 — industry validation at scale, but 90% of Groq's engineering team moved to NVIDIA, raising platform continuity questions. No custom models. Enterprise LoRA only. 30+ reported outages over 6 months. Free tier: 30 RPM / 6,000 TPM. Rating: 4/5."
card_description: "Groq (groq.com) is a cloud LLM inference API built on the Language Processing Unit (LPU) — a custom ASIC with 230MB of on-chip SRAM and 80 TB/s internal bandwidth that eliminates the memory-bottleneck limiting GPU inference. **2,100+ tokens/sec on Llama 3 8B. Whisper at 189x real-time.** OpenAI-compatible API; drop-in for any existing OpenAI integration. Model catalog includes Llama 4 Scout (10M context window), Llama 4 Maverick (1M context), Llama 3.3 70B, Gemma 2 9B, Whisper Large v3. LangChain, LlamaIndex, LiteLLM, Vercel AI SDK all have native Groq integrations. **December 2025: NVIDIA agreed to a $20B licensing deal** — industry validation of LPU technology, but ~90% of engineering staff joined NVIDIA, creating platform continuity uncertainty. No custom models on public API. Fine-tuning not available; LoRA inference only for enterprise. Batch API (50% discount) and prompt caching on paid tiers. 30+ outages reported over 6 months. Part of our **Developer Tools** category. Rating: 4/5."
last_refreshed: 2026-05-07
categories: ["/categories/developer-tools/"]
---

In late 2024, Groq's speed demos were going viral among developers who had spent years waiting for LLM responses that felt interactive. Tokens streaming at 2,000+ per second made the gap between human reading speed and generation speed basically disappear. GPU-based inference providers took notice.

In December 2025, NVIDIA signed a $20 billion licensing and acquihire agreement with Groq — the largest deal in NVIDIA's history. Bank of America analysts called it "recognition that while GPU dominated AI training, the rapid shift towards inference could require more specialized chips." That validation arrived at a cost: roughly 90% of Groq's engineering team, including founder Jonathan Ross, joined NVIDIA. GroqCloud continues to operate. Its long-term independence is a reasonable thing to wonder about.

The technology, however, is not in question. Part of our **[Developer Tools category](/categories/developer-tools/)**.

---

## At a Glance

| | |
|---|---|
| **Service** | [GroqCloud](https://console.groq.com/) |
| **Hardware** | LPU (Language Processing Unit) — custom ASIC |
| **Founded** | 2016 |
| **Founder** | Jonathan Ross (created Google's first TPU) |
| **Funding** | ~$3.3B raised; $6.9B valuation (Sept 2025) |
| **NVIDIA deal** | $20B licensing/acquihire (Dec 24, 2025) |
| **API** | OpenAI-compatible (`api.groq.com/openai/v1`) |
| **Python SDK** | `pip install groq` |
| **GitHub** | [github.com/groq](https://github.com/groq) |
| **Free tier** | 30 RPM / 6,000 TPM / 14,400 RPD |
| **Data retention** | None by default (Zero Data Retention option) |

---

## The Core Technology: Why LPU Beats GPU on Inference

Transformer inference is memory-bandwidth-bound. Every token generation requires loading billions of model weights from memory, performing matrix multiplications, and writing KV-cache entries — over and over. Modern GPU HBM (High Bandwidth Memory) tops out at roughly 8 TB/s. That ceiling constrains how fast you can generate tokens, regardless of how many CUDA cores you have available.

Groq's Language Processing Unit takes a different approach. The LPU integrates 230MB of on-chip SRAM as its primary weight storage — not a cache, but the actual working memory where model weights live during inference. On-chip SRAM delivers roughly 80 TB/s of internal bandwidth. That is approximately a 10x advantage over GPU HBM for the operations that dominate transformer inference.

The second architectural difference is scheduling. GPU execution is dynamically scheduled at runtime: the driver makes decisions about memory allocation, kernel launch order, and cache eviction on the fly, introducing nondeterministic overhead. The LPU uses static scheduling — execution graphs are compiled ahead of time, so there are no runtime memory controller decisions, no cache misses caused by unexpected access patterns, and no scheduler stalls. The result is consistent, predictable latency, not just fast average latency.

Groq calls this combination — SRAM-resident weights plus static scheduling — the reason why its time-to-first-token is consistently low under load, not just in best-case benchmarks. Developers who have switched from GPU-based APIs frequently report that the "feel" of Groq is different: the first token arrives fast and the stream is smooth.

The LPU is inference-only. It cannot train models. It is not reconfigurable for general ML workloads. The specialization is the source of its performance.

---

## Performance: Real Numbers

Groq's published inference speeds (broadly verified by third-party benchmarks):

| Model | Groq (tokens/sec) |
|---|---|
| Llama 3.1 8B | ~2,100 |
| Gemma 2 9B | ~2,800 |
| Llama 3.3 70B (speculative decoding) | ~1,660 |
| Mixtral 8x7B | ~727 |
| Llama 4 Scout | ~460+ |
| Whisper Large v3 | 189× real-time |

For context: a typical GPU endpoint (H100) returns 100-150 tokens/second on a 70B model and 280-450 tokens/second on an 8B model. Groq is roughly 5-7x faster on the smaller models, and the TTFT consistency advantage is even more pronounced under concurrent load.

**Where the edge matters most:** real-time chat, voice pipelines (fast Whisper + fast generation in sequence), agentic loops where each step waits on a generation, and RAG Q&A where users expect conversational speed. For batch processing where latency doesn't matter, the Groq advantage is less relevant.

**Cerebras comparison:** Cerebras (wafer-scale silicon) now reports ~2,988 tokens/second on certain large model configurations, which is technically higher throughput than Groq on some benchmarks. Cerebras has narrower model support and higher minimum commitments. Groq has better time-to-first-token consistency and lower entry cost. Both are genuinely faster than GPU alternatives for the models they support.

---

## GroqCloud: API Design and Model Catalog

GroqCloud's API is a deliberate OpenAI clone. The base URL is `https://api.groq.com/openai/v1`. The chat completions format, streaming protocol, function calling schema, and JSON mode all mirror OpenAI conventions exactly. Migrating an existing OpenAI-based application to Groq is a two-line change: update the base URL and swap the API key.

```python
from groq import Groq

client = Groq()  # reads GROQ_API_KEY from env

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": "Explain KV cache in one sentence."}]
)
```

**Official SDKs:** Python (`pip install groq`, mirrors the openai package structure), TypeScript/Node.js (`npm install groq-sdk`), and a Vercel AI SDK provider (`@ai-sdk/groq` for Next.js applications).

**Ecosystem integrations:** LangChain has a native `ChatGroq` class via `langchain-groq`. LlamaIndex, LiteLLM (as one of its many providers), and Composio all support Groq natively. Any tool that supports OpenAI-compatible endpoints works with Groq without code changes.

**Model catalog (May 2026):**

| Model | Context | Notes |
|---|---|---|
| Llama 4 Scout | 10M tokens | Multimodal (text + image), MoE 17B active / 109B total |
| Llama 4 Maverick | 1M tokens | Multimodal, 128 experts, 17B active / 400B total |
| Llama 3.3 70B Versatile | 8K | Text only; strong instruction following |
| Llama 3.1 8B Instant | 8K | Fast, cheap, good for high-volume tasks |
| Gemma 2 9B | 8K | Google's efficient open model |
| GPT-OSS 120B | 8K | OpenAI's open-weight release |
| Llama Guard 3 8B | 8K | Content moderation |
| Whisper Large v3 | — | ASR; 189× real-time |
| Whisper Large v3 Turbo | — | Faster, slightly lower accuracy |

The Llama 4 models are the standout additions. Llama 4 Scout's 10-million-token context window is exceptional — enough for roughly 7 million words. Multimodal support (image + text) expands Groq beyond text-only use cases.

---

## Pricing

Groq offers a free tier with meaningful but strict limits: 30 requests per minute, 6,000 tokens per minute, and 14,400 requests per day, shared across the whole organization. This is enough for development and low-traffic prototyping; it hits its ceiling quickly at production scale.

Paid tiers remove RPM limits and unlock the batch API (50% cost reduction for non-time-sensitive workloads) and prompt caching (approximately halves input costs on repeated system prompts or document prefixes). Exact per-token pricing depends on the model; smaller models like Llama 3.1 8B are priced below most GPU-based competitors.

GroqRack — on-premise LPU hardware — exists for regulated industries that cannot send data to a cloud API. The entry cost is in the millions of dollars.

---

## The NVIDIA Deal: What It Means for GroqCloud

On December 24, 2025, NVIDIA and Groq announced a $20 billion licensing and acquihire agreement. The structure: NVIDIA licenses Groq's inference technology (non-exclusively), and approximately 90% of Groq's engineering team — including founder Jonathan Ross and president Sunny Madra — joins NVIDIA. Jonathan Ross and Sunny Madra joined NVIDIA. A new CEO, Simon Edwards (formerly Groq's CFO), now leads GroqCloud as an independent company. Groq shareholders received $7.6 billion in distributions in February 2026 (~$64/share).

The Groq 3 LPU chip, developed under the NVIDIA partnership, debuted at GTC 2026 as part of NVIDIA's Vera Rubin platform, targeting 1,500 tokens/second for agentic workloads.

**How to read this for production dependency decisions:**

The deal validates the technology — NVIDIA's $20B price is a very public acknowledgment that LPU-style inference acceleration is real and valuable. The risk is platform continuity: GroqCloud is now run by a skeleton financial/operations team, not the engineers who built the hardware. The company says GroqCloud will continue operating. Whether it will add new model families, expand hardware capacity, or match the feature pace of better-staffed competitors is less clear.

For non-critical workloads, prototypes, and latency-sensitive applications that can tolerate provider risk: Groq remains excellent. For production infrastructure where provider stability is a hard requirement: the NVIDIA transition is a reason to either maintain fallback providers (easy given OpenAI API compatibility) or monitor closely over the next two quarters.

---

## Limitations

**No custom models on the public API.** You run only what Groq has deployed. If your use case requires a fine-tuned variant, a domain-specific model, or a model not on the catalog, you need a different provider or self-hosted infrastructure.

**Fine-tuning is not available.** LoRA inference is available only to enterprise customers through a separate process. You cannot upload and serve a LoRA adapter via the standard API.

**Free tier rate limits are strict.** 30 RPM and 6,000 TPM sounds reasonable until you are testing a multi-turn agent that makes 10 API calls per conversation. Developers frequently hit these limits within minutes of serious testing.

**Reliability has been imperfect.** StatusGator recorded 30+ incidents over the six months ending in April 2026. Most are brief availability or latency spikes rather than complete outages. Groq does not publish a specific uptime SLA for the public API tier. The last major acknowledged outage was February 7, 2026. This is meaningfully worse than the major cloud providers and worth factoring in for uptime-sensitive applications.

**Engineering team transition risk.** With ~90% of the founding engineering team now at NVIDIA, GroqCloud's ability to execute on hardware roadmap, reliability improvements, and new feature development is an open question. The technology is proven; the team continuity is not.

---

## vs. Self-Hosted Alternatives

| | Groq | vLLM | SGLang | Ollama |
|---|---|---|---|---|
| **Setup** | API key | GPU server required | GPU server required | Local install |
| **Speed** | 2,100+ TPS (8B) | 280-450 TPS (8B) | 300-500 TPS (8B) | 50-150 TPS |
| **Custom models** | No | Yes (any HF model) | Yes (any HF model) | Yes (any GGUF) |
| **Fine-tuning** | Enterprise LoRA only | Bring your own | Bring your own | Not applicable |
| **Data leaves org** | Yes (unless GroqRack) | No | No | No |
| **Ops burden** | Zero | Significant | Significant | Low |
| **Cost at scale** | Per-token pricing | GPU infrastructure | GPU infrastructure | Free |

Groq wins decisively on zero operations burden and raw speed. It loses on model flexibility, data sovereignty (for public API users), and cost efficiency at very high volume where GPU infrastructure amortizes well.

---

## Who Should Use Groq

**Strong fit for:**
- Applications where token streaming speed directly affects UX quality (chat, voice, real-time agents)
- Voice pipelines combining Whisper transcription with text generation — Groq's Whisper at 189× real-time makes this category exceptional
- RAG applications where fast generation completes the retrieval loop
- Developers prototyping with Llama 4 and wanting day-zero access with large context windows
- Any OpenAI-based application looking to reduce latency without a rewrite

**Weaker fit for:**
- Organizations that require custom fine-tuned models in production
- Regulated industries that cannot send data to a US cloud API (GroqRack exists, but is expensive)
- High-volume batch processing where cost efficiency matters more than latency
- Teams that need guaranteed SLA uptime for customer-facing infrastructure

---

## Verdict

Groq built real technology and earned genuine developer love by making LLM inference feel instant. The NVIDIA validation at $20 billion is not marketing — it is the largest company in the GPU market concluding that SRAM-based, statically-scheduled inference is worth betting on.

The honest uncertainty in 2026 is whether GroqCloud as a standalone service continues to improve or coasts. The engineering team that built the LPU is now at NVIDIA. The service runs; the roadmap is less clear. OpenAI API compatibility means you can add Groq as a provider and fall back to another in an afternoon — which is probably the right way to use it until platform continuity becomes clearer.

For latency-sensitive use cases with open-weight models, Groq is still the fastest easy option. Use it. Just don't build a single-provider dependency.

**Rating: 4/5** — Exceptional speed and developer experience, validated by a $20B industry endorsement. Half-point deduction each for platform continuity uncertainty post-NVIDIA deal and persistent reliability concerns (30+ incidents in 6 months). Another half-point for the walled-garden limitations (no custom models, restricted fine-tuning) that constrain advanced use cases.
