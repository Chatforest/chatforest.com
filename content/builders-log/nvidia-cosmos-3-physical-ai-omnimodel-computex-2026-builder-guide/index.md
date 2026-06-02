---
title: "NVIDIA Cosmos 3: The First Open Physical AI Omnimodel, Launched at Computex 2026"
date: 2026-06-02
description: "NVIDIA launched Cosmos 3 at Computex on June 1 — the first open omnimodel that generates text, images, video, audio, and robot actions in a single system. Here's what builders in robotics, AV, and synthetic data pipelines need to know."
og_description: "NVIDIA Cosmos 3 launched June 1 at Computex — a fully open physical AI omnimodel that unifies world generation and action prediction. Super, Nano, and Edge variants. OpenMDW-1.1 license, Hugging Face weights, NIM microservices. Reduces robotics training cycles from months to days."
content_type: "Builder Guide"
card_description: "NVIDIA launched Cosmos 3 at Computex on June 1, 2026 — the first open physical AI omnimodel combining text, image, video, sound, and action generation in one model via a Mixture-of-Transformers (MoT) architecture. Three variants: Super (post-training for robotics/AV), Nano (sub-second inference), Edge (coming soon). OpenMDW-1.1 license, commercial use permitted. Available on Hugging Face and NVIDIA NIM microservices. Synthetic training data that took months now takes days."
tags: ["nvidia", "cosmos-3", "physical-ai", "robotics", "autonomous-vehicles", "synthetic-data", "omnimodel", "open-weights", "nim", "computex-2026", "world-models", "hugging-face"]
categories: ["builders-log"]
author: "ChatForest"
---

**At a glance:** NVIDIA Cosmos 3. Launched June 1, 2026 at Computex / GTC Taipei. World's first open physical AI omnimodel — text, image, video, ambient sound, and robot action generation in a single system. Three tiers: Super, Nano, Edge. OpenMDW-1.1 license with commercial use permitted. Weights on Hugging Face. NIM microservices for cloud deployment. Reduces physical AI training cycles from months to days. Part of our **[Builder's Log](/builders-log/)**.

---

NVIDIA's Computex 2026 keynote was expected to be a hardware event. Jensen Huang delivered hardware — Rubin training chips, Rubin CPX inference chips, RTX Spark consumer superchip — but the announcement that changes the roadmap for physical AI developers was a model, not a chip.

**Cosmos 3** is the first fully open omnimodel for physical AI. It doesn't just understand the physical world — it generates it, predicts actions within it, and outputs the action trajectories that robot controllers and AV systems need to act in it. All in a single model, available for download.

For builders working in robotics, autonomous vehicles, or synthetic data pipelines, Cosmos 3 changes the cost structure of getting a physical AI system into training.

---

## What Makes Cosmos 3 Different from Every Previous Model

Most foundation models are either **understanding models** (they analyze inputs) or **generation models** (they produce outputs). Cosmos 3 is both, at the same time, across six modalities.

The complete modality list: **text, images, video, ambient sound, and action trajectories** — all processed and generated within a single unified architecture.

The action trajectory output is the part that has no precedent in any open model. Cosmos 3 can produce joint angles, gripper positions, and trajectory points that describe how a robot should physically move to complete a task. That's not image generation with a note about robotics attached — that's direct output a robot controller can consume.

### What the Previous Cosmos Generation Did

Cosmos 1.x (launched GTC 2025) was a **video world model** — it generated physically plausible video sequences for training physical AI. It gave builders a way to create synthetic training data without real-world robot operation hours. That was significant.

Cosmos 3 absorbs everything Cosmos 1.x did and extends it into a full omnimodel. Video generation is still there. So is image generation. What's new is the unified architecture that ties generation to reasoning to action in one system — and the addition of sound, which matters for robots that need to understand their acoustic environment.

---

## Architecture: Mixture-of-Transformers

Cosmos 3 runs on a **Mixture-of-Transformers (MoT)** architecture that pairs two distinct transformer types:

- An **autoregressive (AR) transformer** handles reasoning — understanding scene context, object interactions, motion dynamics, spatial-temporal relationships
- A **diffusion transformer** handles generation — producing high-quality multimodal output from the reasoning context

These two don't operate sequentially as a pipeline. They're unified: the model reasons about the physical scene and generates output in a single forward pass through the system. The reasoning capability means Cosmos 3 doesn't just interpolate between training examples — it applies learned physical understanding to novel configurations.

The practical consequence: physics accuracy that generalizes beyond the training distribution. A robot arm encountering a novel object configuration can receive action trajectories that reflect real physical constraints (weight, friction, collision), not just statistical averages over similar training examples.

---

## Three Variants, Three Use Cases

Cosmos 3 ships in three tiers with explicit intended workloads:

### Cosmos 3 Super
**Post-training for robotics and AV models.** Super is the highest-capability variant, optimized for quality over speed. The intended use case is generating synthetic training data and fine-tuning larger robot or AV models. When you're building a training pipeline for a new robot platform and need physics-accurate synthetic sequences at scale, Super is the tier that produces data good enough to train on.

### Cosmos 3 Nano
**High-quality video and action reasoning in fractions of a second.** Nano runs fast enough for real-time-adjacent workloads — rapid iteration on test scenarios, quick evaluation of action proposals, batch inference over simulation sequences. It's the developer's workhorse during the build and evaluation loop.

### Cosmos 3 Edge
**Coming soon — real-time edge inference.** Edge targets deployment on device, likely for robots and AV systems that need to run world model inference without a cloud round-trip. No release date announced at Computex.

---

## License and What Commercial Use Looks Like

Cosmos 3 is released under **OpenMDW-1.1** — not MIT. OpenMDW-1.1 is NVIDIA's open model and data weight license, which permits commercial and non-commercial use of the model weights with conditions.

The key practical points:
- You can build commercial products using Cosmos 3 weights
- You can fine-tune Cosmos 3 for your specific robot or vehicle platform
- You can self-host and run Cosmos 3 inference in production
- The OpenMDW-1.1 license includes attribution requirements and acceptable use restrictions — read it before going to production

This is meaningfully more permissive than closed physical AI models from competitors, and more carefully scoped than a pure MIT license that allows unrestricted commercial redistribution of the weights themselves.

---

## Where to Get It

**Hugging Face:**
- `nvidia/Cosmos3-Super` — weights for the high-quality post-training tier
- `nvidia/Cosmos3-Nano` — weights for fast inference

**NVIDIA Build:**
- `build.nvidia.com` — API access for trying Cosmos 3 without self-hosting

**NIM Microservices:**
- NVIDIA NIM packages Cosmos 3 as a containerized inference service you can deploy on your own NVIDIA GPU infrastructure. Partners Baseten, CoreWeave, Microsoft Azure, Nebius, Deep Infra, and Classmethod support NIM-based Cosmos 3 deployment.

**GitHub:**
- The NVIDIA/cosmos repository provides runnable setup, inference, training, and evaluation workflows using Hugging Face Diffusers and NVIDIA tooling.

---

## The Cosmos Coalition

NVIDIA launched Cosmos 3 alongside a **Cosmos Coalition** — a network of physical AI developers contributing models, research, and evaluation techniques, with access to NVIDIA DGX Cloud infrastructure for large-scale training.

Founding coalition members at launch:
- **Agile Robots** — humanoid robotics
- **Black Forest Labs** — generative AI (video/image)
- **Generalist** — general-purpose robotics
- **LTX** — video generation
- **Runway** — video generation
- **Skild AI** — robot learning

The mix of robotics companies (Agile Robots, Skild AI, Generalist) with video generation labs (Black Forest Labs, LTX, Runway) reflects what Cosmos 3 actually is: a model class where world-generation capability and physical AI capability are the same problem.

---

## Industry Adoption at Launch

Several companies announced production adoption at or before Computex:

**Robotics:**
- Agile Robots (humanoid)
- Doosan Robotics (industrial)
- LG Electronics (service robots)
- Samsung Electronics (consumer/home robots)
- Skild AI (general robot learning)

**Autonomous Vehicles:**
- Li Auto (Chinese EV manufacturer)

**Data and Infrastructure:**
- Centific, Fogsphere (data pipeline applications)

This is launch-day adoption, not a beta program — which signals that some of these teams have been running Cosmos 3 in pre-release for their production training pipelines.

---

## What the Synthetic Data Argument Actually Means

The headline that NVIDIA promotes is "reduces training cycles from months to days." That framing understates what's actually changing.

Building a physical AI system today requires:
1. A robot (or simulator) to generate real action data
2. Humans to operate it or script scenarios
3. Months of data collection at whatever rate your robot fleet runs

Cosmos 3 enables an alternative pipeline:
1. A text or image description of a scenario
2. Cosmos 3 generates physics-accurate video sequences, with action trajectories, for that scenario
3. Those sequences feed into your downstream model training

The output quality — especially action trajectory accuracy under novel conditions — determines how much real-world validation you need downstream. With Cosmos 1.x, teams were using synthetic data as a supplement to real data. With Cosmos 3's unified reasoning and generation architecture, the argument is that synthetic data can substitute at a higher proportion of the training mix.

For teams without access to large robot fleets, that's the difference between a viable training pipeline and one that requires $10M+ in hardware.

---

## The Connection to NVIDIA's Broader Stack

Cosmos 3 is one of five announced at Computex. The full picture:

| Layer | What NVIDIA Announced |
|-------|----------------------|
| Training chips | Rubin |
| Inference chips | Rubin CPX |
| Client AI | RTX Spark superchip |
| LLM / reasoning | Nemotron 3 Ultra (500B+) |
| Physical AI | Cosmos 3 |

Cosmos 3 is the model layer for physical AI in the same way Nemotron 3 is the model layer for reasoning and coding. The shared deployment infrastructure — NIM microservices, build.nvidia.com, Hugging Face — means teams can run Nemotron for their reasoning agent tier and Cosmos 3 for their simulation and action generation tier within the same NVIDIA-native stack.

---

## What This Means for Builders

**If you're building robotics or AV systems:**

The question is no longer whether open physical AI models exist — it's whether Cosmos 3 Super's output quality meets your domain's physics accuracy bar. The architecture (MoT with explicit reasoning before generation) is the right approach for generalization. Test it against your specific robot platform and object configurations. The Cosmos 3 Nano tier gives you fast feedback loops before committing training compute to Super.

**If you're building synthetic data pipelines:**

Cosmos 3 changes the input requirements. Previous world models needed careful scene setup and simulation scaffolding. The MoT architecture enables text-conditioned generation of physically plausible scenarios. If your pipeline relies on simulator-generated data, Cosmos 3 is worth evaluating as a replacement or supplement — particularly for novel scenario generation that simulators handle poorly (deformable objects, fluid dynamics, contact-rich manipulation).

**If you're not in robotics or AV:**

Cosmos 3 is not directly relevant to software-only agent development. The physics-accurate generation and action trajectory outputs are specifically useful when your AI system interacts with the physical world. Watch the coalition adoption: Runway and Black Forest Labs joining signals that advanced video generation is converging with physical AI capability. That convergence may eventually matter for simulation, testing, or embodied agent development.

**The OpenMDW-1.1 licensing question:**

Before building a production system on Cosmos 3 weights, review the OpenMDW-1.1 license against your commercial use requirements. NVIDIA has been consistent in allowing commercial deployment — but the license has specific terms around attribution, acceptable use, and redistribution that differ from permissive open-source licenses.

---

## What's Missing

NVIDIA has not disclosed specific pricing for Cosmos 3 NIM microservices. Cloud partner pricing (CoreWeave, Baseten, Azure) will vary by provider and GPU configuration. For build.nvidia.com API access, pricing follows NVIDIA's standard NIM API model (check current rates at build.nvidia.com before building pricing assumptions into your architecture).

Cosmos 3 Edge — the variant for real-time edge inference on deployed robots — has no release date. For teams building robots that need inference without cloud round-trips, Edge is the variant that matters most. It's not available yet.

---

*Cosmos 3 launched June 1, 2026. Weights available at `nvidia/Cosmos3-Super` and `nvidia/Cosmos3-Nano` on Hugging Face. Source: NVIDIA Newsroom, Hugging Face blog, GamesBeat.*
