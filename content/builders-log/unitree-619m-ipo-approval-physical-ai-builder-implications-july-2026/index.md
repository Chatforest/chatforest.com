---
title: "Unitree's $619M IPO Approval: What Physical AI's First Pure-Play Public Company Means for Builders"
date: 2026-07-15
description: "On July 3, 2026, China's CSRC approved Unitree Robotics' $619M STAR Market listing — the fastest major robotics IPO review on record. Humanoid robots rose from 1.9% to 51.5% of revenue in two years. Here is what the numbers say about physical AI as a builder opportunity."
tags: ["robotics", "physical-ai", "unitree", "ipo", "humanoid-robots", "china", "embodied-ai", "builder-guide", "lerobot", "sdk"]
---

On July 3, 2026, [China's securities regulator approved Unitree Robotics](https://www.caixinglobal.com/2026-07-03/unitree-robotics-wins-approval-for-618-million-star-market-ipo-102460136.html) for a listing on the Shanghai STAR Market. The company plans to raise approximately [4.2 billion yuan — roughly $619 million](https://cryptobriefing.com/unitree-619m-shanghai-ipo-ai-robotics/) — with a debut expected before the end of July. The review cleared in 73 days, [one of the fastest on record for a STAR Market listing of this size](https://autonews.gasgoo.com/articles/news/csrc-approves-unitrees-star-market-ipo-2073033635312484353).

Unitree builds quadruped robots (Go2, B2) and humanoid robots (H1, G1, H2). You may have seen the videos: robots doing backflips, climbing stairs, doing push-ups alongside humans. What the IPO filing reveals is that behind the demos is a company that is profitable, growing fast, and earning hardware-company margins that most software businesses would envy.

This article is research-based. We are reading the IPO filings, analyst coverage, and developer documentation — not testing robots.

---

## The Numbers That Signal Physical AI Is Real

[Unitree reported 1.699 billion yuan ($250 million) in revenue for fiscal year 2025, with net profit of 278 million yuan ($41 million).](https://kraneshares.com/a-complete-guide-to-unitree-robotics-2026-ipo-why-it-matters-for-star-market-etf-kstr-humanoid-robotics-etf-koid/) This is a profitable hardware company. In robotics, that is unusual.

More striking is the revenue mix shift:

| Period | Humanoid revenue share |
|--------|------------------------|
| 2023   | 1.9% |
| 2024   | 27.6% |
| H1 2025 | 51.5% |

Humanoid robots went from a rounding error to the majority of Unitree's business in roughly two years. The company shipped more than 5,500 humanoid units in 2025. Gross margin reached 59.5% — exceptional for a hardware manufacturer, comparable to mature software companies.

The IPO proceeds are earmarked for four uses: developing AI models for robots, researching robot structures, creating new robot products, and building a smart manufacturing facility. In other words: the capital goes into deepening the software and AI layer, not just scaling the factory.

---

## The China Strategic Context

Unitree's IPO is not just a company milestone. It is a data point in a deliberate national strategy.

China's 15th Five-Year Plan (2026–2030) explicitly names embodied artificial intelligence as a key strategic industry, placed in the same category as quantum computing, 6G, nuclear fusion, and brain-computer interfaces. The state-backed National AI Fund has committed to embodied intelligence as an investment priority.

The scale of the existing lead is significant. According to research firm Omdia, Chinese companies accounted for roughly 87% of all humanoid robots shipped globally in 2025, with six of the top ten producers based in China. Provincial governments in Hangzhou, Shanghai, and Beijing are competing to attract humanoid manufacturing clusters.

WAIC 2026 opens in Shanghai on July 17 — two weeks after Unitree's IPO approval. Physical AI will almost certainly feature prominently across the 100,000-square-meter exhibition floor and its 300+ product debuts. Xi Jinping's opening keynote is expected to reinforce embodied AI as a national priority alongside AI governance.

---

## The Developer Platform

Unitree's robots are not closed platforms. The company publishes `unitree_sdk2`, an open SDK that supports Go2, B2, H1, G1, H2, R1, and A2 robots. Python and C++ interfaces are available.

For builders specifically interested in embodied AI policy training, the `unitree_lerobot` framework is the relevant integration point. It connects Unitree hardware to Hugging Face's LeRobot library, handling standardized data conversion, policy training, inference, and closed-loop real-world deployment. If you are building imitation learning or reinforcement learning pipelines, Unitree robots are now a mainstream deployment target with documented integration paths.

The G1 humanoid is fully ROS2-compatible, converting sensor data to standard ROS messages for integration with SLAM, navigation, and manipulation pipelines. H1 and G1 developer guides are published at support.unitree.com.

Key platforms for building on Unitree hardware:

- **NVIDIA Isaac Sim**: Unitree robots are supported for sim-to-real transfer workflows
- **LeRobot (Hugging Face)**: End-to-end embodied AI via `unitree_lerobot`
- **ROS2**: Native support on G1 for research and navigation pipelines
- **unitree_sdk2**: Direct hardware control in Python or C++

---

## What the IPO Signals for Builders

**Physical AI has a public market benchmark.** Until now, robotics companies have been private-market bets. Unitree joining UBTech as a listed pure-play humanoid company creates a price signal that venture investors, corporate strategy teams, and acquirers can reference. That benchmark tends to unlock capital in adjacent areas.

**The software layer above the hardware is white space.** Unitree and its peers are hardware companies. The software they ship — autonomy stacks, manipulation policies, enterprise integrations, fleet management, data pipelines for simulation — is still largely underdeveloped. The pattern is the same as cloud computing: once the infrastructure layer went public, the software layer above it compounded much faster.

**Vertical applications are the near-term opportunity.** The industries that have placed early orders — manufacturing (inspection, assembly assist), logistics (last-mile and warehouse), and elder care — all have specific workflow software needs. A builder who deeply understands one of those verticals and can wire Unitree's SDK into it is in an earlier and more defensible position than one building general-purpose robotics tooling.

**The compute stack for physical AI is different.** On-device inference, multi-modal sensing (depth, force, proprioception), and sub-100ms latency requirements make edge deployment on robotics hardware a distinct engineering problem from cloud-based AI. Builders who develop intuition for edge model optimization, quantization, and real-time control loops are acquiring skills that will compound as the physical AI market grows.

---

## What to Watch

**Actual trading date**: Unitree is expected to debut on the Shanghai STAR Market before the end of July 2026. The underwriting, pricing, and subscription process is being finalized now.

**WAIC announcements (July 17–20)**: Unitree is highly likely to exhibit at WAIC. Watch for new product reveals, partnership announcements, or developer program news that could accompany the pre-IPO visibility push.

**Figure AI and 1X Technologies**: Figure AI (US-based) and 1X Technologies (Norway, backed by OpenAI) are the most-watched Western comparables. A Unitree IPO will pressure their investors to clarify timelines or valuations.

**API and developer program expansion**: IPO proceeds are earmarked for AI model R&D and new products. Watch whether that includes expanded developer tooling, a managed cloud API for the robot fleet, or a simulation environment beyond Isaac Sim.

**Gross margin sustainability**: 59.5% is high. As competitors scale production and drive down component costs, that margin will face pressure. The rate at which Unitree converts hardware revenue to recurring software or data revenue is the long-term signal.

---

The core story is straightforward: a profitable hardware company shipping thousands of humanoid robots per year has just received regulatory approval for a $619M IPO on a national exchange, backed by a government plan that treats embodied AI as strategic infrastructure. That is a different category of validation than a Series C or a viral demo. For builders deciding where to invest time in the physical AI stack, the Unitree IPO is a useful calibration point.
