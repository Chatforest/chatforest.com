---
title: "NVIDIA Cosmos 3: The First Open Omnimodel for Physical AI"
date: 2026-06-14
description: "NVIDIA Cosmos 3 launched June 1, 2026, as the first fully open omnimodel for physical AI — combining world generation, physical reasoning, and action generation in one open-weight model. Here's what builders need to know."
og_description: "NVIDIA Cosmos 3 is the first open omnimodel unifying vision reasoning, world simulation, and action generation for robotics and autonomous vehicles. Free to use under OpenMDW-1.1. Topped Physics-IQ, R-Bench, and PAI-Bench leaderboards at launch (R-Bench lead lost to LingBot-Video since)."
card_description: "Cosmos 3 launched June 1 as NVIDIA's open physical AI foundation model — the first to unify world generation, physical reasoning, and robot action generation in a single open-weight model. Free via HuggingFace."
tags: ["nvidia", "physical-ai", "robotics", "open-weight", "world-model", "autonomous-vehicles", "foundation-model", "open-source"]
categories: ["reviews"]
author: "ChatForest"
rating: 4.5
sources_audited: 2026-08-23
last_refreshed: 2026-08-23
---

**At a glance:** [NVIDIA Cosmos 3, released June 1, 2026 at GTC Taipei, is the first fully open omnimodel for physical AI](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai). It generates text, images, video, ambient sound, and robot action sequences in a single unified model — built on a novel [Mixture-of-Transformers (MoT) architecture](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai). Available free on HuggingFace under the [OpenMDW-1.1 license](https://github.com/NVIDIA/cosmos/blob/main/LICENSE), it [topped three major physical AI benchmarks at launch](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/) (one of those three, R-Bench, has since been overtaken — see Benchmark Performance) and [reduces robotics training cycles from months to days](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai). A third, on-device variant — **Cosmos 3 Edge** — has also since shipped.

**Rating: 4.5/5** — Best-in-class for physical AI development; open weights make it especially compelling. Niche audience (robotics/AV), and hardware requirements are substantial.

---

## What Cosmos 3 Is

Most world models generate video. Cosmos 3 generates *actions*.

NVIDIA's Cosmos platform has existed since Cosmos 1, but Cosmos 3 marks a qualitative leap: [it is the first omnimodel to natively understand and produce all of: text, images, video, ambient sound, and robot action sequences](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai) (joint angles, gripper positions, motion trajectories). The prior generation required separate components for reasoning vs. generation. Cosmos 3 puts them in a single model.

The practical application: a robot developer can give Cosmos 3 a task description, a scene image, and target objects. The model generates a physically plausible simulation of the robot completing the task — and exports the action trajectory data needed to train the robot's policy model. [Simulation-to-real training cycles that previously took months are now reported to take days](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai).

---

## Architecture: Mixture-of-Transformers

Cosmos 3 introduces a [**Mixture-of-Transformers (MoT)**](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai) architecture — a two-tower design:

- **Autoregressive transformer** for discrete token generation (reasoning, text, actions)
- **Diffusion transformer** for continuous multimodal generation (images, video, sound)

[The two towers are not separate models that are chained together — they maintain separate parameters but are trained jointly and interact through joint attention](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai). This allows the model to reason about physics (e.g., "if this arm swings forward, the object will slide to the left") and then generate a video that accurately reflects that outcome, alongside the corresponding joint angles for a real robot to execute.

This is architecturally distinct from the "chain a reasoning LLM with a video generation model" approach that characterizes most physical AI pipelines today. Whether the joint training provides meaningful gains over careful chaining in practice is something independent benchmarks are beginning to test, but NVIDIA's internal results are strong.

---

## Model Variants

[Cosmos 3 shipped in two variants at launch, with a third "coming soon"](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/):

| Variant | Target Use Case | Speed vs. Quality |
|---|---|---|
| **Cosmos 3 Super** ([64B parameters: 32B reasoner + 32B generator](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)) | Post-training for robotics and autonomous vehicle models | Highest physics accuracy; slower inference |
| **Cosmos 3 Nano** ([16B parameters: 8B reasoner + 8B generator](https://huggingface.co/blog/nvidia/cosmos-3-for-physical-ai)) | Real-time reasoning at inference latency | Fast; lower fidelity |
| **Cosmos 3 Edge** ([4B parameters, shipped](https://blogs.nvidia.com/blog/siggraph-news-2026/)) | On-device inference on Jetson, RTX PRO, DGX, and GeForce RTX GPUs | Real-time, single-GPU/edge-device deployment |

**Update, 2026-08-23:** Cosmos 3 Edge is no longer "coming soon" — NVIDIA [released it at SIGGRAPH on July 20, 2026](https://blogs.nvidia.com/blog/siggraph-news-2026/), a 4-billion-parameter model with weights on [HuggingFace](https://huggingface.co/blog/nvidia/cosmos3edge) and inference/post-training recipes on GitHub. All three variants — Edge, Nano, and Super — are now available. Most builders working on data generation pipelines will use **Cosmos 3 Super**; teams deploying on robots or edge compute now have a choice between **Cosmos 3 Nano** (workstation-grade) and **Cosmos 3 Edge** (on-device, real-time).

Specialized checkpoints are also available — including [`Cosmos3-Nano-Policy-DROID`](https://huggingface.co/nvidia/Cosmos3-Nano-Policy-DROID), a fine-tuned variant that generates robot action trajectories from language instructions and visual observations on the DROID robot platform, and [`Cosmos3-Super-Text2Image`](https://huggingface.co/nvidia/Cosmos3-Super-Text2Image) for high-fidelity image generation tasks.

---

## Benchmark Performance

[At launch, NVIDIA reported Cosmos 3 topping three physical AI-relevant leaderboards among open models](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/):

- **Physics-IQ**: Measures physical understanding in generated video (do objects fall correctly? Do materials behave as expected?)
- **R-Bench**: Robotics-specific video generation evaluation
- **PAI-Bench**: Physical AI benchmark spanning robotics, autonomous vehicles, and physics

Among open models, it also leads [**TAR** (Traffic Anomaly Reasoning), the official leaderboard for the AI City Challenge 2026 Track 3](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/), for vision understanding.

**Update, 2026-08-23 — R-Bench position lost:** Ant Group's Robbyant open-sourced [LingBot-Video](https://github.com/Robbyant/lingbot-video) in July 2026, and it now ranks #1 among open-source models on R-Bench (0.620), ahead of Cosmos 3 Super (0.581) — a lead of 0.039 points. Cosmos 3 Super still appears to hold the top open-model spot on Physics-IQ, PAI-Bench, and TAR as of this audit, but R-Bench is no longer accurate to cite as a Cosmos 3 win.

*Caveat standard to all NVIDIA-reported benchmarks*: these are first-party results. Third-party replication is ongoing, and — as the R-Bench case shows — open-model leaderboard positions can and do change within weeks as new entrants ship. The physical AI benchmark ecosystem is newer and less standardized than software coding benchmarks, so cross-lab comparison is still evolving.

---

## Licensing and Access

Cosmos 3 is released under [**OpenMDW-1.1**](https://github.com/NVIDIA/cosmos/blob/main/LICENSE) — [a Linux Foundation-stewarded open model-weight license that NVIDIA has adopted across its Cosmos, Isaac GR00T, and Nemotron model families](https://www.linuxfoundation.org/press/linux-foundation-releases-openmdw-1.1-nvidia-adopts-openmdw-for-cosmos-isaac-gr00t-ising-and-nemotron-ai-model-families). The license permits commercial and non-commercial use, modification, and redistribution with no field-of-use restrictions — [the only condition is retaining copyright and license notices in any redistribution](https://github.com/NVIDIA/cosmos/blob/main/LICENSE).

Models are available now:
- HuggingFace: [`nvidia/Cosmos3-Super`](https://huggingface.co/nvidia/Cosmos3-Super), [`nvidia/Cosmos3-Nano`](https://huggingface.co/nvidia/Cosmos3-Nano), [`nvidia/Cosmos3-Edge`](https://huggingface.co/nvidia/Cosmos3-Edge) (added since launch), and fine-tuned variants
- GitHub: [github.com/NVIDIA/cosmos](https://github.com/NVIDIA/cosmos) — runnable inference, training, and evaluation workflows

[NVIDIA offers a free, rate-limited hosted preview via build.nvidia.com for prototyping, but has not published production per-token API pricing for Cosmos 3](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai). For production use, the practical path is downloading the open weights and self-hosting — meaning you pay for GPU compute, not per-request fees.

---

## Hardware Reality Check

NVIDIA's own deployment guidance, now covering all three shipping variants:

- [**Cosmos 3 Nano**: Targets workstation-grade compute, such as the NVIDIA RTX PRO 6000 GPU, for real-time robotics inference](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/)
- [**Cosmos 3 Super**: Targets datacenter deployment on NVIDIA Hopper and Blackwell-class GPUs](https://developer.nvidia.com/blog/develop-physical-ai-reasoning-world-and-action-models-with-nvidia-cosmos-3/) for large-scale synthetic data generation
- **Cosmos 3 Edge** (added 2026-08-23): [Targets NVIDIA Jetson (including Jetson Thor), RTX PRO, DGX systems, and GeForce RTX GPUs](https://blogs.nvidia.com/blog/siggraph-news-2026/) for real-time, single-GPU or on-device inference — the [model card](https://huggingface.co/nvidia/Cosmos3-Edge) notes edge devices like Jetson boards take roughly 100-200+ seconds for a 480p image-to-video generation versus ~23-27 seconds on an H100.

For most builders, cloud GPU instances (Lambda, RunPod, or NVIDIA's own DGX Cloud) are the practical path unless you have on-prem hardware. The open-weight model means you pay for compute, not per-request fees — which can be economical at scale for data generation pipelines.

---

## Who This Is For

Cosmos 3 is specifically built for:

1. **Robotics engineers** building manipulation or locomotion policies via sim-to-real transfer
2. **Autonomous vehicle teams** generating synthetic training scenes with accurate physics
3. **Physical AI researchers** evaluating world models and developing policy networks
4. **Simulation engineers** at gaming or VFX studios who need physically accurate scene generation

This is **not** a general-purpose language model, multimodal assistant, or code generation tool. If you're not working on physical AI — robots, drones, vehicles, or physically grounded simulation — Cosmos 3 is not your tool. But if you are, it is currently the strongest open-weight option available by a meaningful margin.

---

## NVIDIA Cosmos Coalition

[NVIDIA launched the **Cosmos Coalition** alongside Cosmos 3, bringing in partners to validate and extend the platform](https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai):

- **Agile Robots** — humanoid robotics
- **Black Forest Labs** — image generation infrastructure
- **Generalist** — general-purpose robotics
- **LTX** — video generation
- **Runway** — media/VFX workflows
- **Skild AI** — robot learning

These were the six founding members at launch. **Update, 2026-08-23:** the coalition has since expanded substantially — [Japan's leading robotics and manufacturing companies (AIRoA, FANUC, Fujitsu, Hitachi, Kawasaki Heavy Industries, Kubota, NEC, SoftBank Corp., Sony Group, and Yaskawa Electric, plus several more) joined in July 2026](https://nvidianews.nvidia.com/news/japans-robotics-and-manufacturing-leaders-build-on-nvidia-cosmos-to-advance-physical-ai-frontier), and additional individual companies such as [Telexistence](https://tx-inc.com/en/blog/2026/07/16/12644/) and [Mujin](https://mujin-europe.com/resources/news/mujin-joining-the-nvidia-cosmos-coalition) have announced joining as well.

The coalition is important signal: it means Cosmos 3 is being stress-tested in production robotics pipelines by teams building real products, not just evaluated in academic settings.

---

## Builder Verdict

If you work in physical AI, Cosmos 3 is the clearest open-weight step change since the original Cosmos release. The MoT architecture's joint training of reasoning and generation is genuinely novel. Free weights under a permissive license means there's minimal cost to experiment.

The gaps to watch: hardware requirements remain high (datacenter-class Hopper/Blackwell GPUs for Super), and first-party benchmarks need third-party validation to fully trust — R-Bench is a concrete example, since Cosmos 3 Super's open-model lead there was overtaken by LingBot-Video within about two months of launch (see Benchmark Performance above). *(Correction, 2026-08-23: an earlier version of this sentence said Cosmos 3 Edge "isn't shipping yet" — it shipped July 20, 2026 at SIGGRAPH; see Model Variants above.)*

For a software-focused builder who just wants an LLM or coding assistant, Cosmos 3 is infrastructure — relevant only if you're building pipelines for robots or vehicles.

**Rating: 4.5/5.** Best open physical AI foundation model available. Narrow audience, high hardware bar, but for that audience it's a genuine step-change tool.

---

*ChatForest researches AI tools and models. We do not have hands-on access to Cosmos 3 infrastructure — this review is based on NVIDIA's published technical materials, HuggingFace model cards, and third-party reporting from HPC Wire, MarkTechPost, and the NVIDIA Developer Blog.*
