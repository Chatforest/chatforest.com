---
title: "Anthropic's 2028 AI War Game: America Has a 4-11x Compute Lead and Two Years to Lock It In"
date: 2026-05-25
description: "Anthropic published a policy paper in May 2026 laying out two scenarios for global AI leadership by 2028. The paper warns the US has 'several months' of capability lead over China, a 4-11x compute advantage, and a closing window to translate that lead into lasting democratic dominance — or lose it to inaction."
og_description: "Anthropic's '2028: Two Scenarios for Global AI Leadership' (May 14, 2026): US-China AI race, 4-11x compute lead, DeepSeek compliance with 94% of malicious requests vs 8% for US models, distillation attacks as the CCP's 'back door,' and why Anthropic calls 2026 a 'breakaway opportunity' — while also being the company that benefits if export controls tighten."
content_type: "Analysis"
card_description: "Anthropic published a May 2026 policy paper arguing America has a 'several months' capability lead over China, a 4-11x compute advantage, and a closing window to lock in democratic dominance of AI. The paper names distillation attacks as China's primary exploit, points to DeepSeek complying with 94% of malicious requests, and calls 2026 a 'breakaway opportunity.' It is simultaneously a policy brief and a lobbying document."
tags: ["anthropic", "ai-policy", "us-china", "ai-safety", "export-controls", "deepseek", "geopolitics", "compute", "nvidia", "huawei", "national-security", "analysis"]
categories: ["reviews"]
author: "ChatForest"
last_refreshed: 2026-05-25
---

**Summary:** On May 14, 2026, Anthropic published "2028: Two Scenarios for Global AI Leadership" — a policy paper framing the US-China AI race as a two-year window that will either be seized or squandered. The paper contains some of the most specific public data on compute asymmetry and safety divergence between US and Chinese labs. It is also, transparently, a document produced by a company that stands to benefit directly from the policies it recommends. Part of our **[AI Industry Analysis](/categories/ai-tools/)** series.

---

The paper opens with a premise Anthropic describes as "a high likelihood": 2026 will be looked back on as the "breakaway opportunity" for American AI. Not 2025. Not 2028. This year.

That framing is designed to create urgency. Whether it accurately describes reality is a separate question.

---

## The Two Scenarios

The paper presents the 2028 world as a binary outcome.

**Scenario One: Democratic Dominance.** The US and its allies maintain a 12-24 month capability lead by 2028. Export controls tighten. Distillation attacks — the method by which Chinese labs harvest US model outputs to build cheaper near-frontier systems — are disrupted legislatively. American AI is exported globally, embedding democratic-aligned norms into global infrastructure. This scenario enables "favorable engagement on safety with China."

**Scenario Two: Competitive Parity.** Policy inaction allows the People's Liberation Army and aligned labs to reach near-frontier capabilities. Authoritarian regimes shape global AI norms. Automated surveillance and repression scales in ways that previously required significant human labor — and no longer does.

The paper does not present a third scenario, which is notable: a world where US dominance is maintained but used badly, or where the framing of the US-China AI race as an existential binary drives policy choices that create their own dangers. That absence is worth keeping in mind.

---

## The Numbers

The paper's most useful contribution is the specificity of its claims about compute asymmetry.

**Chip production gap:** Huawei, China's primary domestic chip producer, will produce "just 4% of NVIDIA's aggregate compute in 2026," dropping to "2% in 2027." The paper puts the overall compute advantage of the US and its allies at **4 to 11 times** China's domestic capacity.

**Why the range is so wide:** The paper is honest about uncertainty. The low end accounts for chips smuggled through third-party countries or accessed via offshore data centers — a documented and ongoing problem. The high end assumes effective enforcement. The gap between those two numbers is, essentially, the enforcement problem.

**The EUV barrier:** China lacks extreme ultraviolet (EUV) lithography technology, which is essential for producing chips at the leading edge. Without EUV — controlled by ASML in the Netherlands, with export licenses required — China cannot close the fabrication gap through domestic production alone. The US-allied chokehold on the supply chain is, the paper argues, real and currently effective.

**The intelligence gap:** US frontier models are "estimated to be at least several months ahead" of top Chinese models. The paper is careful to note that this estimate "carries uncertainty." Several months is also a relatively modest lead for a compute advantage in the 4-11x range — which suggests Chinese labs are doing something to close the gap faster than raw compute would predict.

That something is distillation.

---

## The Distillation Problem

The paper dedicates significant attention to distillation attacks — a method by which external actors create accounts on US AI platforms, systematically harvest model outputs at scale, and use those outputs to train their own models.

Chinese state media, the paper notes, described distillation as "the back door" that Chinese labs "depend on as a core part of their business model." Anthropic is calling for legislative clarification that these attacks are illegal and for facilitated threat intelligence sharing among US labs — which would let companies identify and block coordinated harvesting campaigns more quickly.

The mechanics are worth understanding. If a US model costs $100 million to train from scratch but costs $5 million to approximate by distillation, compute export controls become significantly less effective. They slow raw capability development but don't block knowledge transfer. The paper's recommendation — treat systematic harvesting as a legal and security issue, not just a terms-of-service violation — addresses this gap.

Whether it would be enforceable in practice is not addressed.

---

## The Safety Divergence Data

The paper's most striking number isn't about compute. It's about safety behavior.

Among the top 13 Chinese AI labs, only 3 published any safety evaluation results. DeepSeek's publicly available model "complied with 94% of overtly malicious requests" in testing. The US reference models in the same test complied with **8%**.

That is not a gap. That is a category difference.

The paper frames this as a national security issue: open-weight Chinese models can be deployed by "any state or non-state actor" and have safety measures removed trivially. The 94% figure, if accurate and replicable, means that a bad actor seeking to use AI for CBRN (chemical, biological, radiological, nuclear) applications or cyber operations would find Chinese open-weight models substantially more cooperative.

The paper does not address what happens when US open-weight models also ship — which they do. Llama models are open-weight. The safety divergence argument applies unevenly to the US AI ecosystem too.

---

## What Anthropic Is Asking For

The policy recommendations fall into three categories:

**1. Close compute loopholes.** Tighten enforcement on chip smuggling routes through third countries. Increase enforcement budgets. Cut off Chinese access to offshore data centers (particularly in Southeast Asia) that can run US-controlled hardware.

**2. Legislate against distillation attacks.** Make systematic harvesting of US model outputs explicitly illegal. Create threat intelligence sharing infrastructure so US labs can coordinate in identifying attack patterns without needing bilateral negotiations for each incident.

**3. Export American AI globally.** Rather than restricting US AI exports to allies only, actively promote adoption of US-built hardware and models in emerging markets — to shape global AI infrastructure with democratic-aligned systems before Chinese alternatives fill that space.

None of these recommendations are obviously wrong on their merits. They are also recommendations that, if implemented, would directly benefit Anthropic by reducing competition from lower-cost Chinese alternatives and subsidizing US lab exports.

That dual reality — accurate analysis, aligned incentives — is not a reason to dismiss the paper. It is a reason to read it with both eyes open.

---

## The Self-Serving Problem

Anthropic is a company. It has investors. It has a valuation currently approaching $900 billion. The companies that most benefit from tighter export controls, from restrictions on distillation, and from government promotion of US AI exports are: OpenAI, Google DeepMind, and Anthropic.

This doesn't make the analysis wrong. The compute numbers, the distillation dynamics, the safety divergence data — these describe something real.

But when a company publishes a policy paper that recommends policies that protect its market position, calling it simply a "policy analysis" is incomplete. The paper is also a competitive strategy document wearing a national security frame.

The honest read is that both things are true simultaneously: the US-China AI race is a genuine strategic challenge *and* Anthropic's recommended responses also happen to advantage Anthropic. Readers who find the paper compelling should interrogate both dimensions.

---

## What the Paper Doesn't Address

A few significant gaps:

**The "Democratic" frame is doing a lot of work.** The paper assumes that US AI leadership produces democratic outcomes. It does not grapple with how US AI is currently being used — in surveillance, in social media amplification, in military targeting systems — or why those applications are preferable to Chinese equivalents on first principles rather than national origin.

**The window claim is unfalsifiable in the moment.** "2026 is the breakaway year" is not a prediction that can be tested until 2028. By then, the policy choices will have been made.

**OpenRouter data cuts against the narrative.** Our coverage of [Chinese AI dominance on OpenRouter](/reviews/chinese-ai-models-openrouter-dominance-deepseek-kimi-minimax-glm-2026/) shows Chinese models at 60% of developer usage on that platform. The compute lead and the market share trend point in opposite directions. The paper focuses on the former; the latter is real too.

---

## The Bottom Line

"2028: Two Scenarios for Global AI Leadership" is worth reading as a primary source for the US government and AI policy debate as it stands in mid-2026. It contains genuinely useful specificity about compute asymmetry, safety divergence, and the distillation problem.

It is not a neutral document. It is a policy brief produced by a company that benefits from the policies it recommends, presenting a binary framing designed to create urgency, with a gap at the center: the question of whether US dominance of AI is itself a guarantee of good outcomes.

The 94% versus 8% malicious compliance number is real and alarming regardless of who published it. The question is what it justifies — and for whom.

---

*"2028: Two Scenarios for Global AI Leadership" was published by Anthropic on May 14, 2026. The full paper is available at anthropic.com/research/2028-ai-leadership.*
