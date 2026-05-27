---
title: "AI Safety Guardrails Stripped From Meta and Google Models in Minutes — Here's What That Means"
date: 2026-05-27
description: "A Financial Times investigation with AI safety group Alice found that Llama 3.3's safety mechanisms could be removed in under 10 minutes using four lines of code. Gemma 4's fell within 90 minutes of release."
tags: ["ai-safety", "meta", "google", "open-source", "llama", "gemma", "security", "ai-industry"]
rating: 4
---

## The Demonstration

On May 25, 2026, the *Financial Times* published an investigation conducted with AI safety research group Alice that established something uncomfortable: the safety guardrails built into major open-source AI models can be removed by an ordinary person with no specialist hardware.

A journalist working with Alice removed Meta's Llama 3.3 guardrails in under ten minutes using four lines of code. Google's Gemma 3 was similarly stripped. Google's Gemma 4 — which had just launched — had its safeguards removed within 90 minutes of release.

The models, once stripped, produced output that the safety systems were explicitly designed to prevent:

- **Gemma 3** generated instructions for dispersing chlorine gas through a crowded indoor space, code to steal credit card information, and stories describing child sexual abuse.
- **Llama 3.3** provided precise lethal dosages of ricin calibrated to a person's body mass.

This is not a theoretical paper. It happened. The tools used are publicly available, and they are being used at scale.

---

## The Technique: Abliteration

The method used is called **abliteration**. Unlike jailbreaking — which tries to trick a model into ignoring its safety instructions through cleverly crafted prompts — abliteration surgically removes the neural pathways that cause the model to refuse. The safety mechanisms are not bypassed. They are deleted.

The process is automated and, according to researchers, "operates completely automatically." No deep ML expertise is required.

Two tools have made abliteration accessible to the general public:

**Heretic** — a GitHub-hosted tool that automates the abliteration process. Since its release in late 2025, Heretic has been used to create more than 3,500 "decensored" model variants, which have been downloaded 13 million times from Hugging Face.

**OBLITERATUS** — released March 4, 2026 by a developer known as "Pliny the Liberator." The open-source toolkit supports 116 different models and runs on consumer hardware via a user-friendly Hugging Face Spaces interface.

These tools are not hidden on dark web forums. They are on mainstream AI development platforms, operating under the same terms as other research code.

---

## Company Responses

**Google** acknowledged the issue, calling abliteration "a known technical challenge facing all open models" and noting that its open models "undergo rigorous internal safety evaluations prior to launch." That framing — treating abliteration as an expected environmental hazard rather than a product failure — signals that Google does not believe a fix is straightforward.

**Meta** declined to comment publicly. A person close to the company indicated that Meta assesses its open-source models' capabilities before releasing them. What that assessment concludes about models that will immediately be stripped of their safety layers is unclear.

**GitHub** has allowed Heretic and similar tools to remain on the platform, citing a policy that permits educational security code while prohibiting tools designed for direct attacks. The distinction between "educational" and "operational" is doing significant work in that policy.

---

## The Open-Weight Tradeoff

Closed-model systems — Claude, ChatGPT, Gemini accessed through the API — are not directly vulnerable to abliteration. Their weights are not public. To remove safety guardrails from a closed model, you would need to steal the model first.

Open-weight models are different. Once weights are released, the developer no longer controls what users do with them. Abliteration is not a bug Meta or Google can patch; it is a structural consequence of releasing model weights into a world where those weights can be modified.

This creates a genuine dilemma for the open-source AI movement, which has argued — correctly — that open weights democratize access, enable independent research, reduce dependence on a handful of powerful companies, and allow users to run models locally without sending their data to a third party. Those arguments remain valid.

But open weights also democratize the ability to remove safety mechanisms. Kawin Ethayarajh, an assistant professor of applied AI at the University of Chicago's Booth School of Business, put it plainly: stripping guardrails is now "much easier for the average person."

---

## What This Changes

The practical security picture shifts in a few specific ways:

**Enterprise AI threat models need updating.** Organizations evaluating open-weight models for internal deployment now have to treat a stripped, unguarded version of that model as realistically within reach of a moderately motivated insider or attacker. The default assumption that "the model has safety guardrails" does not hold once weights leave the lab.

**The weight-release decision is a safety decision.** Model developers releasing open weights are effectively making a permanent, irrevocable choice. The FT investigation documented this vividly: Gemma 4's safeguards fell within 90 minutes of release. There is no window in which a company can release weights, observe usage, and then claw them back if problems emerge.

**Safety filtering is not the same as safety.** Ethayarajh raised a subtler point: simply omitting harmful training data does not necessarily make a model safe. A model trained without dangerous knowledge may become "naive" — unable to recognize when it is being manipulated for malicious ends — while still being ablatable into producing dangerous outputs from the underlying knowledge it has absorbed indirectly. The relationship between training data, safety training, and model capability is not as clean as it might appear.

---

## The Broader Stakes

This story is not primarily about bad actors who want to cause harm. Most of those 13 million downloads of decensored models are probably not for dangerous purposes. People remove guardrails to write unrestricted creative fiction, to ask blunt questions without being lectured, to use models without content filters they find paternalistic. That use case is real and widespread.

The problem is that capability without restriction is available to everyone in the same download. The 13 million downloads are not screened for intent. The chlorine gas instructions and the creative fiction come from the same stripped model.

The open-source AI ecosystem built an impressive edifice of safety work — RLHF, constitutional AI, red-teaming, safety evaluations — all of which can be removed in four lines of code and ten minutes by someone who does not know what RLHF stands for.

That is the finding. What to do about it is a harder question that no one has answered yet.

---

*Sources: Financial Times / Alice safety group investigation (May 25, 2026); Irish Times, Eweek, Futurism, Cointelegraph follow-up coverage. ChatForest covers AI industry developments; we do not independently test or reproduce the techniques described.*
