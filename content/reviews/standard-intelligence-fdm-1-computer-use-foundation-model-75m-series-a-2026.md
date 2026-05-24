---
title: "Two 21-Year-Olds Trained a Computer-Use Model on 11 Million Hours of Video. Sequoia Just Valued It at Half a Billion Dollars."
date: 2026-05-24
description: "Standard Intelligence's FDM-1 is a foundation model for computer use — trained on 11 million hours of raw screen recordings, not annotated screenshots. The six-person company just raised $75M at ~$500M valuation. Andrej Karpathy is an angel investor."
og_description: "Standard Intelligence raised $75M Series A (Sequoia + Spark Capital) at ~$500M valuation for a six-person team. FDM-1: computer-use foundation model trained on 11M hours of raw video — 550,000× larger than the previous best public dataset. 11ms latency. Drove a Toyota RAV4 on SF streets after <1 hour of fine-tuning. Founders Galen Mead (21) and Devansh Pandey (20) met through the Atlas Fellowship. Andrej Karpathy is an angel investor."
content_type: "Review"
card_description: "Standard Intelligence raised a **$75 million Series A** (Sequoia + Spark Capital) at a **~$500 million valuation** for a six-person team in San Francisco. Their product, **FDM-1**, is a foundation model for computer use — trained on **11 million hours of raw screen recording video**, compared to the previous best publicly available dataset of under 20 hours. The approach mirrors Tesla's self-driving playbook: skip the annotation bottleneck and train on internet-scale observational data instead. Andrej Karpathy is an angel investor. Co-founders Galen Mead and Devansh Pandey are 21 and 20 years old. They met as teenagers at the Atlas Fellowship, a scholarship program for students working on AI alignment."
tags: ["standard-intelligence", "fdm-1", "computer-use", "foundation-model", "ai-agents", "funding", "sequoia", "spark-capital", "andrej-karpathy", "atlas-fellowship", "autonomous-agents"]
categories: ["ai-ml-tools"]
author: "ChatForest"
---

**At a glance:** Standard Intelligence (si.inc). Product: FDM-1 ("The First Fully General Computer Action Model"). Founded: ~2024, San Francisco. Team: six people. Funding: $75M Series A at ~$500M post-money valuation (announced April 30, 2026). Investors: Sequoia (Sonya Huang), Spark Capital (Yasmin Razavi), Andrej Karpathy (angel), Stanley Druckenmiller (angel). Founders: Galen Mead (21) and Devansh Pandey (20). Part of our **[AI Models & Companies reviews](/categories/ai-ml-tools/)**.

---

In 2022, Galen Mead and Devansh Pandey were teenagers attending the Atlas Fellowship, a selective scholarship program for high school students focused on AI alignment and AGI. They weren't at a university yet. They hadn't started a company. They were 17 and 16 years old.

Four years later, they are 21 and 20. They run a six-person company with $75 million in Series A funding and a valuation that most decade-old startups never reach. Their backers include Sequoia Capital, Spark Capital, Andrej Karpathy, and Stanley Druckenmiller.

Their product, FDM-1, was trained on 11 million hours of video of humans using computers.

The previous best publicly available computer-use training dataset contained under 20 hours.

---

## The Problem with Teaching AI to Use a Computer

The dominant approach to AI computer use — from Anthropic's Claude computer use, to OpenAI's Operator, to Google's Project Mariner — shares the same architecture: take a frontier language model, show it screenshots, let it reason in text about what to click next.

This approach works. It also has a fundamental ceiling.

Screenshots are static. They strip away everything temporal about how a person actually uses a computer: the mouse movement between clicks, the hesitation before a keystroke, the scroll pattern that tells you where someone's attention is. More importantly, building datasets out of annotated screenshots is expensive and slow. You need human contractors to label every action. The data is bottleneck-constrained from the start.

Standard Intelligence's argument is that this annotation approach is wrong at the architectural level — not just suboptimal, but permanently limited in a way that will hold computer-use models back as long as the field relies on it.

Their alternative: forget the screenshots. Train on raw video.

---

## 11 Million Hours of Video

FDM-1 was announced on February 23, 2026. The launch post described a training corpus of **11 million hours of screen recording video** — film editing workflows, coding livestreams, video game playthroughs, general computer use captured from internet-scale sources.

To put that number in context: the largest previously published public computer-use dataset contained under 20 hours of annotated data. The Standard Intelligence corpus is roughly **550,000 times larger**.

They didn't annotate all 11 million hours by hand. That would be impossible. Instead, they used a phased approach:

1. Human contractors manually labeled **40,000 hours** of video — enough to teach a model what actions correspond to what visual context.
2. That labeled subset was used to train an **Inverse Dynamics Model (IDM)**: a model that watches video and predicts what action was taken between two frames.
3. The IDM then automatically labeled the remaining ~10.96 million hours.

This is the lever that makes internet-scale computer-use training tractable. You don't need to annotate everything. You annotate enough to bootstrap a labeler, then let the labeler do the rest.

Sequoia's framing in their investment writeup described the approach as "Tesla's self-driving playbook applied to knowledge work." Tesla didn't label every edge case in its training data by hand. It captured billions of miles of real driving footage and used fleet learning to extract signal at scale. The bet at Standard Intelligence is that the same transition — from data-constrained to compute-constrained — will unlock computer-use models the way it unlocked self-driving.

---

## What FDM-1 Actually Does

Standard Intelligence describes FDM-1 as "The First Fully General Computer Action Model." The model takes a live 30 FPS video stream of a computer screen and predicts the next action to take — where to move the mouse, what to click, what to type — with **11 milliseconds of round-trip latency** from screen capture to action.

The demos in the February 2026 launch included:

**CAD modeling:** The model performed continuous 3D design operations in Blender — extruding faces, manipulating geometry — using mouse movements that require spatial continuity rather than discrete click-to-click jumps.

**Vehicle control:** After less than one hour of fine-tuning on driving data, FDM-1 operated a vehicle via keyboard inputs on public streets in San Francisco using live visual feeds. The model had never been trained to drive a car. It watched human drivers for an hour and extrapolated.

**Software testing:** The model autonomously explored application state spaces to discover bugs — a form of GUI fuzzing that requires navigating unfamiliar UI without explicit instructions.

The token efficiency underlying these capabilities is notable. FDM-1's video encoder processes approximately **36,000 frames per 200,000 tokens**, versus 775 for Gemini and 162 for Claude in comparable conditions. The company claims their encoder is **50 times more efficient than prior art** and **100 times more efficient than OpenAI's video encoder** specifically. On a single H100 GPU, the inference system runs 42 virtual machines in parallel; their evaluation infrastructure processes over one million rollouts per hour across 80,000 forking VMs.

At a practical level: the model can maintain roughly **two hours of 30 FPS video** in context — enough to watch a full afternoon of human work before acting.

---

## The Investors

Sequoia Capital led the Series A, with partner Sonya Huang leading for the firm. Spark Capital co-led, with partners Yasmin Razavi and Miko Ashwill joining the round.

The angel roster is notable on its own. **Andrej Karpathy**, one of the founding members of OpenAI and former head of Tesla AI, is an investor. Karpathy has been public about his views on AI and scaling; his presence as an angel is a meaningful signal in a field where he is one of the most credible independent validators. **Stanley Druckenmiller**, the macro investor, also participated.

The post-money valuation reported by The Information is approximately **$500 million** for a team of six people and a product with no disclosed commercial customers.

That is a significant bet on what the model represents — not what it has already sold, but what a fully general computer-use foundation model could become if the scaling thesis holds.

---

## What Isn't Public

Standard Intelligence has not published scores on standard industry benchmarks like OSWorld or WebArena. Their February launch materials used an internal benchmark suite — covering typing accuracy, mouse precision, UI manipulation, memory, and CAD operations — but independent third-party validation has not been released.

The product is not publicly available as of May 2026. Access is invite-only, requested through [email protected]. No pricing, no named customers, no production API.

The "FDM" acronym has not been officially explained by the company. Secondary coverage has suggested "Foundation Desktop Model" or "Foundation Dynamics Model," but neither has been confirmed in the company's own published material.

For all the scale of the training corpus and the technical credibility of the approach, FDM-1 is, at this point, a research model backed by significant investor conviction — not a shipping product with enterprise contracts.

That's not unusual at this stage. It's a normal place for a model with this level of ambition to be fourteen months after founding. But it's worth being precise: the $500 million valuation is priced on the ceiling of what this approach could achieve, not on its current commercial output.

---

## Why This Matters

The standard framing for AI computer use treats it as an application layer problem: take a good general model, add tools for taking screenshots and clicking, hope it reasons correctly about what to do.

Standard Intelligence is arguing that this framing is wrong — that the right model for computer use is one that was built for computer use from the ground up, trained on the same kind of raw observational data that human children learn from, at internet scale.

The analogy to self-driving is instructive not just because Tesla won with scale, but because the companies that tried to shortcut scale with hand-crafted rules and annotated edge cases mostly didn't. The question for FDM-1 is whether the same dynamic holds for knowledge work: whether a model trained on 11 million hours of people using computers will generalize better than a language model that has been told, in text, how to click a button.

The investors who backed Standard Intelligence think the answer is yes. Andrej Karpathy, who helped build the most important LLM company on the planet and then built Tesla's data-driven self-driving approach, thinks it's yes too.

Two years ago, the founders were teenagers at a scholarship program for students thinking about AI alignment. Now they're building one of the most technically distinctive computer-use systems in the world, with $75 million and a mandate to scale training by several orders of magnitude.

The car drove itself down a street in San Francisco after less than an hour of fine-tuning. The question is what 11 million more hours of video will teach it to do next.

---

*ChatForest researches and writes about AI tools, models, and infrastructure. Our coverage of Standard Intelligence is based on the company's published blog post, Sequoia Capital's investment writeup, and reporting from SiliconAngle, The Information, AI2Work, and other outlets. FDM-1 is not available for public testing; this article is based on research, not hands-on use.*
