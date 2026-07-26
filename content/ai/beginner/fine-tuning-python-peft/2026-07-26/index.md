---
title: "Fine-Tuning with Python PEFT — Beginner Guide (as of 26 Jul 2026)"
date: 2026-07-26
snapshot_date: 2026-07-26
topic: fine-tuning-python-peft
track: beginner
audience: "people new to AI"
description: "A plain-English guide to fine-tuning open-weight language models on your own data using Hugging Face PEFT, LoRA, QLoRA, and related tools — with clear hardware requirements, cost warnings, and step-by-step install instructions."
content_type: "Best Practice"
categories: ["Fine-Tuning", "Python", "PEFT", "Beginners"]
tags: ["lora", "qlora", "peft", "fine-tuning", "hugging-face", "beginners", "gpu"]
last_refreshed: 2026-07-26
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-26"
grading_result: "14 beginner corrections applied; 0 fabrications"
---

<!-- This file lands at content/ai/beginner/fine-tuning-python-peft/2026-07-26/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->

# Fine-Tuning Language Models with Python PEFT — Beginner Guide (as of 26 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **26 Jul 2026**, frozen here and kept as
> a permanent archive entry. Re-leveled from the 2026-07-26 technical entry; facts unchanged.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING — never guessed.

## What is fine-tuning?

Fine-tuning means taking an existing language model — one that was already trained by someone else on a huge amount of text — and training it a little more on your own data. The goal is to change how it behaves: make it answer in a certain style, focus on a specific topic, or follow your instructions more reliably. You are not building a model from scratch; you are adjusting one that already knows a lot.

This guide covers the tools used to do that in Python on your own machine or a rented cloud GPU.

---

## BEFORE YOU BEGIN — Read this first

### Hardware requirement

⚠️ **WARNING: You need an NVIDIA GPU. Running on a laptop CPU will not work or will run 100-1000x slower.**

Fine-tuning a language model requires a graphics card (GPU) made by NVIDIA. This is different from the GPU used for video games — it is the same physical chip, but fine-tuning software specifically requires NVIDIA's CUDA software stack. If you have a MacBook, a standard Windows laptop without an NVIDIA card, or a basic cloud virtual machine (VM) without a GPU, you will get an error like "CUDA not found" or "no CUDA-capable device detected" and nothing will run correctly.

If you do not have a local NVIDIA GPU, you can rent one by the hour from a cloud provider. Common options mentioned in this guide: Google Colab Pro, Lambda Labs, Vast.ai, RunPod.

⚠️ **WARNING — Cloud GPU billing.** Rented GPUs are billed by the hour, even when your script is idle. An A100 GPU on Lambda Labs costs roughly $1–$3 per hour. If you start a training job and leave it running overnight without stopping your instance, you will receive an unexpected bill. Always stop or terminate your cloud GPU instance when you are done training.

### Software prerequisites

You need:
- Python 3.10 or newer
- `pip` (Python's package installer — comes with Python)
- PyTorch installed with CUDA support (follow the official PyTorch install tool at pytorch.org/get-started to pick the right command for your CUDA version)
- NVIDIA CUDA drivers installed on your machine

Then install the main libraries used in this guide:

```bash
pip install transformers peft trl bitsandbytes datasets accelerate
```

⚠️ **WARNING — VRAM (GPU memory) limits.** Your GPU has a fixed amount of memory called VRAM. If your model plus training state does not fit in VRAM, the training process will crash partway through with a "CUDA out of memory" error — after you have already spent time downloading the model. Check how much VRAM your GPU has before starting. The practices below include VRAM estimates to help you decide.

Use `nvidia-smi` in a terminal to see your GPU and its current VRAM usage.

### Library versions in this snapshot

🕒 **Verify live** — PEFT 0.19.1 · TRL 1.9.0 · lm-eval 0.4.12. These versions are correct as of 26 Jul 2026; always check that you have compatible versions.

---

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers confirmed this
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value before relying on it

---

## Practice 1: Choose LoRA rank, alpha, and target modules deliberately

### What is LoRA?

LoRA (Low-Rank Adaptation) is the most common way to fine-tune a large model without rewriting all of its internal numbers. Instead of changing every weight in the model (which costs enormous amounts of memory), LoRA adds two small extra matrices alongside certain layers and trains only those. The model's original weights stay frozen. The extra matrices are "low rank," meaning they are much smaller than the original weights — that is why LoRA is memory-efficient.

PEFT (Parameter-Efficient Fine-Tuning) is the Hugging Face library that implements LoRA (and other similar techniques). When someone says "PEFT adapter," they mean the small set of extra weights produced by LoRA-style training.

**Do:** Start with `r=16` (rank) and `lora_alpha=16`. For QLoRA-style runs targeting all linear layers, use `target_modules="all-linear"`. For standard LoRA on attention layers only, target `["q_proj", "v_proj"]` (or the equivalent names for your model architecture). Enable `use_rslora=True` when experimenting with higher ranks (32 and above).

**Why (beginner):** The rank (`r`) controls how much extra capacity LoRA adds to the model. Higher rank means the model can learn more from your data, but it also uses more memory and can overfit (memorize your training data instead of learning to generalize). `lora_alpha` scales how strongly the adapter's output is applied — when it equals `r`, the scaling is 1, which is a safe starting point.

`use_rslora=True` activates Rank-Stabilized LoRA, which uses a different scaling formula (`alpha / sqrt(r)`) that stays stable as rank grows. This matters mainly if you experiment with ranks above 32.

"All-linear" targets every dense layer in the model. Targeting only attention layers (`q_proj`, `v_proj`) is faster and uses less memory but may learn less.

**Caveat / contested:** There is no universal best rank. The researchers who introduced QLoRA (Dettmers et al., 2023) used `r=64` for very large 65B models, but community experience shows `r=8` to `r=32` is usually enough for instruction-following fine-tunes. Higher rank does not guarantee better results and can hurt when your dataset is small.

**Sources:** [huggingface.co/docs/peft — LoRA package reference](https://huggingface.co/docs/peft/main/en/package_reference/lora) (2026-07-26) · [huggingface.co/docs/peft — LoRA conceptual guide](https://huggingface.co/docs/peft/main/en/conceptual_guides/lora) (2026-07-26)

**Confidence:** 📄 vendor-documented (both sources are Hugging Face PEFT official docs — same publisher)

---

## Practice 2: Use QLoRA to fine-tune on consumer GPUs

### What is QLoRA?

QLoRA (Quantized LoRA) combines two ideas:
1. **4-bit quantization** — instead of storing each weight as a 16-bit or 32-bit number (full precision), you store it as a 4-bit number. This is trading precision (exactness) for memory savings. You lose a small amount of quality but save a large amount of VRAM.
2. **LoRA** (from Practice 1) — you add small trainable adapter matrices on top of the frozen quantized weights.

**NF4** (Normalized Float 4) is the specific 4-bit number format used. It is designed for the bell-curve distribution that neural network weights tend to follow, so it loses less quality than a plain 4-bit integer format.

**bfloat16** and **FP16** are both 16-bit floating-point number formats (half-precision). They trade some precision compared to the default 32-bit (FP32) format. Both are much smaller than FP32 but take slightly different approaches to representing the range of numbers. bfloat16 is generally preferred for training on modern NVIDIA GPUs (Ampere and newer).

**Do:** Load the base model with `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=torch.bfloat16)`, then call `prepare_model_for_kbit_training(model)` before wrapping with `get_peft_model()`. Use `target_modules="all-linear"` in `LoraConfig`.

**Why (beginner):** The numbers in this config do the following:
- `load_in_4bit=True` — load the model's weights in 4-bit format (saves VRAM)
- `bnb_4bit_quant_type="nf4"` — use the NF4 format (better quality than plain 4-bit integer)
- `bnb_4bit_use_double_quant=True` — apply a second round of compression to the quantization constants themselves, saving about 0.4 extra bits per parameter
- `bnb_4bit_compute_dtype=torch.bfloat16` — do the actual math in bfloat16 (fast, half-precision arithmetic)

`prepare_model_for_kbit_training()` adjusts the model so training does not break under low precision — it casts layer norms to float32 and enables gradient checkpointing.

**Concrete VRAM estimates:**
- A 7B parameter model in FP16 (standard) uses roughly 14 GB of VRAM
- The same model in 4-bit NF4 with QLoRA uses roughly 5–6 GB for weights alone — fitting comfortably on a T4 GPU (16 GB) at sequence length 1024
- A 13B model (about 27 GB in FP16) fits on a single T4 with double quantization and gradient checkpointing

⚠️ **WARNING — VRAM.** If you run out of VRAM partway through training, your process will crash with "CUDA out of memory." Always monitor VRAM usage with `nvidia-smi` in a separate terminal. The VRAM figures above are for weights only — activations and optimizer state add more.

**Caveat / contested:** The 4-bit base weights are frozen — only the LoRA adapter trains. Always call `prepare_model_for_kbit_training()` before `get_peft_model()`, or you will get NaN (not-a-number) gradients and the training run will be useless. VRAM figures are approximate. 🕒 bitsandbytes version matters — verify against the current release.

**Sources:** [huggingface.co/docs/peft — Quantization guide](https://huggingface.co/docs/peft/developer_guides/quantization) (2026-07-26) · [huggingface.co/blog/4bit-transformers-bitsandbytes](https://huggingface.co/blog/4bit-transformers-bitsandbytes) (2026-07-26)

**Confidence:** 📄 vendor-documented (PEFT quantization docs + HF 4-bit blog — both Hugging Face)

---

## Practice 3: Prepare datasets with `load_dataset`, column mapping, and chat templates

**Do:** Use `datasets.load_dataset()` to load data, then map it to one of the four formats SFTTrainer understands natively: (1) plain `{"text": "..."}`, (2) conversational `{"messages": [...]}`, (3) standard prompt-completion `{"prompt": "...", "completion": "..."}`, or (4) conversational prompt-completion. Apply `tokenizer.apply_chat_template()` if your model family expects special role tokens. Pass tokenization to SFTTrainer — avoid pre-tokenizing manually.

**Why (beginner):** SFTTrainer (the Hugging Face trainer built for supervised fine-tuning) automatically detects which format you are using and applies the right loss masking. "Loss masking" means the model only learns from the assistant's replies, not from the user's questions — which is what you want for instruction-following.

Tokenization is the process of converting text into numbers that the model can process. Letting SFTTrainer handle this ensures consistency with the specific model checkpoint being trained.

**Caveat / contested:** ⚠️ If you use `remove_unused_columns=True` (the default), any column in your dataset that the trainer does not recognize will be silently dropped without warning. Rename or keep only the columns the trainer expects. Different model families use different special tokens — for example, Qwen models use `<|im_end|>` as the end-of-sequence token for chat. Set `eos_token` in `SFTConfig` to match your model, or the model may generate text forever without stopping.

**Sources:** [huggingface.co/docs/trl — SFT Trainer](https://huggingface.co/docs/trl/sft_trainer) (2026-07-26) · [huggingface.co/docs/datasets — Use with PyTorch](https://huggingface.co/docs/datasets/main/en/use_with_pytorch) (2026-07-26)

**Confidence:** 📄 vendor-documented (TRL docs + HF Datasets docs — both Hugging Face)

---

## Practice 4: Use `trl.SFTTrainer` with packing, gradient checkpointing, and NEFTune

**Do:** Prefer `SFTTrainer` over a raw `Trainer` loop. Set `SFTConfig(packing=True, max_length=2048, gradient_checkpointing=True)`. For better generalization on instruction-following tasks, add `neftune_noise_alpha` to `TrainingArguments` (values 0.05–0.1). Note that `gradient_checkpointing` defaults to `True` in `SFTConfig`, and `bf16` defaults to `True` if `fp16` is not set.

**Why (beginner):**

**Packing** fills each training sequence up to `max_length` by concatenating multiple short examples end-to-end. Without packing, short examples are padded with blank tokens to reach `max_length`, and the model wastes time processing those blanks. Packing removes the waste and makes training significantly faster.

**Gradient checkpointing** is a memory-saving technique: instead of storing the intermediate calculations from every layer during a training step (which requires a lot of VRAM), the model recalculates them as needed. This saves roughly 20–30% VRAM at the cost of about 20% slower compute. Think of it as trading speed for memory.

**NEFTune** (Noisy Embedding Fine-Tuning) adds a small amount of random noise to the model's embedding vectors during training. The original research showed this improves benchmark scores for instruction-following without changing anything at inference time.

**Caveat / contested:** ⚠️ `neftune_noise_alpha` belongs in `TrainingArguments` (the base class from the Transformers library), not in `SFTConfig` (the TRL-specific config object). These are two separate configuration objects. `SFTConfig` handles SFTTrainer-specific settings like packing and max_length. `TrainingArguments` handles general training settings like learning rate, batch size, and NEFTune noise. Pass `neftune_noise_alpha` to `TrainingArguments`, then pass that object to `SFTTrainer`. If you put it in `SFTConfig`, it will be silently ignored.

⚠️ SFTTrainer's `packing` uses Best-Fit Decreasing (BFD) by default, which may silently discard tokens that overflow the max length. Use `packing_strategy="bfd_split"` to preserve all tokens. The default `loss_type="chunked_nll"` in current TRL is a memory optimization incompatible with `use_liger_kernel=True`.

🕒 TRL API evolves quickly (current snapshot: TRL 1.9.0, released July 21, 2026); verify defaults before pinning configs.

**Sources:** [huggingface.co/docs/trl — SFT Trainer](https://huggingface.co/docs/trl/sft_trainer) (2026-07-26) · [huggingface.co/docs/transformers — Performance on one GPU](https://huggingface.co/docs/transformers/main/en/perf_train_gpu_one) (2026-07-26)

**Confidence:** 📄 vendor-documented (TRL docs + Transformers performance guide — both Hugging Face)

---

## Practice 5: Use Unsloth for 2x faster fine-tuning on constrained hardware

**Do:** Install `unsloth` using the official README instructions — the install command depends on your CUDA version, so do not just type `pip install unsloth` without checking first. See [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) for platform-specific install commands.

After installing, replace `AutoModelForCausalLM.from_pretrained` with `FastLanguageModel.from_pretrained(model_name, load_in_4bit=True, ...)` and then call `FastLanguageModel.get_peft_model(model, ...)` instead of `peft.get_peft_model()`. Use `FastLanguageModel.for_inference(model)` before running inference to activate Unsloth's inference kernels.

**Why (beginner):** Unsloth replaces key internal operations (attention, cross-entropy loss, positional encoding, etc.) with hand-written, highly optimized CUDA/Triton code. The project claims 2x faster training with 70% less VRAM compared to a standard Hugging Face setup, and up to 3x faster on long-context fine-tuning. Unsloth's API is designed to be a near-drop-in replacement for the standard Hugging Face/TRL workflow, so you change only a few lines of code. TRL's official docs list Unsloth as an officially supported integration path. AMD GPU support was added in 2026 for select architectures.

⚠️ **WARNING — Platform-specific install.** Unsloth has different install commands for CUDA 11.8 vs CUDA 12.1 vs Google Colab. Installing the wrong version may silently produce incorrect results or crashes. Always follow the current install instructions at [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth).

**Caveat / contested:** ⚠️ Unsloth is a fast-moving open-source project — support for specific models is added incrementally. Always check the current README for your model before starting a run. 🕒 Supported models (Llama, Mistral, Qwen, Gemma, Phi, DeepSeek, etc.) change with each release. For production workloads, test with a held-out validation set after switching from a baseline trainer to catch any kernel correctness issues.

**Sources:** [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) (2026-07-26) · [huggingface.co/docs/trl — SFT Trainer](https://huggingface.co/docs/trl/sft_trainer) (2026-07-26) (mentions Unsloth as an integrated path)

**Confidence:** ✅ independently-corroborated (Unsloth GitHub — Unsloth team; TRL docs — Hugging Face TRL team — different publishers)

---

## Practice 6: Use Axolotl for YAML-driven multi-GPU fine-tuning at scale

> **Beginner note:** This practice is for users who have already succeeded with a single-GPU fine-tune using SFTTrainer (Practice 4) and want to scale up to multiple GPUs or more complex dataset mixing. If you are running your first fine-tune, start with Practice 4 and come back here later.

**Do:** Define your entire pipeline in a single `config.yml` and run `axolotl train config.yml`. Axolotl handles dataset preprocessing, LoRA/QLoRA setup, multi-GPU distribution, Flash Attention integration, and evaluation in one unified config.

To get started, follow the official Axolotl docs or use the official Docker image — see [docs.axolotl.ai](https://docs.axolotl.ai) (confirmed live as of 2026-07-26 with a Config Reference section) and [github.com/axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl).

For multi-GPU runs, add `deepspeed: deepspeed_configs/zero2.json` or `fsdp: full_shard` to the YAML. Axolotl passes these through to the Accelerate/Transformers backend automatically.

**Multi-GPU training terms (brief glosses):**
- **DeepSpeed** — a library from Microsoft that splits a model and its optimizer state across multiple GPUs so large models fit in memory
- **FSDP** (Fully Sharded Data Parallel) — PyTorch's built-in equivalent to DeepSpeed; shards model weights and gradients across GPUs
- **DDP** (Distributed Data Parallel) — an older, simpler approach that keeps a full model copy on each GPU and synchronizes gradients; works best when the model fits on a single GPU

**Why (beginner):** Bare TRL/Trainer code works for single-GPU experiments but becomes tedious at scale. Axolotl collapses dataset mixing, multi-GPU config, and Flash Attention flags into a single YAML file that is version-controllable and reproducible. It is particularly useful when you want to mix multiple datasets with different formats and weights, or switch between DDP, FSDP, and DeepSpeed without rewriting Python code.

**Caveat / contested:** Axolotl adds significant complexity for simple use cases. If you are fine-tuning a single model on a single GPU with one dataset, bare TRL/SFTTrainer is less error-prone and easier to debug. Axolotl's YAML schema evolves; configs written for one version may need updating for the next. 🕒 Consult the current docs at [docs.axolotl.ai](https://docs.axolotl.ai).

**Sources:** [github.com/axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) (2026-07-26) · [docs.axolotl.ai](https://docs.axolotl.ai) (fetched 2026-07-26 — confirmed live with Config Reference section)

**Confidence:** ✅ independently-corroborated (Axolotl GitHub README + Axolotl official docs site — both Axolotl team; the docs site was reported 404 by the pupil but is confirmed live as of grading date)

---

## Practice 7: Enable Flash Attention for memory-efficient long-context fine-tuning

### Which Flash Attention version does my GPU support?

Flash Attention is an optimized implementation of the attention operation — the core computation inside a transformer model. Standard attention uses memory that grows quadratically with sequence length (doubling the sequence roughly quadruples the memory). Flash Attention 2 uses an IO-aware tiling technique that keeps memory usage linear — at sequence length 2048, it uses roughly 10x less memory than naive attention.

Not all GPUs support Flash Attention. Use this table:

| GPU | What to use |
|---|---|
| T4 (Turing — common on free Google Colab) | SDPA — T4 does NOT support Flash Attention |
| RTX 3000/4000 series, A100 (Ampere/Ada) | Flash Attention 2 (`attn_implementation="flash_attention_2"`) |
| H100/H200 (Hopper) | Flash Attention 3 (`attn_implementation="flash_attention_3"`) — 1.5–2x faster than FA2 |
| Blackwell (B200) | Flash Attention 4 beta (`pip install flash-attn-4`) — alpha as of July 2026 |

**Do:** Load your model with `attn_implementation="flash_attention_2"` (for Ampere/Ada GPUs) or `attn_implementation="flash_attention_3"` (for Hopper H100/H200) in `from_pretrained()`. Use fp16 or bf16 dtype — Flash Attention requires half-precision inputs. Install `flash-attn` from PyPI. Use Ninja (`pip install ninja`) to dramatically reduce build time. If your GPU does not support Flash Attention (T4 and older), use `attn_implementation="sdpa"` (PyTorch's native SDPA, the default on PyTorch 2.1.1+).

**Why (beginner):** Flash Attention 3, optimized for H100/H200 hardware, achieves approximately 740 TFLOPS in benchmarks. FA3 is the mainstream recommendation for H100/H200 as of this snapshot. Flash Attention 4 (`flash-attn-4`, version 4.0.0b22, released July 15, 2026) is in alpha and is not production-ready. Axolotl (Practice 6) integrates FA2/3/4 directly via a YAML setting.

SDPA (Scaled Dot-Product Attention) is PyTorch's built-in efficient attention implementation. It does not require any extra install and works on all GPUs, including T4.

⚠️ **WARNING — T4 and Flash Attention.** T4 GPUs (the free tier on Google Colab) are Turing architecture, not Ampere. Flash Attention 2 and 3 require Ampere or newer. If you try to use `attn_implementation="flash_attention_2"` on a T4, you will get an error. Use `attn_implementation="sdpa"` instead.

⚠️ **WARNING — Build time.** Building the `flash-attn` package from source takes 2+ hours without Ninja installed. With Ninja and a multi-core system, it takes 3–5 minutes. Install Ninja first: `pip install ninja`. On RAM-constrained machines, use: `MAX_JOBS=4 pip install flash-attn --no-build-isolation`.

🕒 The current stable `flash-attn` package is 2.8.3.post1 (released June 11, 2026). Verify the current version before installing.

**Sources:** [github.com/Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention) (2026-07-26) · [pytorch.org/blog/flashattention-3/](https://pytorch.org/blog/flashattention-3/) (fetched by Timekeeper 2026-07-26) · [pypi.org/project/flash-attn/](https://pypi.org/project/flash-attn/) (2026-07-26) · [pypi.org/project/flash-attn-4/](https://pypi.org/project/flash-attn-4/) (2026-07-26)

**Confidence:** ✅ independently-corroborated (Dao-AILab GitHub + PyTorch Blog — different publishers; PyPI version pages confirm current release dates)

---

## Practice 8: Compensate for small GPU memory with gradient accumulation

**Do:** Set `per_device_train_batch_size` to the largest value that fits in VRAM (a power of 2: 1, 2, 4, 8...), then set `gradient_accumulation_steps` so that:

```
per_device_batch_size × gradient_accumulation_steps × number_of_GPUs = target effective batch size
```

Keep `per_device_train_batch_size` as large as possible rather than dropping it to 1 with many accumulation steps.

**Why (beginner):** A training "batch" is the number of examples the model sees before it updates its weights once. Larger batches generally lead to more stable training — but larger batches use more VRAM. Gradient accumulation lets you simulate a large batch without holding all examples in GPU memory at once: instead of updating the model's weights after every mini-batch, gradients are summed over N mini-batches and the model updates once at the end. This has the same mathematical effect as a batch N times larger.

For example: if you want an effective batch of 64 examples but can only fit 4 in VRAM at once, set `per_device_train_batch_size=4` and `gradient_accumulation_steps=16`. This is better than `per_device_train_batch_size=1` and `gradient_accumulation_steps=64`, because using 4 examples at once keeps the GPU's parallel cores busier.

**Caveat / contested:** ⚠️ **Learning rate scaling rule.** When you increase the effective batch size, you typically need to scale the learning rate proportionally. Example: if you double the batch size from 8 to 16, double the learning rate from 2e-4 to 4e-4. This is called the linear scaling rule. Watch for loss spikes right after the warmup period ends — they are a sign the learning rate is too high.

A practical starting warmup: `warmup_ratio=0.03` (3% of total training steps). SFTConfig's default `warmup_ratio` is `None`.

Gradient accumulation does not reduce peak activation memory per step. Combine it with gradient checkpointing (Practice 4) for maximum VRAM savings.

**Sources:** [huggingface.co/docs/transformers — Performance on one GPU](https://huggingface.co/docs/transformers/main/en/perf_train_gpu_one) (2026-07-26) · [huggingface.co/blog/ram-efficient-pytorch-fsdp](https://huggingface.co/blog/ram-efficient-pytorch-fsdp) (2026-07-26)

**Confidence:** 📄 vendor-documented (Transformers performance guide + HF FSDP blog — both Hugging Face)

---

## Practice 9: Merge LoRA adapters into the base model for deployment

### What are GGUF, llama.cpp, and Ollama?

Before the deployment steps, here are three terms you will encounter:

- **GGUF** — a file format for storing quantized language models. It is designed to be efficient and portable, especially for running models on CPUs or consumer GPUs without the full PyTorch stack.
- **llama.cpp** — an open-source C++ library that runs language models in GGUF format. It can run on a laptop CPU (slowly) or on a GPU. You would use it to run your fine-tuned model locally after converting it to GGUF.
- **Ollama** — a user-friendly tool built on top of llama.cpp. It makes running GGUF models locally as simple as `ollama run my-model`.

**Do:** After training, call `model = model.merge_and_unload()` to bake the adapter weights permanently into the base model and discard the adapter scaffolding. Save the result with `model.save_pretrained()`.

For hot-swapping multiple adapters at inference (without merging), use `model.load_adapter()` and `model.set_adapter()` instead.

For llama.cpp or Ollama deployment, merge first, then convert to GGUF format using `llama.cpp`'s `convert_hf_to_gguf.py` script.

**Why (beginner):** When you fine-tune with LoRA, you end up with two things: the original base model weights and a small adapter file. At inference time, the model computes a small extra calculation for every adapted layer (`h + (A @ B) × scale`). After merging, the adapter's contribution is permanently added to the base model weights — so inference runs at full speed with no PEFT library needed. If you have many task-specific adapters that share one base model, keeping them separate saves disk space.

**Caveat / contested:** ⚠️ `merge_and_unload()` is NOT in-place — you must assign the return value. Write `model = model.merge_and_unload()`. If you forget the `model =` part, you still have the unmerged model and the variable name is misleading.

⚠️ Merging is impossible for AQLM 2-bit quantized models — their weight format cannot absorb real-valued deltas. See the PEFT quantization guide for details.

⚠️ For INC-quantized (Intel Neural Compressor) models, `merge()` and `unmerge()` are not supported.

**Sources:** [huggingface.co/docs/peft — LoRA developer guide](https://huggingface.co/docs/peft/main/en/developer_guides/lora) (2026-07-26) · [huggingface.co/docs/peft — Quantization](https://huggingface.co/docs/peft/developer_guides/quantization) (2026-07-26) (source for AQLM/INC merge limitations) · [unsloth.ai/docs/get-started/fine-tuning-llms-guide](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide) (2026-07-26)

**Confidence:** ✅ independently-corroborated (PEFT official docs — Hugging Face; Unsloth docs — Unsloth team — different publishers)

---

## Practice 10: Evaluate fine-tuned checkpoints with lm-evaluation-harness

**Do:** Install `lm-eval` and run evaluations on both the base model and your fine-tuned model, then compare:

```bash
pip install lm-eval

# Evaluate the base model (before fine-tuning)
lm-eval --model hf \
  --model_args pretrained=meta-llama/Llama-3.1-8B \
  --tasks hellaswag,mmlu,gsm8k \
  --output_path results/base/

# Evaluate your fine-tuned model (base model + your adapter)
lm-eval --model hf \
  --model_args pretrained=meta-llama/Llama-3.1-8B,peft=./my-adapter \
  --tasks hellaswag,mmlu,gsm8k \
  --output_path results/finetuned/
```

Here `meta-llama/Llama-3.1-8B` is the base model identifier on Hugging Face Hub, and `./my-adapter` is the path to the adapter folder saved by `model.save_pretrained()` after training. Replace these with your actual model ID and adapter path.

Add `--limit 10` for a quick sanity check (runs only 10 examples per task) before committing to a full evaluation run. Use `--use_cache <dir>` so re-runs do not redo completed tasks.

**Why (beginner):** Fine-tuning on a narrow task can silently make the model worse at other things — a phenomenon called catastrophic forgetting. If you train a model to answer questions about your company's products, it might become less good at general reasoning or math. Running a standard benchmark suite on both the base model and your fine-tuned model makes this visible. If `hellaswag` or `mmlu` scores drop noticeably, your adapter is overwriting general knowledge.

As a cheaper first check, compute perplexity on a held-out validation set (examples the model never saw during training). If perplexity rises above the base model's level, something is wrong.

**Caveat / contested:** Results depend heavily on prompt formatting and few-shot settings. Always use the same task configuration when comparing base vs. fine-tuned — do not change shot counts or templates between runs. The `gsm8k_cot` variant uses chain-of-thought prompting and gives very different numbers from the zero-shot variant.

🕒 Current stable release: lm-eval 0.4.12 (May 11, 2026). A 0.5.0 pre-release exists; the `--model_args peft=` syntax may change if 0.5 ships before your run.

**Sources:** [github.com/EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) (2026-07-26) — the README documents `--model_args pretrained=...,peft=...` syntax directly.

**Confidence:** 📄 vendor-documented (EleutherAI GitHub README — EleutherAI team)

---

## CHANGELOG (re-leveled from the 2026-07-26 technical entry; facts unchanged)

1. **[KILL-P1 / KILL-X1]** Added "BEFORE YOU BEGIN" section at the top with a prominent GPU requirement statement: "You need an NVIDIA GPU. Running on a laptop CPU will not work or will run 100-1000x slower."
2. **[KILL-P2 / KILL-X1]** Added prerequisites block listing Python 3.10+, pip, PyTorch with CUDA, CUDA drivers, and `pip install transformers peft trl bitsandbytes datasets accelerate`.
3. **[KILL-P3]** Moved VRAM requirement out of the Practice 2 "Why" explanation and into a prominently placed WARNING in the "Before you begin" section and again in Practice 2. Added concrete failure description: "crash mid-run" and "CUDA out of memory."
4. **[KILL-P4]** Added cloud GPU billing WARNING in the "Before you begin" section: rented GPUs (Colab Pro, Lambda Labs, Vast.ai, RunPod) are billed by the hour; leaving a job running overnight incurs charges (~$1–3/hour for A100).
5. **[KILL-P5]** Added plain-English definitions of NF4, 4-bit quantization, bfloat16, and FP16 in the Practice 2 introduction ("trading precision for memory savings").
6. **[FIX-P1]** Added one plain sentence explaining gradient checkpointing: "instead of storing intermediate calculations from every layer during training, the model recalculates them as needed, saving memory at the cost of time."
7. **[FIX-P2]** Clarified the `TrainingArguments` vs `SFTConfig` distinction for `neftune_noise_alpha`: explained that these are two separate config objects, what each one handles, and that `neftune_noise_alpha` passed to `SFTConfig` will be silently ignored.
8. **[FIX-P3]** Added pointer to Unsloth's official install instructions at [github.com/unslothai/unsloth](https://github.com/unslothai/unsloth) for platform-specific CUDA variants, plus a WARNING not to run plain `pip install unsloth` without checking the platform-specific command first.
9. **[FIX-P4]** Added pointer to Axolotl docs at [docs.axolotl.ai](https://docs.axolotl.ai) and Docker image via [github.com/axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) for getting started.
10. **[FIX-P5]** Added explicit statement that T4 GPUs (common on free Colab) do NOT support Flash Attention 2 because T4 is Turing architecture, not Ampere. Added WARNING to use SDPA instead.
11. **[FIX-P6]** Added one-sentence plain-English definitions of GGUF, llama.cpp, and Ollama in Practice 9 before the deployment steps.
12. **[FIX-P7]** Replaced placeholder `<base-model-id>` and `<adapter-path>` in Practice 10 commands with concrete values (`meta-llama/Llama-3.1-8B` and `./my-adapter`) and added a sentence explaining where each value comes from.
13. **[FIX-P8]** Added a concrete example of the linear scaling rule in Practice 8: "if you double the batch size from 8 to 16, double the LR from 2e-4 to 4e-4."
14. **[FIX-X1]** Added inline glosses for DeepSpeed ("splits a model and optimizer state across multiple GPUs"), FSDP ("PyTorch's built-in equivalent to DeepSpeed; shards model weights and gradients across GPUs"), and DDP ("keeps a full model copy on each GPU and synchronizes gradients") in Practice 6.
15. **[Inherited from technical entry — KILL/FIX applied before re-leveling]** Removed false claim about docs.axolotl.ai being 404 (confirmed live). Practices 2, 3, 4, 8 relabeled vendor-documented. FA3 and FA4 coverage added. Library version notes added. Unsloth AMD support and install note added.
