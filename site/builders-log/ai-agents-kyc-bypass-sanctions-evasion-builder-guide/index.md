# Your KYC Stack Isn't Ready for AI Agents: The RUSI Sanctions Evasion Report

> A UK defense think tank just documented how AI agents handle end-to-end sanctions evasion — document forgery, deepfake biometrics, agentic shell company management. Here's what breaks in your KYC pipeline and what to do about it.


A UK defense think tank published a report in late May 2026 that deserves more attention from the builder community than it's getting. RUSI (Royal United Services Institute) released **"Algorithms of Evasion: The Rise of AI-Enabled Proliferation Financing"**, and its core message is not diplomatic: AI agents have already advanced far enough to handle sanctions evasion at a scale that overwhelms current detection and enforcement capabilities.

The Register covered it on May 26 under the headline "Rogue states are putting AI agents to work on sanctions evasion." Computerworld ran it as "Another IT governance headache." Both framings undersell the implications for builders specifically.

If you are building anything involving identity verification, onboarding, compliance, or financial services — or if you run cloud infrastructure that third parties could use to run AI pipelines at scale — this report is about systems your code sits inside.

---

## What the RUSI Report Actually Says

Lead author Dr. Aaron Arnold focuses on proliferation financing: the use of funds or financial services to acquire weapons of mass destruction. Named actors in the report are North Korea, Iran, and Russia.

But the technical findings are not specific to state actors. The attack classes described — synthetic identity generation, deepfake biometric bypass, agentic shell company management, AI-powered crypto routing — are available to anyone with access to consumer-grade tools and a Telegram account.

The report's central claim: AI has the potential to radically increase the scale of proliferation financing "to levels that overwhelm current detection and enforcement capabilities." The specific mechanism: automation. What once required teams of human operators to maintain shell companies, forge documents, and manage cross-border crypto flows can now be handled by AI agents working autonomously across discrete subtasks.

---

## Three Attack Layers — and Where They Hit Your Stack

### Layer 1: Document Forgery

Generative AI can now produce convincing fake passports, driver's licenses (from 26+ countries), bank statements, vessel registrations, invoices, and corporate records. The canonical case is OnlyFake — a neural-network-based platform that generated 10,000+ fake IDs at $15 each. Operator Yurii Nazarenko (a.k.a. "John Wick") has since pleaded guilty. But what his platform demonstrated matters more than his prosecution: fake British passports from OnlyFake successfully bypassed KYC at OKX, Kraken, Bybit, Bitget, Huobi, and PayPal before anyone caught them.

Sumsub's 2025 Identity Fraud Report found that 2% of all detected fraudulent documents were created with generative AI tools (ChatGPT, Grok, Gemini) in a six-month window. "Detected" is the key word. The undetected share is unknown by definition.

**What this breaks in your stack:** Any document verification pipeline relying primarily on image analysis — OCR, template matching, or AI classifiers trained on pre-2024 forgery patterns. The gap between "looks authentic" and "is authentic" is now a $15 transaction.

### Layer 2: Biometric Bypass

Static liveness checks are gone as a reliable control. The tools to defeat them are commodity:

- **Virtual Camera (VCam) software** injects pre-recorded or AI-generated video into a phone's camera API, defeating "move your head" and "blink" liveness prompts. iProov logged a 2,665% spike in native virtual camera attacks over the past year. These tools sell for $30–$60 on Telegram.
- **Hooking framework exploits** for rooted Android devices intercept the camera API inside banking apps, bypassing liveness checks at the framework level.
- **Face-swap tools** have proliferated. The World Economic Forum's January 2026 Cybercrime Atlas tested 17 face-swapping tools and 8 camera injection tools and found most could bypass standard biometric onboarding checks.

Deepfakes now account for 11% of all global fraudulent activity in 2026, up from 7% in 2024. Synthetic-identity fraud is growing 31% year-on-year and generates an estimated $20–40 billion in annual losses.

In April 2026, Flashpoint counted 63,763 Telegram posts advertising or discussing KYC bypass methods in a single month.

**What this breaks in your stack:** "Record your face" or "take a selfie with your ID" as your primary identity assurance mechanism. If your liveness check is prompt-based (turn your head, blink), VCam tools defeat it reliably. This is not an edge case — it is a commodity attack.

### Layer 3: Agentic Operations

This is the layer the RUSI report introduces that has no clean precedent. Beyond document forgery and biometric bypass, AI agents can now handle:

- **Shell company lifecycle management**: automating entity creation, registration renewals, shareholder structure maintenance, and banking relationship management across jurisdictions.
- **Crypto routing**: real-time analysis of blockchain transaction patterns, dynamic routing through mixers and DeFi platforms to evade pattern-matching in compliance systems.
- **Synthetic persona consistency**: generating coherent fake identities that remain consistent across multiple platforms, customer support interactions, and document requirements over time.
- **Remote hiring bypass**: North Korea's IT worker programs use AI-generated CVs and deepfake video calls to pass remote hiring screens at Western tech companies, generating revenue that funds weapons programs. This is active, not theoretical.

**What this breaks in your stack:** Behavioral fraud detection models trained on the assumption that they're observing human users. An agentic attacker removes the human behavioral signal entirely. If your anomaly detection depends on typing cadence, navigation patterns, or session timing, an agent-operated onboarding flow will look different — but not in the ways your models were trained to flag.

---

## The Numbers Behind the Threat Level

| Metric | Value | Source |
|--------|-------|--------|
| VCam attack spike, past year | 2,665% | iProov |
| Telegram KYC bypass posts, April 2026 | 63,763 | Flashpoint |
| VCam bypass tool cost | $30–$60 | Tech-Insider |
| Synthetic identity fraud growth YoY | 31% | Sumsub |
| Global synthetic ID losses per year | $20–40 billion | Multiple |
| Deepfake share of global fraud, 2026 | 11% (up from 7% in 2024) | FinTech Global |
| Sanctioned entity crypto volume, 2025 | $104 billion | Chainalysis |
| North Korea crypto theft, 2025 | $2 billion+ | CoinDesk |
| OnlyFake fake IDs generated | 10,000+ at $15 each | OECD.AI |
| AI scam profitability vs. traditional | 4.5× more profitable, 253% higher avg. payout | Chainalysis |

The A7A5 stablecoin is the starkest single example of what agentic infrastructure can accomplish at scale: a purpose-built sanctions-evasion settlement rail that processed over $93 billion in under a year before being flagged by Chainalysis.

---

## What Actually Works in 2026

Given the attack surface, here is the current state of defenses that hold:

**NFC chip reading from physical ID documents** catches approximately 62% of synthetic-identity attempts at the document verification step. The cryptographic signing on a physical passport chip cannot be reproduced by a generative model — you need the physical document. This is the single highest-leverage control at the document layer.

**Passive depth analysis and micro-movement scoring** in biometric checks are harder to defeat than prompt-based liveness. These analyze physiological signals across video frames rather than asking the user to perform an action that a VCam loop can simulate.

**Verifiable Credentials with cryptographic proof**: Indicio launched "Proven AI for KYC" in March 2026, allowing banks to verify identity via digital wallets holding credentials signed by issuing authorities — eliminating reliance on document images and perception-based biometrics entirely. The EU Digital Identity framework mandates similar wallet-based verification. This is where the field is heading; the attack surface for a cryptographic credential is fundamentally different from the attack surface for a JPEG of a passport.

**Device fingerprinting and emulator detection**: identifying fraud hardware (rooted devices, emulators, VMs) catches a meaningful share of attacks before biometric checks are even reached.

**Behavioral risk scoring across the full session**: time-to-completion, interaction patterns, re-entry rates, and cross-session consistency. Note the caveat above about agentic attackers — this layer is becoming less reliable as attackers become less human. But it still catches low-sophistication attacks in volume.

**Lifecycle monitoring, not just onboarding**: a synthetic identity that passes onboarding may sit dormant for months. Account behavior after activation — transaction patterns, device changes, network fingerprints — needs continuous scoring, not just a one-time gate at registration.

---

## Compute-KYC: What It Means for Cloud and API Providers

The RUSI report proposes "compute-KYC" as a new obligation: cloud infrastructure providers should be required to know who is renting GPU compute at scale, because running document forgery pipelines, deepfake generation systems, or agentic shell-company management requires substantial compute infrastructure.

This is less hypothetical than it sounds. The U.S. Department of Commerce's Bureau of Industry and Security (BIS) already proposed an IaaS Customer Identification Program rule that requires U.S. infrastructure-as-a-service providers to build written CIPs — the cloud equivalent of what banks operate under the Bank Secrecy Act. Requirements include collecting customer names, addresses, payment information, email addresses, phone numbers, IP addresses, and conducting diligence on foreign beneficial owners. The January 2026 BIS final rule on AI chip exports to China includes KYC and remote access controls as conditions for case-by-case licensing.

The open question — and the one builders should watch — is scope creep to LLM API platforms. Analysis of the BIS IaaS rule's wording suggests that LLM gateways and API platforms may fall within its definition of IaaS, not just raw GPU rental providers. If you run an API that provides model access to third parties at scale, you may be looking at CIP obligations within the rule's implementation window.

---

## Eight Builder Actions

1. **Add NFC chip reading to your document verification pipeline.** It is not optional for any high-assurance onboarding context. Image-based document verification alone is no longer defensible.

2. **Audit your liveness check vendor's posture on VCam attacks.** Ask explicitly: does your solution detect virtual camera injection? What is your false-negative rate on VCam tools? If the answer is vague, assume the worst.

3. **Move toward Verifiable Credentials when you have the choice.** If your identity verification flow gives you any architectural flexibility, start evaluating wallet-based credential verification. EU Digital Identity requirements make this the medium-term standard; adoption now reduces technical debt later.

4. **Rethink behavioral models as "human presence" assumptions go away.** If your fraud models were trained on human session data, they need adversarial retraining against agentic input patterns — sessions where interaction is precise, fast, and consistent in ways human behavior is not.

5. **Don't rely on onboarding as a single control point.** Build lifecycle monitoring. A synthetic identity that passes your gate can sit and wait.

6. **Check whether BIS IaaS rule scope applies to your platform.** If you provide model access via API to third parties, get a legal read on whether you are in scope for Customer Identification Program requirements. Better to know now.

7. **Log your KYC decisions with enough audit trail to reconstruct them.** Regulators are watching this space. You want to be able to demonstrate that your controls were reasonable at the time of any incident.

8. **Treat your compliance controls as an attack surface, not a checkbox.** The RUSI report's bottom line is that compliance systems built for human-speed, document-based evasion are now facing machine-speed, document-generating, biometric-spoofing, agentic-pipeline attacks. The gap between those two is the current opportunity for bad actors.

---

## The Structural Read

The RUSI report's most important implication is not about North Korea or Iran specifically. It is that the automation advantage in fraud has crossed a threshold. What required an organized criminal network with specialized human operators now requires a Telegram subscription and an API key.

Builders deploying anything adjacent to financial services, identity verification, or compliance have always lived with fraud risk. What changed is the cost structure: attacks that were expensive enough to deter except for high-value targets are now cheap enough to run at volume against ordinary onboarding flows.

Fighting automation with automation — as RUSI explicitly recommends — is not a nice-to-have. It is the only architecture that matches the threat's cost curve.

---

*Research for this article draws on the RUSI "Algorithms of Evasion" report, The Register's May 26 coverage, Chainalysis 2026 Crypto Crime Report, iProov 2025 Biometric Threat Intelligence Report, WEF Cybercrime Atlas (January 2026), Sumsub 2025 Identity Fraud Report, and Flashpoint/Biometric Update research on Telegram KYC bypass tool markets.*

