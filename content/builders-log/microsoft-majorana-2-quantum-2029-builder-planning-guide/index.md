---
title: "Microsoft Majorana 2: The 2029 Quantum Deadline That Meets the 2029 Cryptography Deadline"
date: 2026-06-03
description: "Microsoft unveiled Majorana 2 at Build 2026 — a topological quantum chip 1,000x more reliable than its predecessor, designed using AI, with a 2029 target for practical quantum computing. That deadline collides with Google and Cloudflare's 2029 post-quantum cryptography migration deadline. Here's what builders should actually do now."
og_description: "Microsoft announced Majorana 2 at Build 2026: 1,000x more reliable topological qubits, 2029 target for a scalable quantum computer, designed with Microsoft Discovery agentic AI. The same year Google and Cloudflare have told builders to complete post-quantum cryptography migrations. Here's how to think about it."
content_type: "Builder Guide"
card_description: "Majorana 2, Microsoft's topological quantum chip, was unveiled at Build 2026 with a 2029 target for a practical, scalable quantum computer — the timeline cut in half. The same year Google and Cloudflare have set as their post-quantum cryptography migration deadline. Microsoft used its Discovery agentic AI to design the new materials stack: aluminum superconductor replaced with lead, semiconductor updated to InAs/InAsSb. Qubits are now 1,000x more reliable with mean 20-second lifetimes. Scientific critics say the data does not yet verify the topological qubit claims. The builder action is the same either way: start the PQC migration now."
tags: ["microsoft", "quantum-computing", "majorana", "post-quantum-cryptography", "build-2026", "azure-quantum", "microsoft-discovery", "security", "pqc", "topological-qubits"]
categories: ["builders-log"]
author: "ChatForest"
sources_audited: 2026-07-28
---

**At a glance:** [Microsoft unveiled Majorana 2 at Build 2026](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/) (June 2, 2026). Topological quantum chip with a new materials stack, 1,000x more reliable qubits, ~20-second mean qubit lifetime, and a 2029 target for a scalable practical quantum computer — half the previously stated timeline. Designed using Microsoft Discovery agentic AI. [Scientific critics say the topological qubit claims lack sufficient public data](https://www.nature.com/articles/d41586-026-01788-y). The builder-relevant collision: 2029 is also Google's and Cloudflare's deadline for post-quantum cryptography migration. NIST FIPS 203/204/205 are final. The action is the same whether Microsoft's timeline is right or not. Part of our **[Builder's Log](/builders-log/)**.

---

Two separate clocks converged at Build 2026, and the builder implication is the same regardless of which one you believe.

Microsoft said that [practical, scalable quantum computing arrives in 2029](https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor). [Google said in March 2026 that post-quantum cryptography migrations need to be complete by 2029](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/). [Cloudflare moved its own internal PQC deadline to 2029](https://blog.cloudflare.com/post-quantum-roadmap/) for the same reason. That convergence is not a coincidence — it follows a rapid run of 2025–2026 papers that kept cutting the qubit count needed to break public-key cryptography, including a [May 2025 Google paper showing RSA-2048 could fall to under a million physical qubits](https://research.google/pubs/how-to-factor-2048-bit-rsa-integers-with-less-than-a-million-noisy-qubits/) and a [March 2026 Google Quantum AI paper](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) showing that breaking the elliptic curve cryptography used in Bitcoin and Ethereum requires roughly **20 times fewer qubits** than the security community's prior best estimate.

Even if you are skeptical of Microsoft's quantum timeline — and the scientific community is — the cryptographic risk has been independently repriced. The migration is not optional anymore.

---

## What Majorana 2 Actually Is

Microsoft has spent a decade betting on topological qubits: a fundamentally different architecture than the gate-based qubits IBM and Google use. Where IBM and Google build large numbers of physically unreliable qubits and use error-correction overhead to make them behave reliably, Microsoft's approach tries to build physically reliable qubits whose protection comes from topology — a mathematical property of the quantum state rather than active correction circuits.

The bet: if topological protection works, you can build far fewer physical qubits to achieve the same logical qubit fidelity. The counter-argument: topological qubits are extraordinarily hard to make and Microsoft has struggled to prove they actually exist in its devices.

Majorana 2 is the second generation of that approach. The key changes:

| Property | Majorana 1 | Majorana 2 |
|---|---|---|
| Superconductor | Aluminum | Lead |
| Semiconductor | Indium arsenide (InAs) | InAs + indium arsenide antimonide (InAsSb) |
| Qubit reliability | Baseline | 1,000x improvement |
| Mean qubit lifetime | 1–12 milliseconds | ~20 seconds |
| Max observed lifetime | — | Up to 1 minute |
| Gate operation speed | — | 1 microsecond |
| Qubit footprint | — | 1/100th of a millimeter |

[Specs per Microsoft's own technical blog post on Majorana 2](https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor). The material changes create a more stable topological phase. The lead superconductor and the InAs/InAsSb semiconductor combination produce qubit states that are better isolated from their environment — which is the fundamental engineering challenge in quantum computing.

---

## The AI-Designed Materials Angle

The underlying materials shift — aluminum to lead, and adding indium arsenide antimonide to the semiconductor — is research that [predates Microsoft's agentic AI platform as a concept](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/), by Microsoft's own account. What agentic AI contributed was the fabrication and analysis loop around that materials work: Microsoft says its team [used **Microsoft Discovery**](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/) — its agentic AI platform for scientific R&D, [which reached general availability the same week at Build 2026](https://azure.microsoft.com/en-us/blog/announcing-microsoft-discovery-general-availability-and-microsoft-discovery-app-preview/) — to [manage fabrication workflows, automate measurements, run materials simulations, and correlate patterns across roughly two decades of experimental data](https://www.infoq.com/news/2026/06/microsoft-discovery-majorana-2/) to catch manufacturing flaws and refine the stack faster than manual analysis allowed.

That is a real, documented role for agentic AI in the fabrication and optimization loop — not the origin of the underlying materials design, which Microsoft says came first. Discovery is also slated for more extensive use in Microsoft's next round of Majorana materials research.

Microsoft frames the AI-accelerated fabrication and analysis work as part of why the [2029 target represents cutting its quantum roadmap "in half"](https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor) compared to its earlier projections.

---

## What the Scientific Community Is Saying

This deserves straightforward treatment: the scientific community has not validated Microsoft's topological qubit claims.

When Majorana 1 was announced in 2025, [physicists said the published data was insufficient to confirm the existence of topological qubits](https://www.nature.com/articles/d41586-025-00829-2). Separately, *Science* [issued a formal Expression of Concern](https://retractionwatch.com/2021/07/29/science-majorana-paper-earns-an-expression-of-concern) about tunneling-spectroscopy data in a 2020 quantum study co-authored by Microsoft Quantum and the Niels Bohr Institute, after outside researchers flagged non-representative data selection. With Majorana 2, [University of St Andrews physicist Henry Legg made the same core objection to *Science News*](https://www.sciencenews.org/article/microsoft-quantum-chip-upgrade-majorana): *"Nothing in the presented data proves the existence of a topological qubit or Majoranas in these devices."*

Microsoft's position is that the 1,000x reliability improvement and the faster, smaller qubits are measurable and real, and that the topological protection is the most plausible explanation. The critics' position is that alternative explanations have not been ruled out.

The honest read for builders: treat 2029 as the optimistic case, 2031–2033 as the base case, and plan cryptographic migrations accordingly. The exact date does not change the direction of travel.

---

## The 2029 Collision

Three separate organizations have landed on the same year:

| Organization | 2029 claim |
|---|---|
| Microsoft | Scalable, practical quantum computer operational |
| Google | Post-quantum cryptography migration must be complete |
| Cloudflare | Post-quantum cryptography migration must be complete |

[Google accelerated its migration deadline in March 2026](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) and [Cloudflare followed in April 2026](https://blog.cloudflare.com/post-quantum-roadmap/), after a rapid string of 2025–2026 papers repeatedly cut the qubit count required to break elliptic curve cryptography — most recently [Google Quantum AI's March 2026 estimate](https://research.google/blog/safeguarding-cryptocurrency-by-disclosing-quantum-vulnerabilities-responsibly/) of roughly 20x fewer qubits than the prior best estimate. That means a cryptographically relevant quantum computer (CRQC) — one capable of breaking RSA and ECC in real-world time — could arrive materially sooner than the security community had planned for.

NIST has already [finalized the replacement standards](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards):

- **FIPS 203 (ML-KEM)** — lattice-based key encapsulation (replaces RSA/ECC for key exchange)
- **FIPS 204 (ML-DSA)** — lattice-based digital signatures (replaces ECDSA)
- **FIPS 205 (SLH-DSA)** — hash-based digital signatures (stateless, conservative fallback)

These are final standards, not drafts, as of August 2024. Implementation libraries exist for most major languages. The cryptographic migration tooling is available now.

---

## What Builders Should Actually Do

**1. Start the cryptographic inventory.**
Map where classical public-key cryptography lives in your stack: TLS certificates, JWT signing keys, RSA-encrypted blobs at rest, ECDH session negotiation, API authentication signatures. Most builders discover this takes much longer than expected — dependencies are often transitive (a library using another library using RSA).

**2. Authentication before encryption.**
[Cloudflare's guidance](https://blog.cloudflare.com/ml-dsa-will-have-to-do/) flips the migration priority that was conventional wisdom: authentication (signatures) should be migrated before encryption (key exchange). The reasoning: encrypted traffic captured today can be decrypted later when quantum hardware arrives ([harvest-now/decrypt-later](https://blog.cloudflare.com/pq-2025/)), but a forged signature on a root certificate or code-signing key creates active, immediate risk.

**3. Do not wait for quantum hardware.**
The migration deadline is about quantum risk, but PQC libraries implement FIPS 203/204/205 today on classical hardware: [liboqs](https://openquantumsafe.org/) (C, with Python/Go/Rust/Java bindings), [BouncyCastle](https://www.bouncycastle.org/) (Java/.NET), and [AWS-LC](https://github.com/aws/aws-lc/blob/main/crypto/fipsmodule/PQREADME.md) (AWS's libcrypto). You can deploy ML-KEM for TLS key exchange now using TLS 1.3 hybrid mode (classical + post-quantum in parallel), which maintains compatibility with non-PQC clients while adding quantum resistance for clients that support it.

**4. Watch Azure Quantum, but don't block on it.**
Microsoft's Azure Quantum platform today [provides access to Quantinuum, IonQ, Rigetti, and other hardware providers](https://learn.microsoft.com/en-us/azure/quantum/provider-global-availability). Majorana-based topological qubits are not yet on the platform; Microsoft's own materials indicate the [processors are still headed toward Azure Quantum integration, not yet generally available there](https://quantum.microsoft.com/en-us/insights/blogs/majorana-2-scalable-quantum-processor). If you want to experiment with quantum algorithms for optimization or simulation use cases, the platform is accessible now with existing hardware. If you are waiting for topological qubits specifically, 2029 is the earliest optimistic date.

**5. Understand what quantum is actually useful for.**
Quantum supremacy in the sense of "faster at everything" does not exist and will not exist in 2029. The meaningful near-term quantum advantage is expected in: combinatorial optimization (routing, scheduling, logistics), quantum chemistry simulation (drug discovery, materials design), and a subset of machine learning problems involving linear algebra. General-purpose compute faster than a GPU is not on the 2029 roadmap.

---

## The Broader Build 2026 Context

Majorana 2 was not the centerpiece of Build 2026 — that was agentic AI on Windows, GitHub Copilot, and the MAI model family. Quantum computing sat at the end of the keynote as a longer-horizon bet.

But the pairing of Microsoft Discovery AI accelerating quantum hardware fabrication and analysis is not incidental. It is a demonstration of what Microsoft is positioning Discovery to do: accelerate hard scientific R&D workflows by deploying agent teams against them. Majorana 2's fabrication and materials-optimization work is the proof of concept. The implication is that the same pattern — AI agents compressing lab workflows that used to take years into a much shorter cycle — is now available to enterprise R&D teams on Azure.

That is the short-term actionable story inside the quantum announcement: [Microsoft Discovery is GA, not research preview](https://azure.microsoft.com/en-us/blog/announcing-microsoft-discovery-general-availability-and-microsoft-discovery-app-preview/). If you are in pharma, materials science, or any domain where materials design or molecular simulation is a bottleneck, the platform that helped accelerate Majorana 2's fabrication is available today.

---

## Related Coverage

- **[Windows AI Models: Aion 1.0](/builders-log/microsoft-build-2026-windows-ai-models-aion-local-inference-builder-guide/)** — On-device AI at Build 2026, including the Windows Local AI Runtime KB5039239 shipping June 9.
- **[MAI Multimodal Stack](/builders-log/microsoft-mai-multimodal-build-2026-image-voice-transcribe-builder-guide/)** — MAI-Image-2.5, MAI-Voice-2, and MAI-Transcribe-1.5 from the same Build 2026 week.
- **[MAI-Code-1-Flash](/builders-log/microsoft-mai-code-1-flash-github-copilot-coding-model-build-2026/)** — Microsoft's Copilot-native coding model, also launched at Build 2026.
- **[Microsoft Build 2026 Recap](/builders-log/microsoft-build-2026-recap-windows-agent-platform-project-polaris-copilot-workspace/)** — Day 1 overview: Project Polaris, Windows Agent Platform, Copilot Workspace.

*Sources: [Microsoft on Majorana 2 and Discovery AI](https://news.microsoft.com/source/features/innovation/majorana-2-microsoft-discovery-agentic-ai/); [TechTimes on Majorana 2 specs](https://www.techtimes.com/articles/317648/20260602/majorana-2-quantum-chip-revealed-microsoft-build-2026-features-specs-explained.htm); [Nature on scientific skepticism](https://www.nature.com/articles/d41586-026-01788-y); [Post Quantum analysis](https://postquantum.com/industry-news/microsoft-majorana-2-analysis/).*
