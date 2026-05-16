# Mistral Codestral Review — 22B Code Model, Fill-in-the-Middle, 32K Context

> Mistral Codestral (May 29, 2024) is a 22.2B parameter code-specialized model with native fill-in-the-middle training, 32K context, and 80+ language support. HumanEval 81.1%, MBPP 78.2%, RepoBench 34.0% — outperforms Code Llama 70B and DeepSeek Coder 33B on HumanEval at less than a third the parameters. Restricted by Mistral AI Non-Production License. Ollama: codestral. Rating: 4/5.


**At a glance:** Mistral Codestral, released May 29, 2024. 22.2B parameters. 32K context. Native fill-in-the-middle. 80+ languages. HumanEval: 81.1%. Mistral AI Non-Production License (not Apache 2.0). Ollama: `codestral`. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Mistral Codestral is [Mistral AI's](/reviews/mistral-ai-open-weight-llm-european-ai/) first code-specialized model, released May 29, 2024. Its central claims are two: first, that a 22-billion-parameter specialist can outperform 33–70B general-purpose models on code tasks; second, that fill-in-the-middle (FIM) capability, baked into pretraining rather than added post-hoc, makes it more useful than autoregressive-only models for the real-world developer workflow of IDE tab completion.

Both claims hold up. Codestral's HumanEval pass@1 of 81.1% outperformed Code Llama 70B (67%) and DeepSeek Coder 33B (~79%) at launch — a striking result for a model less than a third the size. Its RepoBench exact-match score of 34.0% was the best at launch, which Mistral attributed directly to the 32K context window (large enough to hold entire files). FIM worked as advertised in IDE integrations: Continue.dev and Tabnine added Codestral support at launch.

The complication is the license. Codestral ships under the **Mistral AI Non-Production License (MNPL)**, which allows research and testing but prohibits commercial use — including free-of-charge SaaS — without a separate paid agreement. This was a deliberate commercial decision by Mistral, and it sets Codestral apart from the Apache 2.0 models in their lineup. For individuals and researchers, the weights are accessible on Hugging Face. For production use, a commercial arrangement is required.

---

## Background: Why a Code Specialist

In mid-2024, the main open-weight code models were **Code Llama** (Meta, July 2023 — 7B/13B/34B, FIM-capable, 100K context in the Instruct variant), **DeepSeek Coder** (DeepSeek, October 2023 — 1B to 33B, FIM-capable, 87% code in training data), and **StarCoder2** (BigCode/Hugging Face, February 2024 — 3B/7B/15B, FIM-capable). All were competitive on benchmarks but had gaps.

Code Llama 70B scored 67% on HumanEval — strong for a general-to-code-adapted model, but the 70B scale limited deployment options. DeepSeek Coder 33B scored ~79% but required more memory. StarCoder2 was smaller and more accessible but topped out at 15B. None of the open-weight options at this scale had 32K context as standard.

Codestral's positioning: a 22B model that fits within the memory envelope most practitioners were already allocating for 7B models on server hardware (BF16: ~46GB; Q4: ~13GB), with benchmark numbers competitive with models 1.5–3× larger and a context window long enough for repository-scale tasks.

General-purpose models (Mistral 7B, Llama 3, even GPT-4) can write code — but without native FIM training, they cannot cleanly complete code when given a prefix and suffix (the cursor insertion scenario). Codestral is designed specifically for the cursor-insertion use case, making it more useful for IDE autocomplete than models trained only on left-to-right generation.

---

## Architecture

Codestral 22B v0.1 is a dense decoder-only Transformer. Mistral has not published the full architecture specification, but the following parameters are consistent across documentation and Hugging Face model card:

| Property | Value |
|---|---|
| Parameters | 22.2 billion |
| Context window | 32,768 tokens (32K) |
| Architecture | Dense decoder-only Transformer |
| Position encoding | RoPE |
| Training objective | Causal LM + fill-in-the-middle |
| Vocabulary | Not separately published; consistent with Mistral v0.x tokenizer |
| Precision | bfloat16 |
| VRAM (BF16) | ~46 GB |
| VRAM (Q4) | ~13 GB |

The FIM training objective is baked into pretraining, not added via instruction tuning. This matters because instruction-tuned FIM tends to be brittle — the model treats the prefix/suffix framing as a prompt format and can generate inconsistently when the code context doesn't match training patterns. Pretraining-time FIM means the model has deeply internalized the relationship between prefix, suffix, and the completion that belongs between them.

---

## Fill-in-the-Middle: How It Works

FIM is the distinguishing capability. Standard autoregressive generation produces text left to right: given a prefix, predict what comes next. In practice, developers rarely need that. They need the model to complete a function body when the function signature is above and a test is below, or to fill a missing section in the middle of a file.

FIM addresses this by rearranging the document during training:

```
[PREFIX]<code before cursor>[SUFFIX]<code after cursor>[MIDDLE]<completion><EOT>
```

The model sees both the prefix and suffix during training, so at inference time, it can condition its completion on what follows — not just what precedes.

**Inference format (Codestral API):**

```json
POST https://codestral.mistral.ai/v1/fim/completions
{
  "model": "codestral-latest",
  "prompt": "def factorial(n):\n    # TODO: implement this\n",
  "suffix": "\nassert factorial(5) == 120",
  "temperature": 0.2,
  "max_tokens": 256
}
```

The `prompt` field is the prefix (code before the cursor). The `suffix` field is the code after the cursor. Codestral generates what belongs between them and emits `<EOT>` when done. Mistral recommends a temperature of 0.2–0.3 for deterministic autocomplete scenarios.

This is distinct from the chat completion endpoint (`api.mistral.ai/v1/chat/completions`). Codestral has a dedicated FIM endpoint at `codestral.mistral.ai/v1/fim/completions`, and the model is also accessible via the standard chat interface for prompt-driven code generation tasks that don't require FIM.

---

## Benchmarks

Codestral's launch benchmarks:

| Benchmark | Codestral 22B | DeepSeek Coder 33B | Code Llama 70B | Llama 3 70B |
|---|---|---|---|---|
| HumanEval pass@1 | **81.1%** | ~79% | ~67% | ~76% |
| MBPP pass@1 | 78.2% | **80.2%** | 70.8% | 76.7% |
| RepoBench EM | **34.0%** | lower | lower | lower |
| CruxEval-O | **51.3%** | — | — | — |

The headline result is HumanEval: 81.1% at 22B, beating Code Llama 70B at less than a third the parameter count. This is the "code specialist beats generalist" argument in concrete numbers.

MBPP shows a different story — DeepSeek Coder 33B edges Codestral at 80.2% vs 78.2%. This makes the comparison more honest: Codestral is not uniformly dominant, and DeepSeek Coder 33B is a legitimate competitor at a cost of 50% more parameters.

RepoBench (repository-level code completion, requiring context across files) is where Codestral's 32K window pays off most clearly. All competitors at launch had smaller effective context windows, and their scores were lower. This is the benchmark most relevant to real-world repository work rather than isolated function generation.

CruxEval-O evaluates code output prediction — given a function and an input, what is the return value? 51.3% measures whether the model understands program execution semantics, not just code pattern matching.

---

## Language Support

Mistral states 80+ programming languages. Explicitly documented: Python, Java, C, C++, JavaScript, TypeScript, Bash, Swift, Fortran. The complete list was not published. In practice, coverage follows the distribution of public code repositories — languages with large GitHub footprints are better covered than niche languages regardless of Mistral's explicit enumeration.

The 80+ language claim puts Codestral in the same tier as Code Llama and DeepSeek Coder in breadth. The practical difference between "80 languages" and "100 languages" in terms of real-world utility is small — the quality of coverage for the top 20 languages matters more than the tail count.

---

## License: The MNPL Constraint

Codestral ships under the **Mistral AI Non-Production License (MNPL)**. This is the most consequential limitation in the model's profile.

What MNPL allows:
- Research and academic use
- Personal experimentation (narrowly defined: non-profit, non-commercial, unconnected to employment)
- Evaluation before purchasing a commercial license

What MNPL prohibits:
- Using the model in any commercial product or service
- Hosting it as a service for others, even free of charge
- Using it in connection with any employment or business purpose without a paid agreement
- Creating revenue or commercial value of any kind from the model's outputs

The weights are on Hugging Face (`mistralai/Codestral-22B-v0.1`), gated behind a license acceptance click. This is "open-weight" in the sense that the weights are downloadable, but not "open source" by OSI definition — the OSI definition requires no restrictions on use, field, or purpose.

At launch in May 2024, this generated significant community discussion. Developers accustomed to the Apache 2.0 terms of Mistral 7B and Mixtral 8x7B found the MNPL a meaningful step back in terms of commercial flexibility. Mistral's position was that Codestral represented substantial investment in specialized code training, and the commercial licensing model was the mechanism to recoup that investment.

For individual developers running Codestral locally for personal projects, the license is permissive enough. For organizations building products, the license gates production use behind a negotiated commercial agreement. Mistral's commercial license inquiry goes through `license@mistral.ai`.

Compare this to DeepSeek Coder (MIT license, fully open) and Code Llama (Meta Llama license, permissive with a 700M MAU threshold). Both alternatives allow commercial use without a separate agreement. For organizations making a build-vs-buy decision, this is a real cost factor in the MNPL path.

---

## Deployment

**API:** The primary access method for most users. Mistral operates `codestral.mistral.ai` as a dedicated endpoint, separate from their main API. FIM completions go to `/v1/fim/completions`; chat-style code generation goes to `/v1/chat/completions`.

**Ollama:** Available as `codestral`. Q4 quantized, approximately 13 GB. The Ollama version respects the MNPL license — personal and research use is within scope; production deployment is not without a commercial license.

**Hugging Face:** `mistralai/Codestral-22B-v0.1` — gated behind license agreement. Full weights in bfloat16 (~46 GB). Requires a Hugging Face account and explicit license acceptance.

**IDE integrations at launch:** Continue.dev (VS Code and JetBrains), Tabnine, LlamaIndex, LangChain. Codestral FIM was designed to slot into the tab-completion workflow these tools expose.

---

## Updates Since Launch

Codestral has evolved significantly since v0.1 in May 2024. The v0.1 model described in this review is the launch version; subsequent releases address its main constraints.

**Codestral Mamba (July 2024):** A separate 7B model built on the Mamba2 state-space architecture — not a Transformer. Smaller, faster inference due to linear (not quadratic) attention scaling. Apache 2.0 license, fully open. Performance comparable to Transformer-based models of similar scale on code benchmarks. This was Mistral's experimental move into non-Transformer architectures for code; it does not supersede the 22B v0.1.

**Codestral 25.01 (January 2025):** A substantial update to the API model (not directly open-weight in the same way). Key changes: improved tokenizer, more efficient architecture with fewer than 100B parameters (exact count not disclosed), approximately 2× faster generation, and context window extended to 256K tokens — eight times the original 32K. Debuted at #1 on the LMSys Copilot Arena leaderboard at launch, indicating meaningful quality improvement over v0.1. The 256K window addresses the primary limitation of v0.1 for very large repository work.

**Codestral 25.08 (~August 2025):** Part of Mistral's "Mistral Coding Stack" enterprise offering. Claimed improvements: 30% increase in accepted code suggestions (as measured in IDE deployment contexts), 5% improvement in instruction following. Positioned for enterprise code assistance deployment.

For practical purposes: if you are accessing Codestral via the Mistral API, you are getting a model significantly better than v0.1. The `codestral-latest` alias routes to the current production version. The v0.1 weights on Hugging Face and Ollama are the original May 2024 release.

---

## Practical Considerations

**When Codestral v0.1 is a good choice:**
- Research and evaluation use cases where the MNPL is permissive enough
- IDE tab completion with Continue.dev or similar (FIM is the differentiator)
- Tasks requiring long code context (32K covers most single-file scenarios)
- Organizations that have negotiated a commercial license with Mistral

**Where alternatives are stronger:**
- Commercial production use without a Mistral agreement: DeepSeek Coder (MIT) or Code Llama (Meta Llama license) are drop-in alternatives without licensing overhead
- General reasoning alongside code generation: a general-purpose model at 70B+ is likely stronger on MBPP and multi-step reasoning tasks
- Very long repository context: Codestral 25.01 (via API, 256K) addresses this, but v0.1 is limited to 32K

**The FIM vs. instruction-following distinction:**
Codestral is optimized for the cursor-insertion pattern — FIM completions via the dedicated endpoint. For prompt-style code generation ("write me a function that does X"), a strong general model like [Mistral Large 3](/reviews/mistral-large-3-open-weight-moe-llm-review/) or even [Mistral Small 3.2](/reviews/mistral-small-3-2-24b-instruct-refinement-llm-review/) may perform better due to stronger instruction following. Codestral's advantage is specifically in the IDE autocomplete scenario, where FIM training depth matters.

---

## In the Mistral Model Family

Codestral sits alongside, not above, [Mistral AI's](/reviews/mistral-ai-open-weight-llm-european-ai/) general-purpose lineup. The contemporaneous general models in May 2024 included Mistral 7B and Mixtral 8x22B (both Apache 2.0). [Mistral Large 3](/reviews/mistral-large-3-open-weight-moe-llm-review/) (July 2024) and [Mistral Medium 3.5](/reviews/mistral-medium-3-5-dense-128b-agentic-llm-review/) arrived later with stronger general-purpose performance.

Codestral is a domain specialist, not a general-purpose upgrade. A developer choosing between Codestral and a general model should think of it the way one thinks of any specialized tool: narrowly excellent, broadly weaker.

The MNPL license also means Codestral exists in a separate commercial tier from Mistral's Apache 2.0 models. [Mistral Small 3.1](/reviews/mistral-small-3-1-vision-24b-llm-review/) and [Mistral Small 3.2](/reviews/mistral-small-3-2-24b-instruct-refinement-llm-review/) — released later and Apache 2.0 — have HumanEval Plus scores in the 89–93% range and can be used commercially without a licensing conversation. For organizations that want Apache 2.0 code capability, those models are worth evaluating against Codestral v0.1.

---

## Rating: 4/5

Codestral v0.1 deserves a 4. The technical achievement is real: 81.1% HumanEval at 22B was a genuine state-of-the-art result for parameter-efficient code generation in May 2024. Native FIM training at pretraining-time is the right approach for IDE autocomplete, and the RepoBench result demonstrates that 32K context was a meaningful advantage at launch. The model works as described, and the IDE integrations were ready at launch.

The MNPL license keeps it from a 5. A code model intended for developer tooling, with commercial use gated behind negotiated agreements, is harder to recommend than MIT-licensed or Apache-2.0-licensed alternatives for most practical deployments. DeepSeek Coder 33B's ~79% HumanEval with MIT licensing is only modestly weaker technically, but dramatically more flexible commercially.

For research, personal use, or organizations with a Mistral commercial agreement: Codestral v0.1 is excellent, and Codestral 25.01 (via API) is better still. For production deployment without an existing Mistral relationship: the licensing overhead is a real cost that MIT-licensed alternatives avoid.

---

*This review covers Mistral Codestral 22B v0.1 (May 29, 2024). For Codestral 25.01 and later API versions, refer to Mistral's official release notes. Benchmark figures sourced from Mistral AI's launch announcement and independent evaluations at release time. See also our [Mistral AI company overview](/reviews/mistral-ai-open-weight-llm-european-ai/).*

