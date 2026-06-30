# GLM-5.2 Beats Claude Code on Vulnerability Detection: What the Export Control Rationale Gets Wrong

> Semgrep's June 22 benchmark found open-weight GLM-5.2 outperforming Claude Code on IDOR detection at $0.17 per finding. Graphistry's CyBT-CTF placed it at Opus 4.8 parity. This is the first empirical test of whether US export controls on Fable 5 and Mythos 5 can actually contain the capability they targeted — and the early answer is no.


On June 12, 2026, the US government enacted an emergency export control barring any foreign national from accessing Anthropic's Fable 5 and Mythos 5. The stated rationale: these models had demonstrated advanced cybersecurity capabilities — specifically, a red-team test in which Mythos penetrated NSA classified systems in hours. Restricting access was framed as containing a dangerous capability.

Ten days later, Semgrep published a benchmark. Open-weight GLM-5.2, released by Zhipu AI on June 13 with an MIT license and no regional access restrictions, **outperformed Claude Code on IDOR vulnerability detection**: 39% F1 versus 37% (Opus 4.6) and 28% (Opus 4.8/4.7). Graphistry's CyBT-CTF placed GLM-5.2 at parity with Opus 4.8 on agentic cybersecurity investigation tasks.

This is the first empirical data point on whether the Fable 5/Mythos 5 export controls can actually contain the capability they targeted. The early data suggests they cannot — not because the controls were wrong in principle, but because the capability they tried to lock down is now reproducible with freely downloadable open weights.

---

## What the Benchmarks Actually Measured

**Semgrep — IDOR Detection (published June 22, 2026)**

Semgrep's security research team tested models on a real vulnerability detection task: finding IDOR (Insecure Direct Object Reference) flaws in open-source applications they had previously used for vulnerability research. IDOR bugs are high-value targets — they allow one user to access another's data by manipulating object identifiers in API requests.

| Model | F1 Score | Notes |
|---|---|---|
| Semgrep pipeline (multimodal) | 53–61% | Custom harness, not a raw model result |
| GLM-5.2 | 39% | MIT license, open weights |
| Claude Code (Opus 4.6) | 37% | US model, API access |
| Claude Code (Opus 4.8/4.7) | 28% | US model, API access |

Cost for GLM-5.2: **$0.17 per vulnerability found** via the Z.ai Coding Plan.

The test used a minimal scaffolding harness (Pydantic AI framework) for both open-weight models and Claude Code — matching the harness as closely as possible to isolate model capability. Caveats: this is one task, one dataset, one run. Semgrep's own team does not present it as a comprehensive model evaluation.

**Graphistry — CyBT-CTF**

Graphistry's CyBT-CTF (Cyber Threat CTF) benchmark evaluates agentic cybersecurity investigation performance: models are given incomplete incident data and must autonomously identify threat actors, attack paths, and root causes across multi-step scenarios. GLM-5.2 matched Opus 4.8 on solve rate, placing it in what Graphistry characterized as "frontier-like" territory for open-weight models.

This benchmark is closer in spirit to the Mythos NSA red-team framing — it measures autonomous, multi-step security reasoning, not just pattern matching.

---

## The Export Control Argument and What These Numbers Mean

The US government's position on the Fable 5/Mythos 5 suspension rests on a specific claim: that these models have cybersecurity capabilities qualitatively beyond what was previously accessible, and that restricting foreign access limits a dangerous capability.

The GLM-5.2 benchmarks challenge the "limit a dangerous capability" half of that claim.

What the benchmarks show: **the specific task profile that justified the ban — autonomous cybersecurity vulnerability detection and investigation — is now replicable with a freely downloadable open-weight model**. Not at full Mythos 5 capability across all dimensions, but on the narrow measurable tasks that correlate most directly with the stated concern.

What the benchmarks do not show: whether GLM-5.2 matches the autonomous intrusion behaviors described in the NSA red-team test. The Mythos incident involved full system penetration — multi-stage lateral movement, credential compromise, access to classified infrastructure — in a controlled red-team environment. IDOR detection and CTF solve rates are leading indicators, not proof of equivalent offensive capability. That distinction matters.

---

## The MIT License Problem for Containment Policy

GLM-5.2 is distributed under the MIT license. Anyone on Earth can:
- Download the weights from Hugging Face (`zai-org` organization)
- Run them on their own hardware
- Modify and redistribute them
- Use them in production without API access restrictions

Fable 5 and Mythos 5 are closed-weight, API-only models. The export controls work at the API authentication layer — restricting API keys issued to foreign nationals. That control surface does not exist for open-weight models.

On June 25, Axios reported that Russian hacker forums were already discussing GLM-5.2 jailbreak techniques and testing the model on offensive security tasks. This is three days after Semgrep's benchmark was published. Whatever capability GLM-5.2 has, the operational adversaries the export controls were designed to contain appear to have access to it.

---

## What This Means for Builders

**1. The harness is what actually matters for security tasks**

The most important number in the Semgrep benchmark is not GLM-5.2's 39% or Claude Code's 37%. It is the gap between those numbers and Semgrep's own pipeline at 53–61%. Semgrep's pipeline achieves that lead not by using a more powerful model, but by using a purpose-built harness: endpoint enumeration, structured output parsing, and domain-specific scaffolding that directs the model toward what it needs to find.

If you are building AI-assisted security tooling, the architecture of your harness will have more impact on performance than your model choice. A well-scaffolded GLM-5.2 pipeline can outperform a naive Claude Code integration.

**2. Open-weight models are now a viable contingency for security use cases**

Before June 12, builders building security-adjacent products had a clear choice: use Fable 5/Mythos 5 for frontier capability, or settle for less. After June 12, that choice was removed for anyone who lost access. GLM-5.2 benchmarks suggest that open-weight alternatives are now competitive on the specific vulnerability detection tasks where Fable 5/Mythos 5 were most valuable.

If your security pipeline lost access to Anthropic models via the export control disruption, GLM-5.2 is the first open-weight option with credible benchmark data on the relevant tasks. You will need self-hosting infrastructure (the model is a 744B MoE; you need significant compute), but the MIT license removes API reliability risk.

**3. API access is a policy variable now, not a technical one**

The Fable 5/Mythos 5 suspension showed that US government action can remove frontier model API access in hours. The GLM-5.2 data shows that the capability logic motivating those controls is now outpacing the controls themselves.

This is a signal for architecture decisions: **API access to frontier models should not be a single point of failure in any security-critical pipeline**. Whether through open-weight fallbacks, multi-provider failover, or local inference capabilities, the last six weeks have empirically demonstrated that government policy decisions will affect your API access, and they will not give you much notice.

**4. Expect policy escalation, not policy retreat**

The most likely response to "export controls failed to contain the capability" is not "so let Fable 5 return." It is escalation to the hardware layer — restrictions on Nvidia chip exports, tighter controls on the data center compute required to train and run models like GLM-5.2, or secondary sanctions on jurisdictions running the inference infrastructure.

The Great American AI Act (currently a discussion draft) includes federal preemption provisions that could preempt state AI laws but does not address open-weight model policy. The White House June 2 executive order directed agencies to build a pre-release review framework for "covered frontier models" — closed-weight, API-distributed models. Open-weight models sit outside that framework entirely.

The regulatory gap between closed API models and open-weight models is where the next policy move is most likely to land.

---

## What to Watch

- **Fable 5 restoration timeline**: The cybersecurity benchmark data does not directly accelerate Fable 5 restoration — the government's concern was about specific advanced capabilities, not the commodity task range GLM-5.2 was tested on. But it changes the political calculus: the "containment" argument is harder to make if the capability is already freely available. Watch for Anthropic and the White House to respond to this specifically.

- **NIST AI Safety Institute open-weight model working group**: Since March 2026, NIST has been developing guidance on how to apply AI safety frameworks to open-weight models. The GLM-5.2 benchmark data is likely to become a reference point in those discussions.

- **Semgrep second run**: Semgrep noted their result was "one task, one dataset, one run." A broader replication across vulnerability classes would either confirm or narrow the result. Watch for follow-up benchmarks.

- **GLM-5.2 commercial API stability**: Z.ai's Coding Plan pricing ($1.40/$4.40 per 1M tokens, or flat $10/quarter Lite tier) is currently very competitive. As international demand for GLM-5.2 grows (partly driven by the Fable 5 gap), pricing may change. If self-hosting is your contingency plan, start evaluating hardware requirements now rather than after pricing adjusts.

---

The export controls on Fable 5 and Mythos 5 were enacted on an emergency basis with significant disruption to the API ecosystem. Seventeen days later, the first independent cybersecurity benchmarks show an open-weight alternative matching or exceeding the relevant metric on the task class that justified the ban. That does not make the ban wrong — the NSA incident involved capabilities not measured in these benchmarks. But it does mean the containment logic has a shelf life measured in weeks, not months, and that builders who built API-access dependencies on frontier models need a different risk model going forward.

---

*The Semgrep benchmark was published June 22, 2026. Graphistry's CyBT-CTF results were published in the same window. GLM-5.2 open weights are available at HuggingFace under the `zai-org` organization. The June 25 Axios report on adversarial forum exploitation was published before this article.*

