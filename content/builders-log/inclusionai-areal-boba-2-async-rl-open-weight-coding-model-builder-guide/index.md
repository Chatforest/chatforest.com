---
title: "AReaL-boba-2: Ant Research's Open-Weight Async RL Coding Models (Builder Guide)"
date: 2026-06-18
description: "inclusionAI (Ant Research's RL Lab) released AReaL-boba-2, a family of open-weight coding models (8B, 14B, 32B) trained with asynchronous reinforcement learning that achieves 2.77x speedup over standard RL. The 14B hits 69.1 on LiveCodeBench v5. Apache 2.0. Here is what builders need to evaluate and deploy it."
content_type: "Builder's Log"
categories: ["Open Source AI", "Coding Models", "Self-Hosting", "Reinforcement Learning"]
tags: ["areal", "boba", "inclusionai", "ant-research", "open-weights", "apache-2.0", "async-rl", "coding-model", "vllm", "sglang", "ollama", "livecodebench", "codeforces", "qwen3", "reinforcement-learning", "swe-bench"]
sources_audited: 2026-07-31
---

**AReaL-boba-2** is a family of open-weight coding models from **inclusionAI** (Ant Group's reinforcement learning research team), [live on HuggingFace under Apache 2.0](https://huggingface.co/collections/inclusionAI/areal-boba-2-683f0e819ccb7bb2e1b2f2d5). The 14B model scores [69.1 on LiveCodeBench v5](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open) — beating much larger models like DeepSeek-R1 and OpenAI o3-mini on that benchmark — and the async RL training system behind it claims [up to a 2.77x throughput speedup](https://arxiv.org/abs/2505.24298) over synchronous RL training. The engineering behind it is worth understanding.

This guide covers what the models are, how the async RL training system works, benchmark numbers, deployment options, and what builders should actually do with them.

---

## What inclusionAI Is

[inclusionAI](https://github.com/inclusionAI) is the open-source AI organization of [Ant Group](https://www.scmp.com/tech/article/3361287/fintech-firm-ant-international-raises-us12b-fuel-global-growth), Alibaba's fintech affiliate (spun off from Alibaba in 2011). The AReaL project specifically comes out of Ant Group's RL Lab, working with Tsinghua University's Institute for Interdisciplinary Information Sciences, per the [AReaL paper's author list](https://arxiv.org/abs/2505.24298). The team previously released [AReaL](https://github.com/inclusionAI/AReaL), an open and reproducible framework for large-scale RL training of LLMs — all code, datasets, and training recipes public. The first milestone release, [v0.2 "Boba" (March 2025)](https://github.com/areal-project/AReaL/blob/main/blog/AReaL_v0_2.md), focused on math reasoning; AReaL-boba-2 is the coding-focused successor described in the [boba² technical report](https://arxiv.org/abs/2505.24298).

The research paper is available at [arXiv:2505.24298](https://arxiv.org/abs/2505.24298).

---

## The Model Family

All AReaL-boba-2 models use [**Qwen3**](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open) as the base (Alibaba's open-weight frontier series) and apply async RL post-training specialized for coding tasks.

| Model | Params | License | Weights |
|---|---|---|---|
| AReaL-boba-2-8B | 8B | Apache 2.0 | Public (8B-Open) |
| AReaL-boba-2-14B | 14B | Apache 2.0 | Public (14B-Open) |
| AReaL-boba-2-32B | 32B | Apache 2.0 | Public |

The `-Open` suffix variants (8B-Open, 14B-Open) are fully open-weight releases — weights downloadable directly from HuggingFace. The non-Open 8B and 14B may use a small amount of internal training data on top of the released recipe.

HuggingFace collection: [`inclusionAI/areal-boba-2-683f0e819ccb7bb2e1b2f2d5`](https://huggingface.co/collections/inclusionAI/areal-boba-2-683f0e819ccb7bb2e1b2f2d5)

---

## The Core Technical Story: boba² Async RL

Standard RL training for LLMs uses a synchronous pipeline: generate rollouts, wait, train, wait, repeat. The generation and training steps block each other. At scale across hundreds of GPUs, idle time compounds.

The boba² system (pronounced "double boba") decouples these stages completely:

- **Decoupled generation and training pipeline** — both stages run simultaneously, not sequentially
- **Decoupled PPO loss** — a system-algorithm co-design change ([Eq. 5 in the paper](https://arxiv.org/abs/2505.24298)) that separates the sampling ("behavior") policy from a recent proximal policy, which is what makes asynchronous updates on stale rollouts mathematically stable
- **Result: [up to 2.77x throughput improvement](https://arxiv.org/abs/2505.24298)** versus synchronous training systems (compared against VeRL and a synchronous AReaL baseline), with no benchmark performance drop

For the results reported in the boba² paper, the generation backend is [SGLang v0.4.6](https://arxiv.org/abs/2505.24298), which leverages radix attention to improve throughput when sampling multiple responses from the same prompt — which RL training requires heavily. (In cases where SGLang errors — 32B-model or 64-node runs — the team substitutes vLLM v0.8.4.) Note this is newer than the backend used at the project's first "Boba" milestone, which [upgraded from vLLM 0.6.3 to SGLang v0.4.0](https://github.com/areal-project/AReaL/blob/main/blog/AReaL_v0_2.md) back in March 2025.

That same earlier milestone release describes the data-transfer design: [NCCL with GPU-Direct RDMA over InfiniBand/RoCE](https://github.com/areal-project/AReaL/blob/main/blog/AReaL_v0_2.md), keeping generation-to-training data movement overhead under 3 seconds even in a 1,000-GPU cluster.

Multi-turn agentic RL training is also present as an [experimental feature of the framework](https://github.com/inclusionAI/AReaL) — it can train models on multi-step tool-using trajectories, not just single-turn code generation — but the released AReaL-boba-2 weights were not trained with it; it's listed as future work, not a shipped capability.

---

## Benchmark Performance

### Coding Benchmarks

The 14B model result is the most documented:

| Benchmark | AReaL-boba-2-14B | Notes |
|---|---|---|
| [LiveCodeBench v5 (LCB-v5)](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open) | **69.1** | SOTA in the 14B weight class at release |
| [Codeforces](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open) | 2044 rating / 98.2 percentile | Competitive programming problems |
| [CodeContests](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open) | 46.1 | [DeepMind's competitive-programming dataset](https://arxiv.org/abs/2203.07814) |

For context: the [model card](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open) shows this 69.1 LCB-v5 score beating DeepSeek-R1 (64.3) and OpenAI o3-mini-medium (66.3) — both much larger models. The published evaluation command uses temperature 1.0 and a max of 32,768 generated tokens; the model card does not document a samples-per-problem count.

The 32B model's specific LCB-v5 score is not disclosed in its [model card](https://huggingface.co/inclusionAI/AReaL-boba-2-32B), and the card does not make any comparison claim about the 32B model relative to DeepSeek-R1 or o3-mini — that comparison in the 14B card's benchmark table is specifically about the 14B model.

What is confirmed: the open-weight variants are legitimate and the benchmark numbers above for 14B are documented on the [model card](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open). (An earlier draft of this guide claimed a model called "Boba by stealth" was topping a coding arena leaderboard on llm-stats.com. That claim could not be verified against llm-stats.com's actual leaderboard pages or any other source, and has been removed.)

---

## Deployment

### Hardware Requirements

| Model | FP16 VRAM | Quantized (Q4) |
|---|---|---|
| 8B | ~16 GB | ~6 GB (runs on RTX 3080) |
| 14B | ~28 GB | ~10 GB (runs on RTX 3090) |
| 32B | ~64 GB | ~22 GB (runs on A10G or 2× consumer GPU) |

### vLLM (recommended for API serving)

```bash
pip install vllm
vllm serve "inclusionAI/AReaL-boba-2-14B-Open" --port 8000
```

The server exposes an OpenAI-compatible API at `http://localhost:8000/v1/`.

### SGLang (recommended for high-throughput RL or multi-sample workloads)

```bash
pip install sglang
python3 -m sglang.launch_server \
    --model-path "inclusionAI/AReaL-boba-2-14B-Open" \
    --host 0.0.0.0 \
    --port 30000
```

SGLang's radix attention is particularly effective when you need to sample multiple completions from the same prompt prefix — common in agent loop patterns that retry or score multiple candidate solutions.

### Transformers (quickstart)

```python
from transformers import pipeline

pipe = pipeline(
    "text-generation",
    model="inclusionAI/AReaL-boba-2-8B-Open",
    device_map="auto"
)

result = pipe(
    "Write a Python function that finds all prime numbers up to n using the Sieve of Eratosthenes.",
    max_new_tokens=2048,
    temperature=1.0,
    do_sample=True
)
print(result[0]["generated_text"])
```

### Ollama / llama.cpp

inclusionAI has not published official GGUF quantizations, but community conversions exist, e.g. [`mradermacher/AReaL-boba-2-32B-GGUF`](https://huggingface.co/mradermacher/AReaL-boba-2-32B-GGUF) and [`DevQuasar/inclusionAI.AReaL-boba-2-8B-Open-GGUF`](https://huggingface.co/DevQuasar/inclusionAI.AReaL-boba-2-8B-Open-GGUF). Pull one via Ollama, or convert the original weights yourself with `llama.cpp/convert_hf_to_gguf.py`. [Docker Model Runner](https://docs.docker.com/ai/model-runner/) can also pull a community GGUF repo directly:

```bash
docker model run hf.co/mradermacher/AReaL-boba-2-32B-GGUF:Q4_K_M
```

---

## Evaluation Against Your Own Codebase

The team released the full evaluation suite alongside the model:

```bash
git clone https://github.com/inclusionAI/AReaL
cd AReaL/evaluation

python eval_and_aggregate.py \
  --model_path inclusionAI/AReaL-boba-2-14B-Open \
  --output_path ./results \
  --data_names aime24,aime25,codeforces,lcb_v5 \
  --prompt_type qwen3-think-pure \
  --temperature 1.0 \
  --max_gen_tokens 32768
```

For your own code evaluation tasks, swap `--data_names` for a custom dataset that mirrors your actual production problem distribution.

---

## Builder Patterns

### Pattern 1: Local coding agent on single A10G

The 14B-Open model fits in 28GB FP16 — within reach of a single A10G instance on most cloud providers. Serve via vLLM and route coding tasks from your agent orchestrator to it instead of a frontier API:

```python
import openai

client = openai.OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="not-needed"
)

response = client.chat.completions.create(
    model="inclusionAI/AReaL-boba-2-14B-Open",
    messages=[
        {"role": "user", "content": "Refactor this function to eliminate the O(n²) loop:\n\n" + your_code}
    ],
    max_tokens=4096,
    temperature=0.7
)
```

At an A10G spot price of roughly $0.30-0.50/hour, the effective cost per query is sub-cent for most coding tasks — competitive with Claude Sonnet API pricing for high-volume workloads.

### Pattern 2: Competitive programming / algorithmic challenge agent

AReaL-boba-2 was trained specifically on Codeforces and CodeContests data. If you are building a tool that solves or generates competitive-programming-style algorithmic problems (interview prep tools, code challenge platforms, CS tutoring), this model has domain-specific RL training that frontier general models lack.

```python
SYSTEM = """You are an expert competitive programmer. 
Think step by step. Use <think> tags for your reasoning. 
Output only the final solution in the code block."""

# Sample multiple solutions and pick the one that passes test cases
responses = [
    client.chat.completions.create(
        model="inclusionAI/AReaL-boba-2-14B-Open",
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": problem_statement}],
        temperature=1.0,
        max_tokens=8192
    )
    for _ in range(8)  # sample 8, score against test cases
]
```

This "sample then verify" pattern mirrors exactly how the model was trained — high-temperature sampling followed by outcome-based scoring.

### Pattern 3: Fine-tune on your own code data (Apache 2.0 permits this)

The AReaL training framework is fully open. You can run RL fine-tuning on your own proprietary codebase:

1. Collect your internal code generation tasks (function stubs + expected behavior)
2. Write a reward function that runs your test suite and returns +1 / -1
3. Train with the AReaL framework starting from AReaL-boba-2-8B-Open weights

The released [`AReaL-boba-2-RL-Code`](https://huggingface.co/datasets/inclusionAI/AReaL-boba-2-RL-Code) dataset (on HuggingFace) shows the expected data format. The models are released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0), which permits derivative model use in closed commercial products.

---

## What This Does Not Cover

- **SWE-bench Verified**: No scores published for AReaL-boba-2. The model excels at algorithmic coding (LCB-v5, Codeforces) but SWE-bench requires repository-level multi-file context, which is a different skill. Evaluate before assuming parity with [Claude Opus 4.8's 88.6%](https://llm-stats.com/benchmarks/swe-bench-verified) on that benchmark.
- **Long-context file tasks**: The context window is 32,768 tokens maximum — fine for most function-level tasks, but not repository-scale analysis. For that, consider [GLM-5.2](https://docs.z.ai/guides/llm/glm-5.2) (1M-token context) or [Gemini 3.1 Pro](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-pro-on-gemini-cli-gemini-enterprise-and-vertex-ai) (also 1M-token context) instead.
- **Multi-turn agentic RL**: The framework supports it experimentally, but the released model weights were not trained with it. This is a future capability, not a current one.

---

## What to Watch

- **32B benchmark disclosure**: Exact LCB-v5 and Codeforces scores for the 32B model not yet published as of this writing.
- **inclusionAI public positioning**: The team is associated with Ant Group but has not made a high-profile branded announcement. A public launch or paper presentation could raise the profile of these models significantly.
- **Multi-turn agentic RL stabilization**: If the experimental multi-turn training matures, AReaL-boba-2 (or a successor) could become a strong base for tool-using coding agents trained on your specific workflow data.

---

## The Bottom Line

AReaL-boba-2 is a strong open-weight coding model family: the non-Open [14B model achieves 69.1 on LiveCodeBench v5](https://huggingface.co/inclusionAI/AReaL-boba-2-14B-Open) under Apache 2.0, the 14B-Open variant fits on a single A10G, and the fully open [AReaL training framework](https://github.com/inclusionAI/AReaL) means you can fine-tune it further. For builders running high-volume coding tasks or evaluating self-hosted alternatives to frontier APIs, it's worth including in your evaluation set — just verify it against your own workload before assuming it beats every other open-weight competitor in its size class, since no independent cross-model comparison is cited here.
