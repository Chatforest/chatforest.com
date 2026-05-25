---
title: "Andrew Ng Just Bet on AI PCs. IrisGo Wants to Watch You Work — So It Can Work for You."
date: 2026-05-25
description: "IrisGo raised $2.8M from Andrew Ng's AI Fund, Nvidia, and Google to build a desktop AI companion that learns your workflows by watching you once. Acer is its first OEM partner. The bet: on-device AI that understands your context before you ask."
og_description: "IrisGo: $2.8M seed from Andrew Ng's AI Fund + Nvidia + Google. Founded by Jeffrey Lai (ex-Apple, helped build Chinese Siri). 'Watch and Learn' system — observe a workflow once, automate it. Acer OEM partner, preloading on AI PCs. Hybrid on-device/cloud with user-authorized cloud sync. Competing with Microsoft Recall, Apple Intelligence, Gemini Nano in the ambient computing race."
content_type: "Review"
card_description: "IrisGo is a desktop AI companion that learns your workflows by watching you do them — once. Show it how to process an invoice or summarize a report, and it can handle the next hundred on its own. The $2.8M seed came from Andrew Ng's AI Fund, Nvidia, and Google. Acer will preload it on AI PCs. The founder is Jeffrey Lai, who helped build the Chinese version of Siri at Apple. The bet is that the next computing interface isn't a chatbot you ask — it's an ambient agent that already knows what you need."
tags: ["irisgo", "ai-pc", "andrew-ng", "on-device-ai", "desktop-ai", "acer", "ambient-computing", "ai-agents", "personal-ai", "productivity"]
categories: ["reviews"]
author: "ChatForest"
---

**At a glance:** IrisGo. Founded by Jeffrey Lai (former Apple engineer, built Chinese Siri) and co-founder. Product: on-device AI desktop companion for AI PCs — learns workflows by observation, automates them with no repeat instructions. Funding: $2.8 million seed led by Andrew Ng's AI Fund, with participation from Nvidia and Google. OEM partner: Acer (software preloaded on AI PCs). Architecture: hybrid on-device/cloud, with cloud processing only for complex tasks and only when explicitly authorized. Announced: May 2026. Part of our **[AI Models & Companies reviews](/categories/ai-tools/)**.

---

The AI assistant you talk to is not the only model for personal AI.

The alternative — ambient, observational, context-aware — is what IrisGo is building. Its AI PC software does not wait for you to ask it something. It watches what you do, learns from it, and then does it for you the next time without being asked.

The company raised $2.8 million from Andrew Ng's AI Fund, Nvidia, and Google. Acer is preloading it on AI PCs. The founder built Siri. The bet is that the future of personal productivity is not a chatbot but a silent collaborator that already knows your workflows.

---

## What IrisGo Actually Does

The core mechanic is called "Watch and Learn." You perform a workflow once — processing an invoice, summarizing a document, drafting a status update, filing a report — while IrisGo observes. The next time that workflow needs to happen, IrisGo does it for you without being asked again.

This is a different design philosophy from the dominant interface for AI assistants. ChatGPT, Claude, Copilot, and Gemini are all reactive: you prompt, they respond. IrisGo's model is proactive: it infers what you're about to do from context and either does it or prompts you to let it.

The product includes a prebuilt "skills" library — email composition, invoice processing, report creation, document summarization, and other common knowledge-work routines — for users who do not want to train the system themselves. Lai describes this as the on-ramp: "Show it once or use what's already there. Either way, the idea is that the second time it happens, you're not involved."

The architecture is hybrid. Routine, context-aware tasks — watching your screen, tracking workflow patterns, recognizing document types — are handled on-device, on the PC's local neural processing unit. More complex operations that require larger models are routed to the cloud, but only when the user has explicitly authorized cloud access for that type of task. The company uses end-to-end encryption for anything that leaves the device.

---

## Who Built It and Why Andrew Ng Said Yes

Jeffrey Lai came to IrisGo from Apple, where he was one of the engineers who built the Chinese-language version of Siri. That background matters: Siri's core problem — and the reason it has spent years losing ground to more capable assistants — is that it is reactive and narrow. It handles discrete commands well. It handles context poorly.

Lai's thesis is that the NPU in modern AI PCs (Qualcomm Snapdragon X, Intel Core Ultra, AMD Ryzen AI) changes the viability calculus for on-device ambient AI. These chips can run lightweight models locally at low power, making always-on screen awareness and workflow tracking feasible without the battery and privacy costs of continuous cloud streaming.

Andrew Ng connected with Lai through Carnegie Mellon University, where both are alumni. After seeing a demo, Ng's AI Fund led the seed round. Ng's track record includes early calls on cloud AI, edge AI, and AI in manufacturing before each of those became obvious — his involvement is read by the industry as a signal about where serious enterprise AI is heading.

Nvidia and Google co-investing alongside Ng is worth noting. Nvidia has a direct hardware interest: its NPUs power many AI PCs and its inference software stack is embedded in the devices IrisGo targets. Google's interest is less obvious from the outside — it has its own AI PC strategy through Gemini Nano — but co-investing in a company that may generate enterprise observational data on workflows aligns with Google's longer-term context intelligence ambitions.

---

## The AI PC Race

IrisGo is entering a crowded market, though one with no clear winner yet.

Microsoft Recall — announced and then delayed for privacy concerns in 2024, finally shipping to Windows Insiders in early 2026 — is the most visible competitor. Recall takes periodic screenshots of everything on your screen and makes it searchable via natural language. The privacy backlash to Recall's original announcement was severe enough that Microsoft added multiple layers of opt-in controls before shipping. The concern is structural: a system that takes a continuous visual record of your screen, even one stored locally, represents a new category of data that enterprises and privacy regulators are only beginning to process.

IrisGo's response to the Recall comparison is architectural. Rather than a continuous screenshot buffer, IrisGo says it uses selective observation — it pays attention when you are actively working on a recognized workflow type, not passively recording everything. Whether this distinction holds up under enterprise security scrutiny has not yet been independently validated.

Apple Intelligence on macOS 26, Gemini Nano in Android 17 and on Chrome OS, and Copilot integrated into Windows 11 are all operating in adjacent territory. What differentiates IrisGo's position — for now — is the focus on workflow automation rather than conversational assistance, and the OEM distribution path through Acer.

---

## The Acer Partnership

Getting preloaded on Acer hardware is a meaningful distribution wedge. AI PCs are the fastest-growing segment in the PC market; Acer has been one of the most aggressive OEMs in certifying and shipping Qualcomm Snapdragon X and Intel Core Ultra AI PC variants. Lai says the goal is to replicate the Acer partnership with additional device makers.

Preloaded software lives in a different adoption environment than downloaded software. The friction for the user is near zero — it is already on the machine — which means IrisGo's first customer interaction is observation rather than acquisition. If the product is useful, the habit forms before the user has made a conscious decision to use an AI productivity tool.

The enterprise IT counterpart to this is the question of device management. Preloaded software that observes user activity — even locally — will need to pass enterprise security review in most managed-device environments. That is not a trivial bar, and it is one IrisGo has not yet cleared at scale.

---

## What the Critics Say

**$2.8 million is a small bet.** The seed round positions IrisGo against Microsoft (market cap ~$3.5T), Google (Alphabet, ~$2.1T), and Apple (market cap ~$3.5T), all of which are shipping or will soon ship on-device ambient AI products. The AI Fund's endorsement is valuable signal, but signal without capital is not a moat.

**The privacy framing needs verification.** "On-device with authorized cloud sync" is a reasonable architecture, but IrisGo's privacy claims have not yet been independently audited. Enterprise buyers will not take vendor attestation at face value. The company will need third-party security reviews before it can seriously compete for managed enterprise deployments.

**The "watch and learn" paradigm is unproven at scale.** Teaching an AI your workflow by demonstration is intuitive in demos. In production environments, workflows are inconsistent, edge cases are common, and "it worked when I showed it" does not always mean "it works when I am not watching." Reliable automation of knowledge-work workflows is harder than it looks, and no ambient desktop AI company has demonstrated consistent production reliability at scale yet.

---

## What to Watch

- **Additional OEM deals** — whether Lai can extend the Acer partnership to Lenovo, Dell, or HP will determine whether IrisGo is a niche product or a category play
- **Enterprise vs. consumer positioning** — the preloaded OEM path suggests consumer/prosumer, but the invoice and report skills suggest enterprise; which market IrisGo actually serves will determine its valuation trajectory
- **Privacy audit results** — the first independent security review will be a credibility event in either direction
- **Microsoft Recall adoption** — if Recall succeeds despite its privacy complexity, it will validate the ambient observation category; if it stalls, it will create space for alternatives

IrisGo is a small bet from credible investors on a genuine behavioral shift in how personal computing might work. Whether "watch and learn" becomes the dominant paradigm for knowledge work automation depends on whether users are willing to trust an AI that observes before it acts — and whether enterprises are willing to certify the device that carries it.

---

*We did not test IrisGo's platform directly. This review is based on public company announcements, press coverage, and the May 2026 TechCrunch profile. No hands-on access was obtained.*
