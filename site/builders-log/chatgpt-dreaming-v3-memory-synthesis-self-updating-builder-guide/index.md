# ChatGPT Dreaming V3: Self-Updating Memory and What It Means for Builders

> OpenAI began rolling out Dreaming V3 on June 4, 2026 — a background synthesis process that replaces the saved-memories list and revises entries automatically, the way a memory of 'planning a Singapore trip' rewrites itself once the trip is over. OpenAI's only published performance figure is a roughly 5x cut in the compute needed to serve the system; no accuracy benchmarks were published. The same auto-revision that removes repetitive context-setting also means older memory states aren't preserved for audit.


On June 4, 2026, OpenAI began rolling out Dreaming V3 to ChatGPT Plus and Pro users in the US ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/)). For regular users, it means ChatGPT remembers more and asks less. For builders, it introduces a different mental model of what "memory" means in a production context, and a set of open compliance questions that weren't present with the older saved-memories architecture.

**At a glance:** Dreaming V3 is a background process that reads across a user's conversation history, synthesizes a persistent memory profile, and automatically revises that profile as circumstances change — without user prompting. The only performance figure OpenAI has published is an approximate 5x reduction in the compute required to serve the system, which is what it says makes Free-tier rollout viable; no accuracy benchmarks have been published. The auto-update capability that removes repetitive context-setting also means platform-revised records replace user-authored ones, raising audit trail questions for regulated or accuracy-sensitive workflows. Part of our **[Builder's Log](/builders-log/)**.

---

## The Architecture History: Three Distinct Systems

OpenAI has shipped three distinct memory systems for ChatGPT since 2024, and the differences matter for builders. OpenAI recaps this history itself in its [Dreaming announcement](https://openai.com/index/chatgpt-memory-dreaming/):

**Saved Memories (from April 2024):** Manual and reactive. In OpenAI's own description, saved memories "were only written during the conversation and relied on strong cues to decide when to trigger memory" — the experience "could feel like talking to someone who took a few notes, but still forgot everything." Users or the model had to explicitly decide something was worth saving.

**Dreaming V0 (from April 2025):** OpenAI added a background synthesis layer — the first version of what it calls "dreaming" — that could reference chat history beyond the saved-memories list. OpenAI has said this version "historically was never sufficient as a standalone memory system"; it was an augmentation, not a replacement.

**Dreaming V3 (June 4, 2026):** Replaces the saved-memories list as ChatGPT's primary memory mechanism. The background synthesis process reads across a user's conversations, identifies facts and preferences, and writes a continuously updated profile — no explicit save action required.

The shift from V0 to V3 is a change in role, not just capability: synthesis goes from a supplemental layer to the system of record.

---

## How the Self-Updating Memory Works

OpenAI's own example, from its announcement: a memory that starts out reflecting a user's upcoming trip to Singapore updates itself once the trip has passed, so the system reflects that the event is now in the past — without the user correcting it or asking for an update ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/)).

OpenAI's illustrative examples of what gets synthesized include specific facts (camera equipment, dietary restrictions such as being vegetarian), stated preferences and constraints (wanting strong air conditioning while traveling, preferring quiet restaurants), and inferred context such as a user's home location — all drawn from patterns across past conversations rather than a single explicit "remember this" instruction ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/)).

The synthesis runs in the background between conversations, not within them — per OpenAI, the active conversation itself doesn't trigger the rewrite; a background process does.

---

## Performance: The One Number OpenAI Actually Published

OpenAI's Dreaming V3 announcement discloses exactly one quantified performance figure: an "approximately 5x" reduction in the compute required to serve the dreaming system, which the company says is what makes expanding the feature to Free-tier users economically viable ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/)).

OpenAI has not published factual-recall percentages, preference-adherence scores, or a benchmark methodology comparing Dreaming V3 against the saved-memories system or Dreaming V0. Treat any specific accuracy numbers circulating for Dreaming V3 as unverified — none appear in OpenAI's own materials as of this writing, and we could not locate an independent evaluation either.

---

## Memory, Training, and Temporary Chat

Data handling differs by account tier, and builders should verify the current configuration rather than assume a default.

For ChatGPT Business (formerly Team) workspaces, OpenAI's own FAQ states that "workspace data, including conversations and memories, is not used to train OpenAI models" by default ([OpenAI Business Memory FAQ](https://help.openai.com/en/articles/9295112-memory-faq-business-version)). For ChatGPT Enterprise and Edu, OpenAI's release notes describe the Enterprise version of dreaming ("improved memory") rolling out through an admin-controlled toggle during an early-access period, turning on by default afterward unless an admin opts out ([OpenAI Enterprise & Edu Release Notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes)). Builders deploying to Enterprise end users should check their workspace's actual setting before assuming Dreaming V3 is active.

**Temporary Chat mode** suppresses memory entirely. OpenAI's Temporary Chat FAQ states these chats "do not use existing memories or create new memories," are not used for model training, and are deleted from OpenAI's systems within 30 days ([OpenAI Temporary Chat FAQ](https://help.openai.com/en/articles/8914046-temporary-chat-faq)). For builders handling sensitive queries, Temporary Chat remains the cleanest isolation mechanism.

---

## The Memory Summary Page

Users have a transparency surface called the memory summary page. OpenAI's own examples describe it organizing what's been synthesized by category — including work, hobbies, travel interests, and community involvement ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/)). From this surface, users can view what's been synthesized, correct entries the system got wrong, and dismiss individual items they don't want retained.

For builders, the more consequential piece is that users can now express persistent behavioral preferences through this interface rather than repeating them in every session — meaning some user preferences may already be baked into a session before your prompt runs, whether or not your application is aware of it.

---

## API and Developer Access

OpenAI's June 4, 2026 announcement makes no mention of an API parameter, enterprise developer endpoint, or any programmatic route for accessing the synthesized memory profile — it describes a ChatGPT product feature, not a developer-facing capability ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/)). We could not find any OpenAI developer documentation describing memory access via the API.

Builders integrating with ChatGPT via the API today continue to manage their own conversation state (for example, via the Responses API's `previous_response_id` for chaining) rather than reading from Dreaming's synthesized profile. If OpenAI exposes this programmatically in the future, its developer documentation would be the authoritative source — nothing to that effect has been published as of this writing, so don't build against a parameter that doesn't yet exist.

---

## Competitor Context: How Memory Architectures Differ

| System | Memory Model | Update Model | Scope |
|--------|-------------|-------------|-------|
| **ChatGPT (Dreaming V3)** | Implicit auto-synthesis | Continuous background revision | Account-wide, cross-conversation ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/)) |
| **Claude** | Explicit and auto-detected entries | Real-time updates in the current version; the legacy system synthesized on a roughly 24-hour cycle | Separate per-project memory plus account-wide memory for non-project chats ([Anthropic](https://www.anthropic.com/news/memory); [Claude Help Center](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)) |
| **Gemini** | Opt-in "Personal Intelligence" drawing on connected Google apps | Retrieval at query time from connected sources (Gmail, Photos, Search, YouTube) | Personal, opt-in; rolling out to Google AI Pro/Ultra subscribers in the US ([Google](https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence/)) |

The key distinction is implicit vs. explicit. ChatGPT's Dreaming V3 captures context that arises naturally in conversation without the user asking for it to be remembered. Claude's model remains more user-driven, with memory kept separate per project. Gemini's Personal Intelligence is opt-in and pulls from connected Google services rather than synthesizing purely from chat history.

For builders choosing a platform for memory-heavy applications, the implicit synthesis model in Dreaming V3 reduces the burden of memory management on users but shifts the audit and correction burden onto a system-managed profile rather than a user-curated list.

---

## The Audit Trail Problem for Regulated Workflows

The same auto-update mechanism that makes Dreaming V3 more convenient creates a genuine question for accuracy-sensitive applications.

With Saved Memories (2024), the memory contained only what a user or the model explicitly saved; changes required deliberate action, so the audit trail was simple — an entry existed or it didn't.

With Dreaming V3, entries are platform-revised in the background. A record may have been accurate when synthesized, then updated silently, then updated again after further synthesis. Users and builders can view the current state of a memory, but OpenAI's announcement does not describe any built-in revision history showing what a memory previously said or when it changed.

This is a plausible liability in several contexts:

**Healthcare and legal workflows:** If a user's stated situation changes, the memory self-updates — but without a visible revision log, a workflow that relied on the memory state at a specific past time can't confirm what the system believed then.

**Compliance-gated decisions:** For any application where the rationale behind an AI output needs to be auditable, a memory input that revises itself without a revision log is a gap.

**Enterprise onboarding/offboarding:** When a user's role changes, Dreaming V3 will eventually synthesize new facts about their responsibilities — but the window between the old role and the updated memory is opaque.

The practical mitigation for builders in regulated domains: don't treat synthesized memory as a primary data source for decisions. Use it as context enrichment, not as a record of facts you're relying on, and keep your own source of truth.

---

## Regulatory Exposure: GDPR and the EU AI Act

Dreaming V3's auto-revising profile raises real open questions under EU law — but it's worth being precise about what has and hasn't actually happened on the regulatory side.

**GDPR:** A persistent, self-revising profile of a user's facts and preferences maps closely onto GDPR's definition of profiling — "any form of automated processing of personal data... to evaluate certain personal aspects relating to a natural person" ([GDPR, Article 4(4), EUR-Lex](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)). We could not find any published EDPB opinion or other regulator statement specifically addressing Dreaming V3's profiling status. Builders relying on Dreaming V3 for EU users shouldn't assume the feature has been formally cleared, and should track guidance directly from the EDPB and OpenAI's own EU-facing documentation rather than secondary summaries.

**EU AI Act:** The Act's Article 50 transparency obligations — including the requirement that AI systems interacting directly with people disclose that they are AI, unless obvious from context — apply from August 2, 2026 ([Regulation (EU) 2024/1689, EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202401689); [EU AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-50)), about eight weeks after the Dreaming V3 launch. Builders deploying ChatGPT-based applications to EU users need to verify their disclosure mechanisms against this deadline, independent of any memory-specific ruling.

For builders operating exclusively in the US, none of this applies directly — but enterprise buyers in Europe may still ask for contractual representations about how memory features are handled.

---

## What Changes for Builders Starting June 4

1. **For ChatGPT-based consumer applications:** Users now bring a richer, auto-synthesized memory profile to each session. Context-setting prompts from users ("as I mentioned, I work in healthcare...") may be redundant. Some users will have memory turned on; some will have dismissed or corrected records. The system state is more personalized by default but also less predictable from session to session.

2. **For applications built on the API:** Dreaming V3's synthesized memory is not currently exposed through the API. Continue managing your own conversation/user state as you do today; don't design around an OpenAI-hosted memory profile that isn't accessible programmatically.

3. **For regulated-domain applications:** Treat synthesized memory as enrichment context, not an authoritative record. Log the memory state that influenced an output at the time of the output if you need an audit trail — don't rely on the system's current memory state as a proxy for what it believed in the past.

4. **For EU-facing deployments:** Review your AI-disclosure and consent mechanisms ahead of the EU AI Act's August 2, 2026 Article 50 deadline, and keep an eye on EDPB guidance for anything specifically addressing self-revising memory profiles.

5. **For Free-tier application users:** Dreaming V3 is expanding to Free users over the coming weeks. OpenAI attributes this to the ~5x compute-efficiency gain described above. Applications built on top of Free-tier ChatGPT access will see the same memory enrichment as paid tiers once the expansion completes.

---

## Rollout Timeline

- **June 4, 2026:** Dreaming V3 live for ChatGPT Plus and Pro users in the US ([OpenAI](https://openai.com/index/chatgpt-memory-dreaming/))
- **Coming weeks:** Expansion to additional countries and to Free and Go tiers
- **Enterprise:** "Improved memory" (Dreaming V3 for Enterprise/Edu workspaces) rolling out via admin-controlled early access ([OpenAI Enterprise & Edu Release Notes](https://help.openai.com/en/articles/10128477-chatgpt-enterprise-edu-release-notes))

For the official announcement and current rollout status, see OpenAI's blog post: [Dreaming: Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/).

