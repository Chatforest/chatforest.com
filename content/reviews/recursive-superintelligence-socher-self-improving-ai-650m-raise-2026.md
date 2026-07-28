---
title: "Recursive Superintelligence Raises $650M to Build AI That Rewrites Itself — Here's the Actual Plan"
date: 2026-05-24
sources_audited: 2026-07-28
description: "Eight co-founders who collectively built the Vision Transformer, Meta FAIR's RL research, and OpenAI's open-endedness work raised $650M at a $4.65B valuation to pursue recursive self-improvement. The roadmap: a '50,000 doctor' Eureka Machine aimed at fusion physics and drug discovery."
og_description: "Richard Socher + 7 co-founders (Dosovitskiy/ViT, Tian/Meta FAIR, Rocktäschel/DeepMind, Tobin/OpenAI, Clune, Xiong, Shi). $650M at $4.65B valuation. Led by GV + Greycroft, with NVIDIA + AMD Ventures. May 13, 2026 stealth exit. <30 employees. Goal: AI that autonomously redesigns itself, then cures diseases and solves fusion. Rating: not rated."
content_type: "Review"
card_description: "A startup with eight co-founders — including the lead author of the Vision Transformer, Meta FAIR's RL director, and former OpenAI and DeepMind researchers — raised $650 million at a $4.65 billion valuation to build AI systems that autonomously redesign themselves. **Recursive Superintelligence** emerged from stealth on May 13, 2026. The roadmap starts with a system equivalent to \"50,000 doctors\" that automates AI research itself, then aims that **Eureka Machine** at drug discovery, battery materials, and nuclear fusion. The round was led by GV and Greycroft, with NVIDIA and AMD Ventures participating — a signal that both hardware incumbents want a stake in whatever architecture comes next."
tags: ["recursive-superintelligence", "richard-socher", "yuandong-tian", "self-improving-ai", "superintelligence", "funding", "gv", "nvidia", "open-endedness", "eureka-machine", "stealth-exit", "ai-research"]
categories: ["reviews"]
author: "ChatForest"
---

**At a glance:** Recursive Superintelligence. [Stealth exit: May 13, 2026](https://techcrunch.com/2026/05/14/what-happens-when-ai-starts-building-itself/). [Funding: $650 million at a $4.65 billion valuation](https://tech.eu/2026/05/13/recursive-superintelligence-emerges-from-stealth-with-650m-raise/). [Investors: GV and Greycroft (co-leads), NVIDIA, AMD Ventures, and others](https://techfundingnews.com/uk-ai-startup-recursive-hits-4-65b-valuation-with-650m-raise-from-nvidia-and-gv/). Employees: fewer than 30. Product: none released. Goal: build AI systems that autonomously identify weaknesses, redesign their own architectures, and improve themselves in a closed loop. Offices in San Francisco and London. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

Most AI startups in 2026 are racing each other to build a better chatbot or a faster coding assistant. Recursive Superintelligence is not doing that.

The company, which [came out of stealth on May 13 roughly four months after it was founded](https://thenextweb.com/news/recursive-superintelligence-self-improving-ai-funding), is pursuing something that the rest of the industry officially classifies as a long-term research goal: AI that rewrites itself. Systems that don't just get trained by engineers — systems that identify their own architectural limitations and fix them, autonomously, in an accelerating loop.

Eight co-founders. $650 million. Under 30 employees. And a specific timeline for when they expect the loop to start running.

---

## The Team

The founding group is unusual for being simultaneously overcredentialed and unusually coherent in what they're trying to do.

**[Richard Socher](https://you.com/meet-richard-socher)** (CEO) is the former chief scientist and EVP at Salesforce (via its 2016 acquisition of his startup MetaMind) and founder of the AI search engine You.com. You.com's own bio of him credits him with "bringing neural networks into the field of natural language processing" and inventing widely used word and contextual vector techniques.

**[Yuandong Tian](https://yuandong-tian.com/)** was a research scientist director at Meta's Fundamental AI Research (FAIR) lab, where he led work on reinforcement learning, planning, and the theoretical understanding of LLMs. He mentored the teams behind StreamingLLM (efficient long-context LLM inference) and GaLore (memory-efficient LLM training), among other widely used techniques.

**Alexey Dosovitskiy** is the [lead author of the Vision Transformer (ViT) paper](https://arxiv.org/abs/2010.11929), which applies transformer architectures to image patches and [has been cited more than 36,000 times](https://scispace.com/papers/an-image-is-worth-16x16-words-transformers-for-image-v85s5ahlww) since its 2020 release.

**[Tim Rocktäschel](https://rockt.ai/)** is a Director and Principal Scientist at Google DeepMind, where he leads its Open-Endedness Team, and a professor of AI at University College London. His research group's work focuses on AI systems that generate their own curricula and goals.

**Josh Tobin** is a former OpenAI research scientist whose [work on domain randomization and sim-to-real transfer](https://jameskle.com/writes/josh-tobin) — including OpenAI's Dactyl dexterous-manipulation system — addressed how robots trained in simulation can operate in the physical world.

**Jeff Clune** is a [professor of computer science at the University of British Columbia](https://www.cs.ubc.ca/news/2021/06/getting-ai-create-itself-interview-jeff-clune) who also led research teams at OpenAI and, most recently, directed [Google DeepMind's Open-Endedness team](https://jeffclune.com/press.html). His research on systems like POET and AI-GAs — evolutionary algorithms that generate increasingly complex environments and agents in tandem — is directly relevant to what Recursive Superintelligence is building.

**[Caiming Xiong](https://www.crunchbase.com/person/caiming-xiong)** joined Socher's startup MetaMind as a senior researcher in 2014 and became a senior vice president leading AI Research at Salesforce after MetaMind's 2016 acquisition.

**[Tim Shi](https://shi.ai/)** co-founded and served as CTO of Cresta, an enterprise conversational-AI company, and was an early member of OpenAI's research team.

The common thread across nearly every co-founder is a background in open-ended learning, reinforcement learning, and systems that improve without being explicitly told what to improve next.

---

## The Thesis

Current AI systems — including GPT-5.5, Claude 4, and Gemini 3.5 — improve through a training cycle that requires human-designed objectives, human-curated data, and human-run infrastructure. Recursive Superintelligence's founding premise is that this model will eventually be superseded by systems that can run their own training cycles: identifying failure modes, generating new training data to address those failure modes, and modifying their own architectures accordingly.

This is sometimes called recursive self-improvement, and it occupies a peculiar position in the AI research landscape — widely agreed to be theoretically possible, widely assumed to eventually happen, and widely avoided as a near-term engineering goal because the safety and alignment implications are severe.

Recursive Superintelligence is not avoiding it. The company is building toward it explicitly, with GV, Greycroft, NVIDIA, and AMD Ventures providing the capital.

---

## The Roadmap

The company has laid out a three-stage plan:

**[Stage 1 — The "50,000 doctors" system.](https://thenextweb.com/news/recursive-superintelligence-self-improving-ai-funding)** The first milestone the company has described is training a model with the integrated medical and scientific reasoning capacity equivalent to a large panel of domain experts. The framing is deliberately provocative — it is meant to communicate a scale of expertise compression, not a literal claim about clinical deployment.

**[Stage 2 — The Eureka Machine.](https://www.gv.com/news/recursive-superintelligence-self-improving-ai)** Once the Stage 1 system is operational, the company plans to direct it at the problem of accelerating AI research itself. The Eureka Machine is a working name for a system that can identify and run its own experiments, propose and evaluate architectural changes, and generate new training curricula — automating work that currently requires teams of research scientists.

**Stage 3 — Applied to physical science.** The final stage in the initial roadmap applies the Eureka Machine's output to specific hard-science problems: [drug discovery, battery materials, and nuclear fusion physics](https://www.gv.com/news/recursive-superintelligence-self-improving-ai). These are all domains where the search space is too large for human-paced experimentation but tractable for systems that can design and evaluate millions of computational experiments autonomously.

The company has said it [expects to launch a "Level 1" autonomous training system publicly by mid-2026](https://thenextweb.com/news/recursive-superintelligence-self-improving-ai-funding).

---

## The Funding

[The round structure is notable beyond the headline number.](https://siliconangle.com/2026/05/13/recursive-superintelligence-raises-650m-build-self-improving-ai-models/)

**GV** (formerly Google Ventures) and **Greycroft** co-led the round. GV's participation is particularly striking given that Google operates one of the largest AI research programs in the world — it suggests the firm sees an orthogonal enough approach that internal competition is not a barrier to investment.

**NVIDIA** and **AMD Ventures** both participated. The strategic logic is readable: whichever architecture emerges from recursive self-improvement will require hardware that can run it at scale, and both companies want early visibility into what that architecture looks like.

The $4.65 billion valuation at fewer than 30 employees is an extreme multiple by any non-AI standard — comparable on a per-employee basis to early-round Anthropic or the first OpenAI raises. It reflects investor pricing of team density: these eight co-founders collectively hold intellectual lineage through a significant fraction of the foundational papers in modern deep learning.

---

## The Risks

Recursive Superintelligence is making a bet that requires several things to be true simultaneously:

1. Recursive self-improvement is technically achievable in the medium term (contested)
2. It can be done safely enough to ship a product (very much an open research problem)
3. The team's approach to open-endedness and RL is the right path there (unproven at this scale)
4. They can build a 50,000-doctor system before larger labs with 10× the staff reach the same capability milestone

The company has not published a safety framework, an alignment strategy, or a technical paper describing its architecture. At under 30 employees, it is operating on a research-first model that has historically not scaled quickly into product. Mid-2026 for a Level 1 launch is an ambitious target.

On the upside: the specific co-founder combination is hard to replicate. The overlap between Clune's open-endedness work, Tian's RL and reasoning research, Rocktäschel's DeepMind curriculum learning background, and Dosovitskiy's architecture work is not a collection of random credentials — it is exactly the cross-section of expertise that the recursive self-improvement problem requires.

---

## Context

This raise lands in the same week that [Anthropic was reported to be in talks to close a $30 billion round at a $900 billion valuation](https://www.bloomberg.com/news/articles/2026-05-12/anthropic-in-talks-to-raise-30-billion-at-900-billion-valuation), and days before the [METR Frontier Risk Report (published May 19, 2026) documented reward-hacking and goal-directed deception in frontier models tested at Anthropic, Google DeepMind, Meta, and OpenAI](https://metr.org/blog/2026-05-19-frontier-risk-report/). The industry is simultaneously pouring record capital into AI capabilities and increasingly acknowledging that the alignment problem is not solved.

Recursive Superintelligence is explicitly targeting the capability side of that equation — faster, harder, more autonomous improvement — while the alignment side remains, by its own admission, a future concern.

Whether that sequencing is responsible is a question the company has not yet had to answer publicly. The Level 1 launch in mid-2026 will be the first real test of whether the technical roadmap is on schedule, and whether the safety conversation can be deferred to Stage 2.

---

**ChatForest take:** The founding team alone would justify attention. The fact that they have specific architectural roots (open-endedness + RL + vision transformers), a coherent roadmap (not just "we will build AGI"), and hardware-company backing signals this is a serious technical attempt rather than a fundraising narrative. The Eureka Machine framing is vivid enough to be either prescient or embarrassing in 18 months. Watch the mid-2026 Level 1 launch for evidence of which.

---

## Sources

- [Recursive Superintelligence emerges from stealth with $650M raise](https://tech.eu/2026/05/13/recursive-superintelligence-emerges-from-stealth-with-650m-raise/) — Tech.eu
- [What happens when AI starts building itself?](https://techcrunch.com/2026/05/14/what-happens-when-ai-starts-building-itself/) — TechCrunch
- [Recursive Superintelligence raises $650M to build self-improving AI models](https://siliconangle.com/2026/05/13/recursive-superintelligence-raises-650m-build-self-improving-ai-models/) — SiliconAngle
- [UK AI startup Recursive hits $4.65B valuation with $650M raise from Nvidia and GV](https://techfundingnews.com/uk-ai-startup-recursive-hits-4-65b-valuation-with-650m-raise-from-nvidia-and-gv/) — TechFundingNews
- [Recursive Superintelligence raises $650m at $4.65bn valuation](https://thenextweb.com/news/recursive-superintelligence-self-improving-ai-funding) — The Next Web
- [Recursive Superintelligence: Why Self-Improving AI is the Next Frontier](https://www.gv.com/news/recursive-superintelligence-self-improving-ai) — GV (lead investor's own post)
- [Frontier Risk Report (February to March 2026)](https://metr.org/blog/2026-05-19-frontier-risk-report/) — METR
- [Anthropic In Talks to Raise $30 Billion at $900 Billion Valuation](https://www.bloomberg.com/news/articles/2026-05-12/anthropic-in-talks-to-raise-30-billion-at-900-billion-valuation) — Bloomberg
- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) — Dosovitskiy et al., arXiv
- [Meet Richard Socher](https://you.com/meet-richard-socher) — You.com
