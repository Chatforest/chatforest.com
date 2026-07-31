---
title: "GPT-5 Pro Solved a Shelved 3-Year T-Cell Mystery. OpenAI's Science Acceleration Evidence Is Real."
date: 2026-06-29
description: "OpenAI's June 2026 feature on immunologist Derya Unutmaz shows GPT-5 Pro cracking a T-cell differentiation puzzle shelved since 2022 -- one data point in a pattern that also includes a 79x gene-editing efficiency result from a separate December 2025 wet-lab collaboration. Here's what the research actually shows for builders working in biotech, pharma, and research tools."
tags: ["openai", "gpt-5", "science", "biology", "immunology", "research", "life-sciences", "builder-guide", "biotech", "ai-for-science"]
draft: false
sources_audited: 2026-07-31
---

On June 24, 2026, OpenAI published a [case study](https://openai.com/index/gpt-5-immunology-mystery/) about immunologist Derya Unutmaz solving a T-cell puzzle his lab had shelved since 2022. It's the kind of story that gets filed under "AI is amazing" and promptly forgotten. That would be a mistake.

The Unutmaz case is not an isolated anecdote. It's one data point in a pattern OpenAI has been documenting across wet labs, math departments, and materials science teams. The pattern is consistent, and it has specific implications for builders — especially given that Anthropic is running its own [AI for Science event tomorrow, June 30](https://chatforest.com/builders-log/anthropic-ai-for-science-june-30-briefing-life-sciences-builder-guide/).

Here is what the evidence actually shows.

## The T-Cell Case

Derya Unutmaz, M.D., is a professor of immunology at [The Jackson Laboratory for Genomic Medicine](https://www.jax.org/research-and-faculty/faculty/derya-unutmaz) in Farmington, Connecticut, and an adjunct faculty member in the [University of Connecticut School of Medicine's Department of Immunology](https://health.uconn.edu/immunology/faculty/). In 2022, his lab ran an experiment comparing how T cells behave in two glucose-deprived conditions: actual low glucose, and deoxyglucose — a molecule that disrupts glucose metabolism rather than simply reducing its availability. ([OpenAI](https://openai.com/index/gpt-5-immunology-mystery/))

The expectation: limited energy should drive similar outcomes in both conditions.

The result: T cells in the deoxyglucose group behaved unexpectedly differently.

The lab couldn't explain the discrepancy. They documented it, shelved it, and moved on to more pressing work. It stayed shelved for three years, until Unutmaz brought the dataset to GPT-5 Pro in late 2025. ([OpenAI](https://openai.com/index/gpt-5-immunology-mystery/))

The model's explanation: deoxyglucose was interfering with the construction of IL-2, a signaling protein. With IL-2 suppressed, T cells were losing a brake that normally prevents them from differentiating into Th17 cells — a class of inflammatory response cells involved in autoimmune disease and cancer resistance.

That mechanism was coherent with decades of immunological literature that Unutmaz's team hadn't connected to their 2022 data. More broadly, Unutmaz has described using GPT-5 Pro to simulate experiments and predict outcomes as a way to narrow down which experiments are worth running in the lab in the first place. ([OpenAI](https://openai.com/index/gpt-5-immunology-mystery/))

GPT-5 Pro was then tested retrospectively, not predictively in real time: Unutmaz gave the model an experiment his lab had already run — but not yet published — on CD8+ T cells engineered to target a type of lymphoma. Asked to simulate the outcome, GPT-5 Pro correctly predicted the enhanced cancer-killing ability the lab had already observed. Because the result wasn't public, OpenAI's account argues the model couldn't have simply recalled it from training data. ([OpenAI](https://openai.com/index/gpt-5-immunology-mystery/))

## The Wet Lab: 79x Efficiency

The T-cell case involved an expert interpreting model output and validating it against domain knowledge. The wet lab story is structurally different: it's an iterative loop with no human optimization -- and it's a separate OpenAI publication from the Unutmaz case, not part of it. OpenAI published this one as ["Measuring AI's capability to accelerate biological research in the wet lab"](https://openai.com/index/accelerating-biological-research-in-the-wet-lab/) on December 16, 2025 -- about six months before the Unutmaz feature -- corroborated by [Robot on Rails' own account](https://www.robotonrails.com/pages/posts/measuring-ai-capability-biological-research.html) of building the robotic execution system used in the same work.

OpenAI partnered with Red Queen Bio, a biosecurity-focused startup, to evaluate GPT-5's ability to design and optimize laboratory protocols. The task: improve the efficiency of a gene-editing cloning procedure. The rules: GPT-5 designs protocols, human researchers execute them exactly, then feed results back to the model. No human modifies or second-guesses the protocol between iterations. ([OpenAI](https://openai.com/index/accelerating-biological-research-in-the-wet-lab/); [Robot on Rails](https://www.robotonrails.com/pages/posts/measuring-ai-capability-biological-research.html))

The model converged on a novel mechanism: co-deployment of RecA (an E. coli recombinase) and gp32 (a single-stranded DNA-binding protein from bacteriophage T4). The two proteins work in tandem — gp32 stabilizes loose DNA ends while RecA guides each strand to its correct complementary match. ([OpenAI](https://openai.com/index/accelerating-biological-research-in-the-wet-lab/))

This was not a known best practice for this class of cloning procedure. No human had proposed it.

The efficiency improvement over baseline: **79x more sequence-verified clones per unit of input DNA**. ([OpenAI](https://openai.com/index/accelerating-biological-research-in-the-wet-lab/); [Robot on Rails](https://www.robotonrails.com/pages/posts/measuring-ai-capability-biological-research.html))

Because this work touches biological research capabilities with potential dual-use implications, OpenAI conducted it in a controlled setting using a benign experimental system. The published account is careful about exactly what was and wasn't enabled. But the core finding is real: GPT-5 designed a novel protocol that meaningfully advanced experimental outcomes.

## The Broader Paper

The Unutmaz T-cell case is one of the case studies collected in a separate OpenAI paper, ["Early science acceleration experiments with GPT-5"](https://openai.com/index/accelerating-science-gpt-5/) ([arXiv: 2511.16072](https://arxiv.org/abs/2511.16072)), published November 20, 2025 with Unutmaz among its co-authors alongside mathematicians, physicists, and materials scientists. (The wet lab / Red Queen Bio result above is not part of this paper — it's the separate report described above, published about a month later.) The paper's scope extends well beyond biology.

**Mathematics and theoretical computer science:** GPT-5 contributed to four new mathematical results, each verified by human authors. The model helped generate proof outlines and propose transformations that mathematicians then validated. In formal domains with tight feedback loops, this is where GPT-5 appears most consistent.

**Physics and computational science:** The model identified analogous structures across fields and proposed simplifying transformations that domain experts hadn't considered.

**Materials science:** GPT-5 proposed synthesis routes and property predictions that were tested experimentally.

The paper is framed explicitly as *early experiments*, not benchmarks. OpenAI is not claiming GPT-5 runs research programs autonomously. What the paper documents is a set of cases where a frontier model accelerated specific stages of the research workflow — hypothesis generation, literature synthesis, experimental design — when used by an expert who controlled the validation loop.

## What The Human-AI Collaboration Model Actually Looks Like

The phrase "AI-augmented research" covers a lot of ground. These case studies give it a specific shape.

The human side provides:
- Experimental context the model doesn't have (what the 2022 T-cell dataset actually measured)
- Domain judgment on which hypotheses are worth pursuing
- Experimental execution and result validation
- Interpretation of whether the model's prediction was right for the right reasons

The model side provides:
- Synthesis across literature at a scale and speed a single researcher can't match
- Parallel hypothesis generation without fatigue bias
- Mechanistic explanations that connect disparate bodies of knowledge
- Protocol optimization through iterative design loops

Unutmaz's own framing is more modest than "replaced immunology": per OpenAI's account, he described models like GPT-5 Pro as now functioning "more like collaborators" — useful for literature synthesis and hypothesis generation, but only as good as the expert judgment that decides which of the model's ideas are worth testing. ([OpenAI](https://openai.com/index/gpt-5-immunology-mystery/))

That framing matters for builders. The failure mode in research tool design is building toward autonomous AI that replaces expert judgment. The successful pattern in these case studies is building infrastructure for *expert-guided AI velocity* — where the model's breadth amplifies a scientist's depth.

## Builder Implications

**Hypothesis generation is now a real use case.** Writing code and summarizing documents have dominated AI tool use since 2023. These case studies establish that frontier AI can participate meaningfully in hypothesis generation and experimental design for domain experts. If you're building research tools, this capability tier is worth designing around.

**Extended reasoning matters for scientific tasks.** GPT-5 Pro with max reasoning effort is what Unutmaz used. For complex mechanism inference across large bodies of literature, standard inference isn't what's delivering results here. The reasoning compute expansion is doing real work.

**Design for the validation loop, not the automation loop.** Every successful case across OpenAI's published accounts involves a human validating the model's output before the next step. The 79x wet lab result was achieved by executing GPT-5's protocols exactly — but the biosecurity framework required human researchers to observe and record results at each iteration. The loop is human-in-the-middle by design, not by limitation.

**Biosecurity will constrain what you can build.** Red Queen Bio exists specifically to think about dual-use implications of biological AI capabilities. OpenAI ran the wet lab work under carefully scoped conditions. Any builder working at the interface of AI and experimental biology will encounter these constraints — and needs to design compliance into the architecture, not bolt it on after.

**Tomorrow's context:** Anthropic's "AI for Science" event on June 30 will present their own evidence of Claude accelerating life sciences research — with case studies from Novartis, Bristol Myers Squibb, and Genentech, and the context of the John Jumper (AlphaFold) hire. The OpenAI and Anthropic cases complement each other: GPT-5's story focuses on hypothesis generation and wet lab protocol design; Anthropic's story centers on enterprise pharma deployment and the Claude accuracy crisis in biological database retrieval. Both are worth tracking.

---

*ChatForest covers AI tools, platforms, and research for builders. All coverage is based on published sources — we research and analyze, we don't run benchmarks or test models directly.*
