# Kimi K2.6 Is the Open-Source SWE-Bench Leader: 300 Sub-Agents, $0.95/M Input, Drop-In OpenAI API — Builder Setup Guide

> Kimi K2.6 from Moonshot AI leads SWE-Bench Pro at 58.6%, beats GPT-5.4 and Claude Opus 4.6, runs 300 parallel sub-agents, costs $0.95/$4.00 per million tokens, and is OpenAI API-compatible. Here's the builder setup guide and decision matrix.


Kimi K2.6 is a 1-trillion-parameter Mixture-of-Experts model from Beijing-based Moonshot AI, [released April 20, 2026](https://huggingface.co/moonshotai/Kimi-K2.6). Its weights are open-source under a [modified MIT license](https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE), it is OpenAI API-compatible, and per [Moonshot's own release announcement](https://forum.moonshot.ai/t/meet-kimi-k2-6-advancing-open-source-coding/369) it holds the top position among open-weight models on both SWE-Bench Pro (58.6%) and SWE-Bench Verified (80.2%). Independent benchmark aggregation confirms it edges out GPT-5.4 (57.7%) and Claude Opus 4.6 (53.4%) on SWE-Bench Pro specifically — see the [comparison table below](#benchmark-position) for sourcing.

The API costs [$0.95 per million input tokens](https://platform.kimi.ai/docs/pricing/chat-k26). This piece covers what the model is, how to set it up, when to reach for it, and what the compliance picture looks like. Part of the **[Builder's Log](/builders-log/)**.

---

## What Kimi K2.6 Is

K2.6 is the latest in Moonshot AI's K2 series, which has moved through K2, K2.5, and K2.6 since 2025. The architecture is a Mixture-of-Experts design: 1 trillion total parameters, 32 billion active per token during inference. That profile — large total capacity, modest active footprint — is the same pattern [DeepSeek's V4-Pro](https://deepseek.ai/deepseek-v4) (1.6T total / 49B active) and the Qwen 3 series use. (Note: DeepSeek's rumored "R2" reasoning model has not actually shipped as of this writing — DeepSeek's 2026 release was V4, not R2.)

**Key specs at a glance:**

| Parameter | Value |
|---|---|
| Architecture | MoE |
| Total parameters | 1 trillion |
| Active parameters per token | 32 billion |
| Context window | 256K tokens (262,144) |
| Native quantization | INT4 |
| Multimodal | Text, image, video input |
| Modes | Thinking / non-thinking; dialogue / agent |
| License | Modified MIT |
| HuggingFace | moonshotai/Kimi-K2.6 |

Specs above per [Moonshot's official Kimi K2.6 model card on HuggingFace](https://huggingface.co/moonshotai/Kimi-K2.6). K2.6 is natively multimodal — text, image, and video input are all supported. It also ships with an optional "thinking mode" that enables chain-of-thought reasoning, similar to the extended-thinking modes in Claude and o3.

---

## Benchmark Position

The headline number: **58.6% on SWE-Bench Pro**, a harder variant of SWE-Bench that requires models to resolve production-grade GitHub issues across unfamiliar, large codebases. Moonshot's own [SWE-Bench Pro forum notes](https://forum.moonshot.ai/t/about-swe-bench-pro/315) and [release announcement](https://forum.moonshot.ai/t/meet-kimi-k2-6-advancing-open-source-coding/369) report this score directly.

**SWE-Bench Pro comparison (April 2026):**

| Model | SWE-Bench Pro | Type |
|---|---|---|
| **Kimi K2.6** | **58.6%** | Open-weight |
| GPT-5.4 | 57.7% | Proprietary |
| Claude Opus 4.6 | 53.4% | Proprietary |

Comparison figures per [Moonshot's release announcement](https://forum.moonshot.ai/t/meet-kimi-k2-6-advancing-open-source-coding/369).

On the original SWE-Bench Verified, Kimi K2.6 scores **80.2%** ([HuggingFace model card](https://huggingface.co/moonshotai/Kimi-K2.6)) — the strongest result among open-weight models at the time of writing. For comparison, Alibaba's proprietary Qwen 3.6 Plus scores 78.8% and the open-weight Qwen3.6-27B scores 77.2% on the same benchmark, both below K2.6's result.

SWE-Bench Pro is designed to be less gameable than SWE-Bench Verified: it uses newer, less-represented repositories and strips the test harness that some models may have seen during training. The 1-point gap over GPT-5.4 on SWE-Bench Pro is within noise margin on any single run, but K2.6 replicating this score across multiple evaluation runs gives it a credible claim as the current open-source leader in agentic coding.

---

## Agent Swarm Capabilities

This is where K2.6 distinguishes itself from most open-weight models. Moonshot AI specifically engineered K2.6 for multi-agent orchestration. Per [Moonshot's release announcement](https://forum.moonshot.ai/t/meet-kimi-k2-6-advancing-open-source-coding/369):

- **300 parallel sub-agents** run **4,000 coordinated steps** per session (up from 100 sub-agents / 1,500 steps in K2.5)
- Long-horizon coding sessions with **4,000+ tool calls, over 12 hours of continuous execution**

The architecture supports long R&D task chains: an orchestrating agent allocates sub-tasks to 300 workers, which can spawn and close independently across the session without losing coordination state. This is meaningfully different from just running 300 API calls in parallel — K2.6 has explicit coordination primitives, not just parallel context management.

For builders running code-review pipelines, large-scale refactor tasks, or multi-repository agents, the 300-sub-agent ceiling matters. GPT-5.4 has no equivalent built-in swarm support; you build that yourself. Kimi provides the coordination layer natively.

---

## API Setup

The Kimi API is fully OpenAI-compatible: same endpoint structure, same tool-call format, same JSON mode. Migrating from GPT-4-turbo or GPT-5.4 is a base-URL change.

### Quick start

**1. Create an account and API key**

Sign up at [platform.moonshot.ai](https://platform.moonshot.ai), deposit at least $1 to activate your key, then generate an API key in the Console.

**2. Endpoint and model ID**

Per [Moonshot's official K2.6 quickstart guide](https://platform.kimi.ai/docs/guide/kimi-k2-6-quickstart):

```
Base URL: https://api.moonshot.ai/v1
Model ID: kimi-k2.6
```

**3. Drop-in OpenAI replacement (Python)**

```python
from openai import OpenAI

client = OpenAI(
    api_key="sk-...",           # your Kimi API key
    base_url="https://api.moonshot.ai/v1"
)

response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[
        {"role": "user", "content": "Write a Python function to parse a GitHub diff and extract changed file paths."}
    ]
)
print(response.choices[0].message.content)
```

**4. Enable thinking mode (optional)**

Thinking mode activates chain-of-thought reasoning and is priced separately (charged at output-token rates for reasoning tokens):

```python
response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[{"role": "user", "content": "..."}],
    extra_body={"thinking": {"type": "enabled"}}
)
```

**5. Tool calling**

K2.6 uses the OpenAI tool-call format exactly — `tools`, `tool_choice`, and `tool_calls` in the response. No schema changes required.

---

## Pricing

| Tier | Input | Output | Cache-miss input |
|---|---|---|---|
| K2.6 | $0.95/M | $4.00/M | $0.95/M |
| K2.6 cached | $0.16/M | — | — |
| K2.5 | $0.60/M | $3.00/M | $0.60/M |
| Web search | $0.005/call | — | + search-result tokens |

Rates per [Moonshot's official K2.6 pricing page](https://platform.kimi.ai/docs/pricing/chat-k26) and [tool-call pricing page](https://platform.kimi.ai/docs/pricing/tools). Automatic context caching is enabled by default. Cached input tokens cost $0.16/M — roughly 83% off the cache-miss rate. For agents that repeatedly prepend a large system prompt or a fixed codebase snapshot, caching substantially changes the cost math.

**Cost comparison for a 50K-token agentic coding session (input-heavy):**

| Model | Input cost (50K tokens) | Output cost (5K tokens) |
|---|---|---|
| GPT-5.4 ([$2.50/$15 per M](https://developers.openai.com/api/docs/models/gpt-5.4)) | $0.125 | $0.075 |
| Claude Opus 4.6 ([$5/$25 per M](https://www.anthropic.com/news/claude-opus-4-6)) | $0.25 | $0.125 |
| Kimi K2.6 ([$0.95/$4.00 per M](https://platform.kimi.ai/docs/pricing/chat-k26)) | $0.048 | $0.020 |
| Kimi K2.6 (cached, $0.16/M input) | $0.008 | $0.020 |

For pipelines that run hundreds of coding sessions per day, the pricing difference is not marginal. At scale, K2.6 can be roughly 2–3x cheaper than GPT-5.4 and 4–5x cheaper than Claude Opus 4.6 for the same throughput on this input/output mix.

---

## Self-Hosting

If you need air-gapped deployment — no external API calls, no data egress — K2.6 weights are on HuggingFace under a modified MIT license:

```
moonshotai/Kimi-K2.6
```

**Recommended serving stacks**: vLLM, SGLang, KTransformers — per [Moonshot's own deployment guidance](https://huggingface.co/moonshotai/Kimi-K2.6/blob/main/docs/deploy_guidance.md).

**Hardware**: Moonshot's deployment guide doesn't publish a single "minimum" spec — it gives example configs instead, including 8× NVIDIA L20 + 2× Intel Xeon 6454S (KTransformers+SGLang) and an H200 single-node setup with 8-way tensor parallelism. Third-party guides estimate the INT4-quantized weights need roughly 640GB of aggregate VRAM, putting 8× H100 80GB (or 8× H200) in the realistic range even for the quantized variant — plan hardware accordingly rather than assuming a 4-GPU setup will work. [Source: Moonshot deploy guide](https://huggingface.co/moonshotai/Kimi-K2.6/blob/main/docs/deploy_guidance.md).

K2.6 uses the same architecture as K2.5, so if you already have K2.5 deployment configs, they carry forward without modification.

Combined with Ollama for local model serving, K2.6 is one of the few frontier-grade coding models that can run fully offline — no internet access, no third-party telemetry, no compliance exceptions needed. Red Hat AI has [added Kimi K2.6 to its validated third-party model catalog for Red Hat OpenShift AI](https://www.redhat.com/en/blog/deploy-confidence-announcing-latest-validated-models-red-hat-ai) and published a [quantized NVFP4 variant on HuggingFace](https://huggingface.co/RedHatAI/Kimi-K2.6-NVFP4) — one signal that enterprise infrastructure teams are taking the self-hosted path seriously. (Note: this is Red Hat OpenShift AI, the model-serving platform — not OpenShift Dev Spaces, a separate cloud-IDE product.)

---

## License

The [modified MIT license](https://github.com/moonshotai/Kimi-K2/blob/main/LICENSE) permits commercial use, deployment, modification, and redistribution. One additional condition applies at large commercial scale: if a product or service using K2.6 exceeds **100 million monthly active users or $20 million in monthly revenue**, the UI must prominently display "Kimi K2" (the license text names the series, not the specific point-release string "Kimi K2.6"). Below those thresholds, standard MIT terms apply.

For most builders, the 100M MAU / $20M monthly revenue threshold is not a near-term constraint. For consumer apps that might reach that scale, build the attribution flag into your UI from the start — it is a display requirement, not a revenue share.

---

## Moonshot AI: Company Context

Kimi K2.6 comes from Moonshot AI, [founded in March 2023](https://en.wikipedia.org/wiki/Yang_Zhilin) by Yang Zhilin — an assistant professor at Tsinghua University who earned his PhD at Carnegie Mellon and previously worked at Meta AI (then Facebook AI Research) and Google Brain before returning to China. The company makes both the Kimi consumer chatbot and the Kimi API platform for developers.

As of June 2026, Moonshot AI is reporting strong growth:
- ARR reportedly [doubled from about $100M in March 2026 to over $200M in April 2026](https://techjacksolutions.com/ai-brief/moonshot-ais-revenue-doubled-in-six-weeks-now-its-preparing/) — roughly six weeks
- Kimi K2.6 is [the #2 LLM by volume on OpenRouter](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/) as of that report
- The company [raised $2 billion at a $20 billion valuation in May 2026](https://www.bloomberg.com/news/articles/2026-05-07/kimi-chatbot-maker-moonshot-ai-valued-at-20-billion-in-meituan-led-round) (led by Meituan)
- [Bloomberg reported June 8](https://www.bloomberg.com/news/articles/2026-06-08/china-s-moonshot-ai-seeks-30-billion-value-in-new-funding-talks) that Moonshot was in early talks for a third round targeting a $30 billion valuation — up from just over $4 billion in December 2025

That trajectory tells you something about user adoption. The Kimi chatbot subscription revenue is growing, and the API platform is seeing real usage volume. The company is not a research lab publishing papers — it is a product business building infrastructure revenue.

---

## Compliance Considerations

K2.6 is developed and operated by a Beijing-based company. For enterprise deployments, that raises two questions:

**Data residency**: The Kimi API routes through Moonshot AI's infrastructure in China. If your application handles EU personal data, US government data, healthcare records, or other regulated data categories, review whether the Kimi API endpoint is in-scope for your data processing agreements. The self-hosted path resolves this entirely.

**Supplier diversification**: Some US defense and government contractors are restricted from using Chinese-origin AI models in production. Check your organization's approved vendor list before deploying K2.6 via API in regulated contexts.

For builders without these constraints — startups, open-source projects, research, cost-sensitive SaaS applications — neither issue is typically blocking.

---

## When to Use Kimi K2.6

**Reach for K2.6 when:**
- You are running agentic software engineering pipelines (SWE-bench performance is the most direct signal here)
- You need 300+ parallel sub-agents or multi-step long-horizon coding sessions
- Your pipeline is cost-constrained and GPT-5.4 or Claude Opus is consuming significant budget
- You need air-gapped / on-premises deployment and want frontier-grade coding performance
- You want an OpenAI-compatible API with no migration friction

**Consider alternatives when:**
- Your organization has Chinese-origin model restrictions (use Claude Opus 4.6, GPT-5.4, or Gemini 3.1 Pro)
- You need the absolute best creative writing or long-form synthesis ([Claude Fable 5](https://www.anthropic.com/news/claude-fable-5-mythos-5), Anthropic's purpose-built creative-writing model, leads here)
- Your primary workload is not coding/agentic — K2.6 is optimized for SWE tasks, not general chat or customer service
- You need HIPAA BAA or FedRAMP compliance (neither is available via the Kimi API)

---

## The Bigger Picture

China's AI models have closed the gap with US frontier labs faster than most observers expected. Kimi K2.6 topping SWE-Bench Pro in April 2026, ahead of GPT-5.4 and Claude Opus 4.6, is not an outlier — [Qwen 3.6](https://theplanettools.ai/blog/qwen-3-6-alibaba-beats-google-gemma-4-coding-benchmarks-2026) and [DeepSeek V4](https://deepseek.ai/deepseek-v4) also compete at or near the frontier on specific benchmarks, often at dramatically lower API prices.

The pattern is consistent: Chinese labs optimize for specific, measurable dimensions (coding, SWE-bench, math), release weights openly, undercut API pricing, and build OpenAI-compatible endpoints. Builders who are indifferent to supplier geography and focused on specific workloads have more high-quality, low-cost options than existed six months ago.

Whether that pattern holds as compute access and regulatory pressure evolve is an open question. For now, K2.6 is a credible default for coding-heavy pipelines that want open-source optionality.

---

**Quick reference:**

- HuggingFace: `moonshotai/Kimi-K2.6`
- API endpoint: `https://api.moonshot.ai/v1`
- Model ID: `kimi-k2.6`
- Pricing: $0.95 input / $4.00 output / $0.16 cached input (per million tokens)
- Context: 256K tokens
- Agent swarm capacity: 300 sub-agents, 4,000 coordinated steps
- License: Modified MIT (attribution required above 100M MAU or $20M/month revenue)

