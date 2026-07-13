# Thinking Machines Lab's Founding Credo: Why Centralized Alignment Is a Power Problem and Your Fine-Tuning Data Is a Moat

> On July 10, 2026, Thinking Machines Lab — founded by ex-OpenAI CTO Mira Murati and safety researcher John Schulman — published 'The Future Worth Building Is Human,' a philosophy post arguing that centralized alignment concentrates power dangerously, tacit local knowledge beats central AI systems, and builders should own model weights rather than rent API access. Here's what it says and what builders should do with it.


On July 10, 2026, Thinking Machines Lab published a post it calls "The Future Worth Building Is Human." It reads less like a product announcement and more like a philosophical manifesto — a deliberate statement of why the company exists and what it believes is wrong with the current trajectory of AI development.

The authors don't name OpenAI or Anthropic. They don't have to.

The post, attributed to Thinking Machines as a whole, is one of the most direct public critiques of centralized AI alignment to come from an AI lab itself. Coming from a team that includes Mira Murati (former OpenAI CTO), John Schulman (former OpenAI co-founder and safety researcher), Lilian Weng, Barrett Zoph, and Andrew Tulloch, the argument carries weight. This is not an academic paper. It is a company telling you what it is building and why it thinks the field is getting something fundamentally wrong.

---

## The Tacit Knowledge Argument

The post's first major claim draws on two economists most AI builders have probably not thought about since undergrad: Friedrich Hayek and Michael Polanyi.

Hayek's 1945 essay on the use of knowledge in society argued that productive information is not centralized in any single mind or institution — it is "tacit, local, fleeting, and held privately by those who acquired it through their work." No central planner, however well-resourced, can aggregate what thousands of workers, doctors, engineers, and farmers know from direct experience. This is why planned economies fail and markets work: prices let distributed knowledge coordinate without centralization.

Thinking Machines is applying this to AI. A single frontier model, however large, trained on general internet data, cannot capture the expert judgment of a specific surgeon, the institutional memory of a specific legal team, or the production floor instincts of a specific manufacturing operation. That knowledge is tacit — it lives in the person who has done the work, not in any text they wrote about it.

The company invokes Toyota's 2014 decision to reintegrate human craftspeople with its automated assembly lines. Toyota found that automation had displaced the workers who understood *why* certain assembly steps worked, and quality degraded. The fix was not to train the robots better — it was to bring the humans back in. "To be the master of the machine," Toyota concluded, "you have to have the knowledge and the skills to teach the machine."

The implication for builders: general-purpose AI systems are structurally limited in domains where tacit expertise matters most. The companies that will capture the most value from AI are those that figure out how to get their domain knowledge *into the model weights* — not just into the system prompt.

---

## The Decentralized Alignment Thesis

This is the most provocative part of the post, and the part that reads most clearly as a critique of the current paradigm.

Thinking Machines argues that "values must be encoded in the model weights" — but not by a single organization. The problem with centralized alignment, as they frame it, is not technical. It is political.

When one lab decides what an aligned AI system should and should not do, it is making value choices on behalf of every person who uses that system. Those choices reflect the lab's culture, its legal environment, its investor base, and its own judgment about what is safe or appropriate. A single alignment spec, the post argues, "suppresses creativity and diversity" — but more seriously, it concentrates power.

The warning is direct: "Power that needs nothing from people loses the incentive to care for their needs."

This is a statement about what happens when AI systems become sufficiently capable and sufficiently centralized that users have no meaningful alternatives. Thinking Machines is not arguing that OpenAI or Anthropic are malicious. They are arguing that the *structure* of centralized alignment — one set of values baked into one model used by billions — is a governance risk regardless of who is doing it.

Their proposed alternative: build models that individuals and organizations can customize at the weight level, encoding their own values and priorities. Alignment becomes distributed, not concentrated.

---

## Interaction Models as the Technical Answer to the Interface Bottleneck

The third pillar of the post is about the interface between humans and AI systems.

Current chat-based AI, TML argues, creates a bottleneck. Typing a prompt, waiting for a response, reading output, and typing again is a slow, impoverished communication channel compared to how humans actually exchange knowledge: through conversation, gesture, interruption, demonstration, and real-time feedback.

Their technical response to this is "interaction models" — a category they previewed in May 2026 with TML-Interaction-Small, a 276-billion-parameter mixture-of-experts model with 12 billion active parameters. The system processes audio, video, and text in 200-millisecond micro-turns rather than full conversation turns, enabling the AI to listen, process, and respond simultaneously — what engineers call full-duplex operation.

At 0.40-second turn latency, TML-Interaction-Small outperforms both OpenAI Realtime 2 and Google Gemini 3.1 Flash Live on the FD-bench v1.5 interaction benchmark. The architecture splits into two components: an interaction model that stays live in the conversation, and a background reasoning model that handles tool calls and computation asynchronously while sharing full context.

The point is not just speed. It is that the richness of the human-AI communication channel determines how much tacit knowledge can actually flow from the human to the model in real time. Richer interface → more knowledge transfer → better outcomes. This is why TML considers interaction models a research priority, not just a product feature.

---

## Company Context: What TML Has Shipped

For builders evaluating whether this manifesto has any technical substance behind it, the company's track record matters.

Thinking Machines Lab was founded in February 2025 by Mira Murati and colleagues who had left OpenAI. It closed a $2 billion seed round in July 2025 at a $12 billion valuation — at the time the largest seed round in AI history. A subsequent financing round that would have valued the company at $50 to $60 billion collapsed in January 2026 when prospective backers were unwilling to support that markup on the strength of early-stage products. The company is currently operating at its original $12 billion valuation with approximately 140 to 169 employees.

Two live products exist:

**Tinker** (October 2025): An API for fine-tuning language models. Users submit fine-tuning jobs; TML runs them on its internal infrastructure. The product directly implements the "ownership over rental" thesis — organizations pay to adapt a model to their context rather than prompting a shared one.

**TML-Interaction-Small** (May 2026): The full-duplex interaction model described above, currently in preview. The company has not published full API pricing or general availability timelines.

Infrastructure commitments from Nvidia and Google reportedly run into the billions. The technical team is deep: John Schulman's "LoRA Without Regret" (September 2025) addressed a long-standing instability in low-rank adaptation training; Horace He's work on nondeterminism in LLM inference is standard reading in ML engineering circles.

---

## What Builders Should Take From This

The post is philosophy, not a product release. But it contains four practical implications worth building into your architecture decisions now.

**1. Fine-tuning data is a moat, not a nice-to-have.** If TML's tacit knowledge thesis is correct, the builders who win will be those who systematically capture domain expertise in model weights — not just in prompts or retrieval indexes. Start investing in structured fine-tuning datasets from your domain experts now, before your competitors do. The prompt-engineering ceiling is real; weight-level customization does not have the same ceiling.

**2. Prompt-level control is structurally limited.** System prompts are powerful, but they operate on top of a model whose values and style are already fixed. Every refusal, every tone shift, every capability gap you hit via prompting is a consequence of someone else's alignment choices. If your use case requires different value trade-offs — more risk tolerance, different output norms, domain-specific judgment — you will eventually need to influence the weights, not just the prompts.

**3. Full-duplex voice is not incremental — it is architectural.** If you are building any voice-based AI product and are still on a turn-based architecture (speak → wait → response), budget a migration timeline. The 200ms micro-turn paradigm changes what is possible in live assistance, coaching, medical triage, and real-time code review. OpenAI Realtime and Gemini Flash Live are in this space; TML is now measurably ahead on benchmark latency.

**4. Watch the alignment market, not just the model market.** OpenAI, Anthropic, and Google make alignment decisions for their models and publish their reasoning intermittently. TML is explicitly building a competitor that lets you make those decisions yourself — or at minimum, customize the output of theirs. As this market develops, the question "whose values are baked into my AI system?" will become a vendor selection criterion, not just an abstract ethics question.

---

"The Future Worth Building Is Human" is a short post — under 3,000 words. It is worth reading in full at [thinkingmachines.ai/blog/the-future-worth-building-is-human/](https://thinkingmachines.ai/blog/the-future-worth-building-is-human/). The argument is philosophical, but the stakes are concrete: who controls the value systems of the AI tools your users rely on, and what happens when that answer is "one company you don't own stock in."

Thinking Machines is building an answer. It may not be the right one. But builders who ignore the question are making a choice by default.

