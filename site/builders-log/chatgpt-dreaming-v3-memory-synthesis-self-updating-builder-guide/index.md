# ChatGPT Dreaming V3: Self-Updating Memory and What It Means for Builders

> OpenAI shipped Dreaming V3 on June 4, 2026 — a background synthesis process that replaces the saved-memories list and auto-corrects itself over time. Factual recall jumped from 41.5% to 82.8% on OpenAI's internal evals. Enterprise users get a new memory_context API parameter. But the same system that removes repetitive context-setting creates audit liability for accuracy-sensitive workflows.


On June 4, 2026, OpenAI began rolling out Dreaming V3 to ChatGPT Plus and Pro users in the US. For regular users, it means ChatGPT remembers more and asks less. For builders, it introduces a new API parameter, a different mental model of what "memory" means in a production context, and a set of compliance questions that weren't present with the older saved-memories architecture.

**At a glance:** Dreaming V3 is a background process that reads across a user's full conversation history, synthesizes a persistent memory profile, and automatically revises that profile as circumstances change — without user prompting. Enterprise and API customers gain access via a new `memory_context` parameter. The same auto-update capability that makes the system more accurate also means platform-revised records replace user-authored ones, raising audit trail concerns for regulated or accuracy-sensitive workflows. Part of our **[Builder's Log](/builders-log/)**.

---

## The Architecture History: Three Distinct Systems

OpenAI has shipped three fundamentally different memory systems since April 2024, and the differences matter for builders:

**Saved Memories (April 2024):** Manual, list-based. Users or the model explicitly saved facts. Entries never updated themselves. Scope was strictly conversation-by-conversation. OpenAI later described this as a starting point, not a durable approach.

**Dreaming V0 (April 2025):** Added a supplemental synthesis layer that could reference context beyond the saved list. Still treated as an overlay on top of saved memories. OpenAI's own documentation acknowledged it was "never sufficient as a standalone memory system" — it was an augmentation, not a replacement.

**Dreaming V3 (June 4, 2026):** Replaces the saved-memories list entirely as ChatGPT's memory foundation. No explicit save actions needed. The background synthesis process reads across years of conversations, identifies facts, preferences, and context, and writes a continuously-updated profile. Individual entries revise themselves over time.

The architectural shift from V0 to V3 is not incremental. V3 makes the synthesis process primary and authoritative, rather than supplemental.

---

## How the Self-Updating Memory Works

The canonical example from OpenAI's announcement: a memory that reads "the user is going to Singapore in July" revises itself to "the user went to Singapore in July 2026" after the trip ends. No user action, no explicit update prompt — the synthesis process infers the temporal state change and rewrites the record.

This covers three distinct memory categories:

**Factual facts about the user:** Camera gear setups, dietary restrictions, professional role, location, long-running project states. Previously these required manual "remember that I use..." prompts.

**Explicit instructions:** "Don't bring up Stan again." "Always respond in Spanish." Preferences that a user stated directly in a past conversation but shouldn't have to repeat.

**Implicit preferences:** Patterns that emerged over time without explicit instruction — tone preferences, topic areas the user engages with or avoids, workflow habits.

The synthesis runs in the background between conversations, not within them. The active conversation itself does not trigger the rewrite; the background job does.

---

## Performance Metrics (Vendor-Stated, Independent Verification Absent)

OpenAI published internal eval scores across the three memory generations on three metrics:

| System | Factual Recall | Preference Adherence | Time-Sensitive Accuracy |
|--------|---------------|---------------------|------------------------|
| 2024 (Saved Memories) | 41.5% | — | — |
| 2025 (Dreaming V0) | 67.9% | — | — |
| 2026 (Dreaming V3) | **82.8%** | ~71.3% | ~75.1% |

Critical caveat: these are internal OpenAI evaluations on OpenAI-defined benchmarks. The methodology is not published and there has been no independent third-party replication as of June 6, 2026. The directional improvement is plausible given the architectural shift, but the specific numbers should be treated as vendor claims, not verified performance data.

The compute efficiency gain is separately significant: OpenAI reports approximately a 5x reduction in the compute required to serve the dreaming system. That is what makes Free-tier expansion practical — the economics of running Dreaming V0 were not compatible with free users at scale.

---

## Privacy Tiers and Default Settings

The memory defaults differ significantly across account types:

| Tier | Memory Default | Used for Training | Storage |
|------|---------------|-------------------|---------|
| Free / Plus / Pro | **On** | Opt-out available | Standard |
| Team | **On** | Excluded by default | In-transit & at-rest encryption |
| Enterprise / Edu | **Off** | Excluded by default | In-transit & at-rest encryption |

Enterprise and Education accounts default to memory-off, which is consistent with OpenAI's broader pattern of making data-retention features opt-in for organizational accounts. Builders deploying ChatGPT to end users through the Enterprise API should verify their account's memory configuration before assuming Dreaming V3 is active.

**Temporary Chat mode** suppresses memory entirely: no history stored, no synthesis runs, automatic deletion within 30 days. For builders building systems that handle sensitive queries, Temporary Chat remains the cleanest isolation mechanism.

---

## The Memory Summary Page

Users now have a structured transparency layer called the Memory Summary Page. It provides a high-level overview organized by category — work, hobbies, travel, community, preferences. From this surface, users can:

- **View** what has been synthesized
- **Correct** entries the system got wrong
- **Dismiss** individual items they don't want retained
- **Instruct** the system to raise or avoid specific topics going forward
- **Chat directly with ChatGPT** to audit specific memories ("what do you know about my current project?")

The user-steerable instruction layer is the most useful control for builders to understand. Users can now write persistent behavioral rules through a structured interface rather than repeating them in system prompts. For builders building on top of ChatGPT, this means some user preferences may already be baked into the session before your prompt runs.

---

## Builder and API Access: the memory_context Parameter

Enterprise and API customers gain access to Dreaming V3 via a new `memory_context` parameter. The parameter allows builders to build applications that leverage long-term user profiles without storing sensitive data on their own servers — the profile lives in OpenAI's infrastructure, and the builder surfaces it through the API.

The specific API documentation for `memory_context` was not publicly detailed in the June 4 announcement; OpenAI's developer documentation should be the authoritative source for parameter schema and usage constraints. The high-level capability is confirmed: programmatic access to the synthesized memory profile is now part of the Enterprise API offering.

For builders not using the Enterprise API tier, Dreaming V3 operates passively — it enriches responses in ChatGPT sessions but is not directly addressable through standard API calls.

---

## Competitor Context: How Memory Architectures Differ

Dreaming V3's launch changes where ChatGPT sits relative to Claude and Gemini on memory architecture:

| System | Memory Model | Update Model | Scope |
|--------|-------------|-------------|-------|
| **ChatGPT (Dreaming V3)** | Implicit auto-synthesis | Continuous self-update | Global/persistent |
| **Claude** | Explicit, user-controlled | ~24-hour periodic synthesis | Project-scoped + account-wide |
| **Gemini** | Hybrid: LLM-distilled profile + deltas | Periodic refresh | Account-scoped; integrates Gmail/Drive/Sheets |

The key distinction is implicit vs explicit. ChatGPT V3 captures context that arises naturally in conversation — the user does not have to ask for it to be remembered. Claude's model remains more explicit: memories are user-initiated or clearly scoped to a project. Gemini sits in between, adding cross-product context from the Google ecosystem.

For builders choosing a platform for memory-heavy applications (productivity tools, persistent assistants, long-running project support), the implicit synthesis model in Dreaming V3 reduces the burden of memory management on users but shifts the audit and correction burden to a system-managed profile rather than a user-curated list.

---

## The Audit Trail Problem for Regulated Workflows

The same auto-update mechanism that makes Dreaming V3 more accurate creates a compliance problem for accuracy-sensitive applications.

With Saved Memories (2024), the memory contained what the user or model explicitly saved. Changes required deliberate action. The audit trail was relatively simple: an entry existed, or it didn't.

With Dreaming V3, entries are platform-revised. A record may have been accurate when it was synthesized, updated silently by the background process, and updated again after further synthesis. Users (and builders) can view the current state of a memory but do not have automatic visibility into what it previously said or when it changed.

This creates liability in several contexts:

**Healthcare and legal workflows:** If a user's stated situation (employment status, insurance coverage, legal context) changes, the memory self-updates — but there is no automatically-generated log of the revision. A workflow that relied on memory state at time T cannot confirm what the system believed at that time.

**Compliance-gated decisions:** For any application where the rationale for an AI output needs to be auditable, a memory input that can revise itself without a revision log is a gap.

**Enterprise onboarding/offboarding:** When a user's role changes, Dreaming V3 will eventually synthesize new facts about their current responsibilities. But the window between "old role" and "updated memory" is opaque.

The practical mitigation for builders in regulated domains: do not treat the synthesized memory state as a primary data source for decisions. Use it as context enrichment, not as a record of facts you are relying on. Keep your own source of truth.

---

## Regulatory Exposure: GDPR and EU AI Act

The Dreaming V3 rollout has triggered immediate regulatory attention in Europe.

**EDPB preliminary opinion (June 5, 2026):** The European Data Protection Board released a preliminary opinion the day after the rollout, stating that persistent AI memory of the type Dreaming V3 implements constitutes **profiling** under GDPR. That classification triggers: user consent obligations before the profile is built, the right to erasure (and technical enforcement of that right), and data minimization requirements. OpenAI offers opt-out and deletion controls, but whether those controls satisfy GDPR's technical requirements for erasure of synthesized inferences (vs. source conversation data) is not yet settled.

**EU AI Act transparency deadline (August 2, 2026):** The EU AI Act's transparency obligations for chatbot systems take effect on August 2, 2026 — approximately eight weeks after the Dreaming V3 launch. Builders deploying ChatGPT-based applications to EU users will need to verify their disclosure and consent mechanisms against the EU AI Act's requirements as well as GDPR.

For builders operating exclusively in the US, these obligations don't apply directly — but enterprise buyers in Europe may require contractual representations about how memory features are handled, especially given the EDPB opinion.

---

## What Changes for Builders Starting June 4

1. **For ChatGPT-based consumer applications:** Users now bring a richer, auto-synthesized memory profile to each session. Context-setting prompts from users ("as I mentioned, I work in healthcare...") may be redundant. Some users will have memory turned on; some will have dismissed or corrected records. The system state is more personalized by default but also less predictable from session to session.

2. **For Enterprise API integrations:** Evaluate whether the `memory_context` parameter is appropriate for your use case. It offloads user-profile storage to OpenAI's infrastructure, which reduces your data-handling burden — but also means your application depends on OpenAI's memory state, which is not in your control.

3. **For regulated-domain applications:** Treat synthesized memory as enrichment context, not authoritative record. Log the memory state that influenced an output at the time of the output if you need an audit trail. Do not rely on the system's current memory state as a proxy for what it believed in the past.

4. **For EU-facing deployments:** Review GDPR consent flows before August 2. The EDPB's profiling classification means existing consent mechanisms designed for standard data collection may need updating to cover memory synthesis specifically.

5. **For Free-tier application users:** Dreaming V3 is expanding to Free users over the coming weeks. The 5x compute reduction makes this economically viable for OpenAI. Applications built on top of free-tier ChatGPT access will see the same memory enrichment as paid tiers once the expansion completes.

---

## Rollout Timeline

- **June 4, 2026:** Dreaming V3 live for ChatGPT Plus and Pro users in the US
- **Coming weeks:** Expansion to additional countries; Free and Go tiers
- **Enterprise/API access:** `memory_context` parameter available on Enterprise tier (timeline for broader API access not announced)

For the official announcement and current rollout status, see OpenAI's blog post: [Dreaming: Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/).

