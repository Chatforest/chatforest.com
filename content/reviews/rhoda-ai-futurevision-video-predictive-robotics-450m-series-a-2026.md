---
title: "Rhoda AI Review — After 18 Months in Stealth, a $450M Bet That Robots Should Predict Before They Move"
date: 2026-05-24
sources_audited: 2026-07-28
description: "Rhoda AI exited stealth on March 10, 2026 with $450M in Series A funding and FutureVision, a robot intelligence platform built on video-predictive control. Instead of teaching robots rules or reward functions, Rhoda's Direct Video Action architecture trains on hundreds of millions of internet videos to build a physics-aware model of the world, then converts video predictions into real-time robot actions. We review the technology, the team, the funding, and where Rhoda fits in the crowded physical AI landscape."
og_description: "Rhoda AI (March 10, 2026): $450M Series A, $1.7B valuation. FutureVision platform built on Direct Video Action (DVA) — video-predictive robot control trained on 100M+ internet videos, fine-tuned in as little as 10 hours of teleoperation data. CEO Jagdeep Singh; CSO Eric Ryan Chan (Stanford, ex-WorldLabs). Backed by Khosla Ventures, Temasek, Mayfield, Capricorn, John Doerr. Target: manufacturing and logistics deployments. Competes with Physical Intelligence (pi), Genesis AI, Rhoda is hardware-agnostic."
card_description: "Rhoda AI spent 18 months building in complete secrecy before emerging in March 2026 with $450 million and a provocative thesis: the right way to build robot intelligence is to teach robots to predict the future as video, then convert those predictions into actions. The Direct Video Action (DVA) model at the heart of Rhoda's FutureVision platform is trained on hundreds of millions of internet videos — not robot data — and can learn a new industrial task with as little as ten hours of teleoperation. In manufacturing pilots, Rhoda systems have completed component-processing workflows in under two minutes without human intervention. The key question for any physical AI company in 2026 is the same: can it work reliably outside the lab?"
tags: ["robotics", "physical-ai", "robot-intelligence", "manufacturing-ai", "video-prediction", "series-a", "ai-funding", "deep-tech", "edge-ai"]
categories: ["reviews"]
author: "ChatForest"
---

**At a glance:** Rhoda AI. Founded 2024, stealth until March 10, 2026. Headquarters: San Francisco. Product: FutureVision, a video-predictive robot intelligence platform. Funding: $450 million Series A at a $1.7 billion valuation. Investors: Khosla Ventures, Temasek, Mayfield, Capricorn Investment Group, Premji Invest, John Doerr, and others. CEO: Jagdeep Singh. Chief Science Officer: Eric Ryan Chan (Stanford, ex-WorldLabs). Target markets: manufacturing, logistics. Model architecture: Direct Video Action (DVA) — video-based pretraining on hundreds of millions of internet videos, fine-tuned on 10+ hours of teleoperation data per new task. Part of our **[AI Companies & Tools reviews](/categories/ai-tools/)**.

---

The premise of Rhoda AI is that the most important thing a robot can learn is not what to do — it is what happens next. If a robot can predict the immediate future of its physical environment in video form, it can derive actions from those predictions rather than from rigid rules or reward functions. This is the bet behind FutureVision, the platform [Rhoda unveiled on March 10, 2026](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World) after 18 months of building in stealth.

The approach is called video-predictive control. It is distinct from the two approaches that dominated robotics AI before 2025: classical reinforcement learning (optimizing for reward signals that are hard to define) and pure imitation learning (cloning human demonstrations, which generalizes poorly). Rhoda's Direct Video Action architecture treats the real world as a video generation problem first. The robot observes, predicts the next frames, extracts actions from those predictions, and re-observes — cycling every few hundred milliseconds in a closed loop.

This review is based on public announcements, press releases, research publications, and third-party coverage. We have not tested Rhoda hardware or the FutureVision platform directly.

---

## The Stealth Window

Rhoda AI was founded in approximately mid-2024 and [operated in stealth for eighteen months before its March 2026 announcement](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World). The company did not make an official public announcement during that window and did not disclose its industrial pilots — though [Forbes reported on Rhoda's stealth-mode fundraising and robot-building in October 2025](https://www.forbes.com/sites/annatong/2025/10/15/two-ai-startups-have-each-raised-100-million-to-build-humanoid-robots-in-stealth/) based on internal documents, so the company was not entirely unknown to reporters before the March 2026 launch.

Eighteen months of stealth in the current AI environment is unusual. Most AI companies announce before they build, raise publicly announced pre-seed rounds within weeks of founding, and generate press coverage from day one. Rhoda deliberately chose the opposite: build a working system, validate it in real industrial environments, and raise with demonstrated deployments rather than paper architecture.

The [$450 million Series A](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World) came with those validations in hand. Backers included Khosla Ventures, Temasek, Mayfield, Capricorn Investment Group, Premji Invest, Leitmotif, Matter Venture Partners, Prelude Ventures, Xora, and John Doerr; [Rhoda's press release does not name a single lead investor](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World), and press coverage has attributed the lead variously to Premji Invest and to Capricorn/Khosla. That investor list — crossing US venture, Singapore sovereign wealth, impact-adjacent funds, and individual investors with hardware and deep-tech track records — suggests the due diligence on industrial performance was rigorous.

[Reuters reported the round valued Rhoda at $1.7 billion](https://finance.yahoo.com/news/rhoda-ai-raises-450-million-160945418.html), though the company's own press release does not disclose a valuation figure. That figure is not, however, Rhoda's first outside capital: [Forbes reported in October 2025](https://www.forbes.com/sites/annatong/2025/10/15/two-ai-startups-have-each-raised-100-million-to-build-humanoid-robots-in-stealth/) that Rhoda had already raised roughly $230 million, including a $162.6 million round in April 2025 at a valuation near $1 billion, while still in stealth — so the March 2026 raise represents a roughly 70% jump in valuation on top of already-substantial funding, not a debut round. The comparison point is Physical Intelligence (pi), the San Francisco robotics AI company that [raised a $600 million Series B in November 2025 at a $5.6 billion valuation](https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding). Rhoda's $1.7 billion valuation positions it as an earlier-stage company with a more concentrated technology bet, not yet competing on scale.

---

## The Technology: Direct Video Action

The central technical claim Rhoda makes is that video-based pretraining transfers better to real-world robotic control than reinforcement learning or demonstration-based training alone.

The reasoning is intuitive: the physical world is continuous, and human intuition about physics (what falls, what slides, what breaks) is built from years of visual observation, not from reward functions. A model pretrained on hundreds of millions of internet videos — sports, cooking, construction, manufacturing, nature — has seen an enormous variety of physical cause-and-effect. That prior knowledge is what Rhoda calls the "motion prior": a learned understanding of how objects in the world tend to move and interact.

The Direct Video Action (DVA) architecture works in two phases:

**Pretraining on video.** Rhoda trains foundation models on large-scale internet video to learn motion, physics, and the structure of physical environments. This is not robotic data — it is general video of the physical world. The models learn to predict future video frames: given what the robot sees now, what will the next few hundred milliseconds look like?

**Fine-tuning on teleoperation.** After pretraining, Rhoda fine-tunes models using teleoperation data — a human operator controlling the robot to demonstrate tasks. The key claim is that the strong motion prior from video pretraining means fine-tuning is dramatically more efficient: [Rhoda reports that new tasks can be learned with as little as ten hours of teleoperation data](https://www.therobotreport.com/rhoda-ai-exits-stealth-with-450m-to-train-robots-from-video/), a figure the company's own [press materials](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World) repeat but that has not been independently benchmarked against competing systems.

**Closed-loop action generation.** At inference time, the DVA model continuously observes the robot's environment, predicts future states as video, converts those predictions into specific robot actions (joint positions, gripper states), and executes them. The cycle repeats every few hundred milliseconds. Because the loop is closed — the robot re-observes after each action — it adapts to unexpected changes in its environment rather than executing a pre-planned sequence.

This closed-loop design is what Rhoda emphasizes as the key departure from classical robot programming. A traditional industrial robot executes a sequence of pre-programmed movements. If a part is in the wrong position, the robot fails. The DVA model perceives the world continuously and adjusts; when something is out of place, it updates its prediction and adapts its action.

### The "Reality Gap" Problem

Every robotics AI company has to address the same underlying challenge: systems that work in controlled laboratory settings frequently fail in real production environments. Materials have unexpected textures. Lighting changes. Parts are slightly misaligned. Human coworkers introduce variability. Classical robot programs are brittle because they were not designed to handle this variance.

Rhoda's claimed solution is that continuous video-based prediction naturally handles variability — because the model is always re-predicting rather than following a fixed plan, it responds to what is actually in front of it. [The company cites an industrial manufacturing evaluation](https://www.therobotreport.com/rhoda-ai-exits-stealth-with-450m-to-train-robots-from-video/) where Rhoda systems completed a component-processing workflow in under two minutes per cycle without human intervention, exceeding (unspecified) customer KPIs under production conditions.

Third-party verification of these results is not available. The claim is plausible given the DVA architecture, but the deployment conditions — which specific industry, which specific robot hardware, what definition of "exceeding customer KPIs" — are not publicly disclosed.

---

## The Team

**Jagdeep Singh (CEO and Co-Founder)** is a serial deep-tech entrepreneur. He [co-founded optical networking company Infinera in 2000, took it public in 2007, and led it as CEO](https://en.wikipedia.org/wiki/Infinera) until [Nokia acquired it for $2.3 billion in a deal announced in June 2024](https://www.insidearbitrage.com/2024/06/nokia-announces-2-3-billion-acquisition-of-infinera/). He also [co-founded solid-state battery maker QuantumScape in 2010 and served as its CEO through its 2020 SPAC merger and public listing](https://www.cnbc.com/2020/09/03/bill-gates-backed-ev-battery-supplier-to-go-public-through-spac-deal.html), stepping down as CEO in February 2024 while remaining Chairman of the Board. Singh's track record is in building hardware-facing deep-tech companies to exits and public listings — not software-first AI startups. At Rhoda, his role is the kind of commercial and organizational scaling that requires understanding both engineering constraints and production environments.

**Eric Ryan Chan (Chief Science Officer and Co-Founder)** is a [Stanford researcher specializing in computer vision and generative modeling](https://scholar.google.com/citations?user=TLgngQYAAAAJ&hl=en). Before Rhoda, [Chan served as a generative model architect at World Labs](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World) — the spatial intelligence company [co-founded in 2024 by Stanford computer scientist Fei-Fei Li](https://www.siliconrepublic.com/start-ups/fei-fei-li-world-labs-raises-1bn-to-spatial-intelligence-ai-world-models-marble), who directed Stanford's AI Lab from 2013 to 2018 and now co-directs Stanford's Human-Centered AI Institute. World Labs focuses on building world models that understand 3D spatial structure; Chan's work there was at the intersection of generative models and physical-world understanding, a direct precursor to the video-predictive control approach at Rhoda.

**Gordon Wetzstein (Co-Founder)** is an [Associate Professor of Electrical Engineering at Stanford University and leader of the Stanford Computational Imaging Lab](https://engineering.stanford.edu/people/gordon-wetzstein). [Forbes has separately reported Wetzstein as one of Rhoda's co-founders](https://www.forbes.com/sites/annatong/2025/10/15/two-ai-startups-have-each-raised-100-million-to-build-humanoid-robots-in-stealth/). His research focuses on the intersection of computational optics and machine learning — specifically how camera and display systems can be redesigned to work better with AI perception systems. His involvement at Rhoda reflects the hardware-software integration challenge in physical AI: the sensors a robot uses to perceive the world are as important as the model that interprets what those sensors capture.

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

**Physical Intelligence (pi)** — the most direct comparison. [Founded in 2024 by former Google DeepMind and academic researchers Karol Hausman, Sergey Levine, and Chelsea Finn](https://en.wikipedia.org/wiki/Physical_Intelligence_Inc.), among other co-founders. [Raised a $600M Series B in November 2025 at a $5.6B valuation](https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding), and [was reportedly in talks for a $1B round at an $11B valuation as of late March 2026](https://www.bloomberg.com/news/articles/2026-03-27/ex-deepmind-staffers-robotics-startup-in-talks-for-11-billion-valuation), though that round had not closed as of this writing. Pi's π0 architecture is also hardware-agnostic and learns from human demonstrations. The key technical difference is that pi uses a flow matching approach (diffusion-derived) rather than video-predictive control. Both companies are betting on general robot policies that transfer across hardware; they differ on the architecture of that generality.

**Genesis AI** — [unveiled in May 2026 with a $105M seed round and GENE-26.5, its first foundation model for robotic hands](https://techcrunch.com/2026/05/06/khosla-backed-robotics-startup-genesis-ai-has-gone-full-stack-demo-shows/). Earlier stage, more research-oriented than Rhoda or Physical Intelligence.

**Figure AI** — humanoid robot company [building its own hardware (the Figure 02 robot) and partnering with OpenAI](https://techcrunch.com/2024/08/06/figures-new-humanoid-robot-leverages-openai-for-natural-speech-conversations/) on language-grounded instruction following and speech interaction. Different business model — hardware-centric rather than platform.

**Boston Dynamics** — established player with Spot and Atlas; [in April 2026 it integrated Google DeepMind's Gemini Robotics-ER 1.6 model into Spot](https://spectrum.ieee.org/boston-dynamics-spot-google-deepmind) to add autonomous reasoning, gauge-reading, and spill detection to its industrial-inspection deployments. Legacy advantage in mechanical robustness; newer entrants are competing on AI adaptability.

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

---

**Sources:** [BusinessWire — Rhoda AI exits stealth with $450M Series A](https://www.businesswire.com/news/home/20260310715139/en/Rhoda-AI-Exits-Stealth-with-$450-Million-Series-A-to-Bring-Robots-Out-of-the-Lab-and-Into-the-Real-World) · [The Robot Report — Rhoda AI video-predictive robot training](https://www.therobotreport.com/rhoda-ai-exits-stealth-with-450m-to-train-robots-from-video/) · [TechNode Global — Temasek-backed Rhoda AI $450M Series A](https://technode.global/2026/03/11/temasek-backed-rhoda-ai-raises-450m-series-a-funding-to-accelerate-robotics-development/) · [PYMNTS — Rhoda AI manufacturing and logistics focus](https://www.pymnts.com/news/investment-tracker/2026/rhoda-ai-raises-450-million-to-automate-manufacturing-and-logistics/) · [Reuters via Yahoo Finance — Rhoda AI valued at $1.7B](https://finance.yahoo.com/news/rhoda-ai-raises-450-million-160945418.html) · [Forbes — Rhoda AI and Genesis AI building humanoid robots in stealth](https://www.forbes.com/sites/annatong/2025/10/15/two-ai-startups-have-each-raised-100-million-to-build-humanoid-robots-in-stealth/) · [Bloomberg — Physical Intelligence valued at $5.6B](https://www.bloomberg.com/news/articles/2025-11-20/robotics-startup-physical-intelligence-valued-at-5-6-billion-in-new-funding)
