---
title: "Rhoda AI Review — After 18 Months in Stealth, a $450M Bet That Robots Should Predict Before They Move"
date: 2026-05-24
description: "Rhoda AI exited stealth on March 10, 2026 with $450M in Series A funding and FutureVision, a robot intelligence platform built on video-predictive control. Instead of teaching robots rules or reward functions, Rhoda's Direct Video Action architecture trains on hundreds of millions of internet videos to build a physics-aware model of the world, then converts video predictions into real-time robot actions. We review the technology, the team, the funding, and where Rhoda fits in the crowded physical AI landscape."
og_description: "Rhoda AI (March 10, 2026): $450M Series A, $1.7B valuation. FutureVision platform built on Direct Video Action (DVA) — video-predictive robot control trained on 100M+ internet videos, fine-tuned in as little as 10 hours of teleoperation data. CEO Jagdeep Singh; CSO Eric Ryan Chan (Stanford, ex-WorldLabs). Backed by Khosla Ventures, Temasek, Mayfield, Capricorn, John Doerr. Target: manufacturing and logistics deployments. Competes with Physical Intelligence (pi), Genesis AI, Rhoda is hardware-agnostic."
card_description: "Rhoda AI spent 18 months building in complete secrecy before emerging in March 2026 with $450 million and a provocative thesis: the right way to build robot intelligence is to teach robots to predict the future as video, then convert those predictions into actions. The Direct Video Action (DVA) model at the heart of Rhoda's FutureVision platform is trained on hundreds of millions of internet videos — not robot data — and can learn a new industrial task with as little as ten hours of teleoperation. In manufacturing pilots, Rhoda systems have completed component-processing workflows in under two minutes without human intervention. The key question for any physical AI company in 2026 is the same: can it work reliably outside the lab?"
tags: ["robotics", "physical-ai", "robot-intelligence", "manufacturing-ai", "video-prediction", "series-a", "ai-funding", "deep-tech", "edge-ai"]
categories: ["reviews"]
author: "ChatForest"
---

**At a glance:** Rhoda AI. Founded 2024, stealth until March 10, 2026. Headquarters: San Francisco. Product: FutureVision, a video-predictive robot intelligence platform. Funding: $450 million Series A at a $1.7 billion valuation. Investors: Khosla Ventures, Temasek, Mayfield, Capricorn Investment Group, Premji Invest, John Doerr, and others. CEO: Jagdeep Singh. Chief Science Officer: Eric Ryan Chan (Stanford, ex-WorldLabs). Target markets: manufacturing, logistics. Model architecture: Direct Video Action (DVA) — video-based pretraining on hundreds of millions of internet videos, fine-tuned on 10+ hours of teleoperation data per new task. Part of our **[AI Companies & Tools reviews](/categories/ai-tools/)**.

---

The premise of Rhoda AI is that the most important thing a robot can learn is not what to do — it is what happens next. If a robot can predict the immediate future of its physical environment in video form, it can derive actions from those predictions rather than from rigid rules or reward functions. This is the bet behind FutureVision, the platform Rhoda unveiled on March 10, 2026 after 18 months of building in stealth.

The approach is called video-predictive control. It is distinct from the two approaches that dominated robotics AI before 2025: classical reinforcement learning (optimizing for reward signals that are hard to define) and pure imitation learning (cloning human demonstrations, which generalizes poorly). Rhoda's Direct Video Action architecture treats the real world as a video generation problem first. The robot observes, predicts the next frames, extracts actions from those predictions, and re-observes — cycling every few hundred milliseconds in a closed loop.

This review is based on public announcements, press releases, research publications, and third-party coverage. We have not tested Rhoda hardware or the FutureVision platform directly.

---

## The Stealth Window

Rhoda AI was founded in approximately mid-2024 and operated in stealth for eighteen months before its March 2026 announcement. During that period, the company was unknown to the public, had no presence in press coverage, and conducted industrial pilots that were not disclosed until launch.

Eighteen months of stealth in the current AI environment is unusual. Most AI companies announce before they build, raise publicly announced pre-seed rounds within weeks of founding, and generate press coverage from day one. Rhoda deliberately chose the opposite: build a working system, validate it in real industrial environments, and raise with demonstrated deployments rather than paper architecture.

The $450 million Series A came with those validations in hand. The round was led by Khosla Ventures, with participation from Temasek, Mayfield, Capricorn Investment Group, Premji Invest, Leitmotif, Matter Venture Partners, Prelude Ventures, Xora, and John Doerr. That investor list — crossing US venture, Singapore sovereign wealth, impact-adjacent funds, and individual investors with hardware and deep-tech track records — suggests the due diligence on industrial performance was rigorous.

At $1.7 billion, the valuation is notable for a Series A with no prior public funding history. The comparison point is Physical Intelligence (pi), the San Francisco robotics AI company that raised a $600 million Series B in November 2025 at a $5.6 billion valuation. Rhoda's entry valuation of $1.7 billion positions it as an earlier-stage company with a more concentrated technology bet, not yet competing on scale.

---

## The Technology: Direct Video Action

The central technical claim Rhoda makes is that video-based pretraining transfers better to real-world robotic control than reinforcement learning or demonstration-based training alone.

The reasoning is intuitive: the physical world is continuous, and human intuition about physics (what falls, what slides, what breaks) is built from years of visual observation, not from reward functions. A model pretrained on hundreds of millions of internet videos — sports, cooking, construction, manufacturing, nature — has seen an enormous variety of physical cause-and-effect. That prior knowledge is what Rhoda calls the "motion prior": a learned understanding of how objects in the world tend to move and interact.

The Direct Video Action (DVA) architecture works in two phases:

**Pretraining on video.** Rhoda trains foundation models on large-scale internet video to learn motion, physics, and the structure of physical environments. This is not robotic data — it is general video of the physical world. The models learn to predict future video frames: given what the robot sees now, what will the next few hundred milliseconds look like?

**Fine-tuning on teleoperation.** After pretraining, Rhoda fine-tunes models using teleoperation data — a human operator controlling the robot to demonstrate tasks. The key claim is that the strong motion prior from video pretraining means fine-tuning is dramatically more efficient: Rhoda reports that new tasks can be learned with as little as ten hours of teleoperation data. Comparable systems using pure imitation learning typically require orders of magnitude more demonstration data.

**Closed-loop action generation.** At inference time, the DVA model continuously observes the robot's environment, predicts future states as video, converts those predictions into specific robot actions (joint positions, gripper states), and executes them. The cycle repeats every few hundred milliseconds. Because the loop is closed — the robot re-observes after each action — it adapts to unexpected changes in its environment rather than executing a pre-planned sequence.

This closed-loop design is what Rhoda emphasizes as the key departure from classical robot programming. A traditional industrial robot executes a sequence of pre-programmed movements. If a part is in the wrong position, the robot fails. The DVA model perceives the world continuously and adjusts; when something is out of place, it updates its prediction and adapts its action.

### The "Reality Gap" Problem

Every robotics AI company has to address the same underlying challenge: systems that work in controlled laboratory settings frequently fail in real production environments. Materials have unexpected textures. Lighting changes. Parts are slightly misaligned. Human coworkers introduce variability. Classical robot programs are brittle because they were not designed to handle this variance.

Rhoda's claimed solution is that continuous video-based prediction naturally handles variability — because the model is always re-predicting rather than following a fixed plan, it responds to what is actually in front of it. The company cites an industrial manufacturing evaluation where Rhoda systems completed a component-processing workflow in under two minutes per cycle without human intervention, exceeding customer KPIs under production conditions.

Third-party verification of these results is not available. The claim is plausible given the DVA architecture, but the deployment conditions — which specific industry, which specific robot hardware, what definition of "exceeding customer KPIs" — are not publicly disclosed.

---

## The Team

**Jagdeep Singh (CEO and Co-Founder)** is a serial deep-tech entrepreneur. His prior companies span wireless networking (Quantenna, sold to ON Semiconductor), quantum computing (IonQ, which he co-founded and took public in 2021), and AI semiconductor design (Nuvia, which he co-founded and sold to Qualcomm for approximately $1.4 billion in 2021). Singh's track record is in building hardware-facing deep-tech companies to exits — not software-first AI startups. At Rhoda, his role is the kind of commercial and organizational scaling that requires understanding both engineering constraints and production environments.

**Eric Ryan Chan (Chief Science Officer and Co-Founder)** is a Stanford researcher specializing in computer vision and generative modeling. Before Rhoda, Chan served as a generative model architect at WorldLabs — the spatial intelligence company founded by Stanford AI Lab director Fei-Fei Li in 2024. WorldLabs focuses on building world models that understand 3D spatial structure; Chan's work there was at the intersection of generative models and physical-world understanding, a direct precursor to the video-predictive control approach at Rhoda.

**Gordon Wetzstein (Co-Founder)** is a Professor of Electrical Engineering at Stanford University and director of the Computational Imaging Lab. Wetzstein's research focuses on the intersection of computational optics and machine learning — specifically how camera and display systems can be redesigned to work better with AI perception systems. His involvement at Rhoda reflects the hardware-software integration challenge in physical AI: the sensors a robot uses to perceive the world are as important as the model that interprets what those sensors capture.

The combination of Singh (deep-tech commercialization), Chan (generative modeling and world models), and Wetzstein (computational imaging and perception) represents a team built for the specific challenges of physical AI at industrial scale — not a team of language model researchers pivoting to robotics.

---

## The Market and Deployment Targets

Rhoda has disclosed two primary target markets: manufacturing and logistics. Both are large, high-variability environments where the gap between controlled automation and real production has historically been the hardest to close.

**Manufacturing.** Industrial manufacturing requires robots to handle components that vary in dimensions, surface finish, and position — especially in high-mix, low-volume production (where many different part types are made in small batches). Classical automation handles this poorly because reprogramming is expensive and slow. Rhoda's ten-hour fine-tuning claim, if it holds in production, would make it practical to deploy new robotic tasks in days rather than weeks or months.

**Logistics.** Warehouse automation is one of the most active application areas for robotics AI. Sorting, picking, packing, and palletizing all require handling objects with variable weight, shape, and packaging. The core challenge is not speed — it is the long tail of edge cases. DVA's closed-loop prediction is designed for exactly this kind of variability.

The business model Rhoda envisions is a platform licensing model: FutureVision as a foundation model licensed to partners across different robotic hardware platforms. Rhoda is not building its own robot arms or end-effectors. The FutureVision model is hardware-agnostic — designed to work on whatever physical robot a customer already has or wants to purchase. This is distinct from companies like Figure AI (which builds its own humanoid robot hardware) and closer to Physical Intelligence's model of selling AI software that runs on customer-selected hardware.

---

## Competitive Landscape

The physical AI category has become one of the most active investment areas of 2025–2026. Rhoda operates in a field with several well-capitalized competitors:

**Physical Intelligence (pi)** — the most direct comparison. Founded 2024 by former Google DeepMind researchers Karol Hausman, Sergey Levine, and Chelsea Finn. Raised $600M Series B in November 2025 at $5.6B valuation, with reports of a potential $1B round at $11B under discussion as of March 2026. Pi's π0 architecture is also hardware-agnostic and learns from human demonstrations. The key technical difference is that pi uses a flow matching approach (diffusion-derived) rather than video-predictive control. Both companies are betting on general robot policies that transfer across hardware; they differ on the architecture of that generality.

**Genesis AI** — unveiled in May 2026 with a $105M seed and GENE-26.5, its first model. Genesis AI focuses on foundational models for robotic hands. Earlier stage, more research-oriented than Rhoda or Physical Intelligence.

**Figure AI** — humanoid robot company building its own hardware (Figure 02 robot) and partnering with OpenAI for language-grounded instruction following. Different business model — hardware-centric rather than platform.

**Boston Dynamics** — established player with Spot and Atlas, now offering Spot as an AI-accessible platform with the Spot AI API. Legacy advantage in mechanical robustness; newer entrants are competing on AI adaptability.

The critical differentiator Rhoda claims is the combination of internet-scale video pretraining (which is cheap and scalable) and 10-hour fine-tuning (which makes deployment fast). Physical Intelligence's π0 also claims fast adaptation, but has not publicly cited a 10-hour threshold. Whether Rhoda's video-pretraining approach provides meaningfully better generalization than diffusion-based approaches like π0's remains an open empirical question.

---

## What to Watch

**Industrial pilot conversions.** Rhoda has demonstrated at least one production deployment. The question is whether those deployments convert to commercial contracts and whether customer KPI claims hold across a broader range of tasks and environments. Watch for commercial deployment announcements over the next two quarters.

**Open publication.** Rhoda published research on Direct Video Action (DVA) prior to the stealth exit. Whether the company continues publishing technical details or shifts toward protecting its architecture as a moat will signal whether it sees academic credibility or competitive secrecy as the higher priority.

**Open-weight question.** Neither Rhoda nor Physical Intelligence has indicated plans to release open-weight versions of their robot foundation models. The open-weight question in physical AI is less mature than in language models — the robotics community has not yet had a Llama-equivalent moment. If either company releases open weights, the competitive dynamics shift significantly.

**Competition on the 10-hour claim.** If fine-tuning a new industrial task in ten hours of teleoperation data holds up in third-party evaluation, it is a genuine commercial advantage. Competing platforms will attempt to replicate or undercut this number. Watch for independent benchmarks that compare fine-tuning efficiency across Physical Intelligence, Rhoda, and others.

**Hardware partnerships.** Rhoda's platform-licensing model requires hardware partners. Announcements of specific robot arm or logistics hardware integrations will be key milestones.

---

## Caveats

The core technical claims — video pretraining transfers efficiently to robotic control; ten hours of teleoperation data is sufficient; closed-loop prediction handles production variability — are backed by one disclosed industrial evaluation. They have not been independently verified by third parties. Physical AI is a domain where laboratory demonstrations have historically been much more reliable than field deployments; Rhoda's stealth exit with demonstrated production results is a stronger starting position than most, but production-scale validation is still ahead.

The funding size ($450M) is large relative to the stage. It creates capital-efficiency pressure: the company will need to demonstrate commercial scale across multiple industries to justify the valuation trajectory implied by institutional investors at this round size.

---

## Related Reviews

- [Project Prometheus — Jeff Bezos's Physical AI Lab at $38B](/reviews/jeff-bezos-project-prometheus-artificial-general-engineer-manufacturing-ai-2026/) — physical AI at frontier scale
- [Isomorphic Labs — AI Drug Design Engine from the AlphaFold Team](/reviews/isomorphic-labs-alphafold-drug-design-engine-clinical-trials-2-1b-series-b-2026/) — another deep-tech AI spinout building in secret before going public
- [Sierra AI — Enterprise Agent Platform at $15.8B](/reviews/sierra-ai-enterprise-agent-platform-bret-taylor-950m-series-e-2026/) — AI systems reaching production deployments across Fortune 50
