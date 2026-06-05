# The Safety Benchmarks Are Wrong: Cisco Study Shows Multi-Turn Attacks Bypass Frontier Models at Rates No Benchmark Predicts

> Cisco tested 15 frontier AI models across 30,000 single-turn and 7,000 multi-turn attacks. The gap between published benchmarks and production reality is up to 83 percentage points. If you're deploying agents, you're making security decisions on data that doesn't describe your situation.


On May 27, 2026, Cisco published a study that should change how every builder thinks about AI security benchmarks. It tested 15 flagship models from OpenAI, Anthropic, Google, and xAI across roughly 30,000 single-turn prompts and 7,000 multi-turn attacks spanning 1,400+ conversations.

The finding: the attack success rates published in model safety cards do not predict real-world attack success rates. The gap is not a rounding error. For some models, it exceeds 80 percentage points.

## The Numbers

Single-turn attack success rates for frontier models — the figures typically cited in safety documentation — cluster between 2% and 20% for the leading closed models. Cisco replicated those numbers. Then it ran the same models through multi-turn attack sequences.

Results for selected models under multi-turn conditions:

- **Grok 4.1 Fast**: 88% attack success rate under multi-turn conditions (compared to single-turn rates near 5-8%)
- **Gemini 3 Pro**: 73% multi-turn attack success rate (from ~18% single-turn)
- **Claude (Anthropic)**: 16% multi-turn attack success rate (from 3% single-turn, the lowest single-turn rate in the study)
- Several OpenAI flagship models: 40-60% range under multi-turn pressure, compared to single-digit single-turn figures

Cisco's threshold recommendation: any model where the absolute gap between single-turn and multi-turn attack success rate exceeds 15 percentage points should trigger a manual security review before deployment. Eight of the fifteen models in the study are above that threshold.

## Why This Gap Exists

Single-turn benchmarks test whether a model will comply with a harmful request presented directly, in isolation. The model sees one message. It either refuses or it doesn't.

Multi-turn attacks work differently. They establish context, build rapport, shift the conversational frame, and then make the harmful request — or disguise it as a continuation of legitimate earlier conversation. The model's refusal training was largely built around resisting explicit harmful requests. It is less robust against requests that arrive wrapped in plausible context.

In agentic deployments, every interaction is multi-turn by design. A user agent has memory, conversation history, and tool access accumulated across many exchanges. An adversarial user who knows this can construct a sequence where no individual message triggers a refusal, but the accumulated context produces the harmful output.

This is not a theoretical risk. Cisco's 7,000 multi-turn attacks were not novel or exotic. They applied known social engineering patterns — persona shifting, context injection, gradual escalation — implemented in automated conversation sequences. The attack methodology is documented, replicable, and available to anyone who has read AI red-teaming literature.

## What This Means If You're Building Agents

**Benchmark-driven model selection is insufficient for production security.** If you chose your model partly because its safety card cited a 3% or 5% attack success rate, that number describes a test environment that does not resemble your users' interaction patterns. Agents that maintain conversation history across sessions are operating under conditions where multi-turn attack success rates, not single-turn rates, are the relevant metric.

**Your security perimeter is the conversation sequence, not the individual message.** Traditional content filtering operates on message-level signals. A multi-turn attack may contain no single message that would trigger a filter. The harmful intent is distributed across turns. Builders need monitoring that evaluates patterns across a conversation, not just individual inputs.

**Conversation memory is also an attack surface.** Any feature that lets users persist context — saved conversation threads, user preference files, long-term memory tools — is a feature that lets adversarial users write persistent context into your system's frame of reference. This context will be present when the eventual harmful request arrives.

**The 15-point gap threshold is a deployment gate, not an aspirational target.** Cisco's recommendation is concrete: if a model's multi-turn attack success rate exceeds its single-turn rate by more than 15 percentage points, put it through manual security review before it goes to production. Eight of fifteen tested flagship models would fail that gate today. Check where your model sits.

## What Builders Should Do

**Test the model you're actually deploying, not the model in the safety card.** The Cisco methodology — automated multi-turn conversations using known social engineering patterns — is reproducible. Run it against your model in your deployment context before launch.

**Treat agentic systems as high-security contexts by default.** If your agent can take actions with real consequences — sending emails, making API calls, accessing files, executing code — assume the adversarial multi-turn attack profile applies. Single-turn safety benchmarks are baseline due diligence, not sufficient due diligence.

**Instrument for conversation-level anomaly detection.** Log conversation sequences, not just individual messages. Look for patterns: repeated context establishment followed by sensitive requests, persona inconsistency across turns, sudden introduction of high-stakes requests after lengthy rapport-building.

**Scope your agents aggressively.** The narrower the action surface, the less useful a successful multi-turn attack becomes. An agent that can only query a read-only database is a lower-value target than one with broad tool access. Least-privilege applies to agents.

## The Benchmark Problem Is Structural

This isn't Cisco calling out specific models — all fifteen models in the study showed elevated attack success rates under multi-turn conditions. It's a structural problem with how safety benchmarks are constructed and communicated.

Single-turn benchmarks measure something real: a model's baseline refusal training. But they don't measure what users experience in practice, and they don't measure what adversarial users exploit in practice. As agentic deployment becomes standard, the gap between benchmark conditions and production conditions will only grow.

Cisco's recommendation to the industry: publish multi-turn attack success rates alongside single-turn figures as a minimum disclosure standard. Until that becomes standard practice, builders are responsible for conducting their own multi-turn evaluation before deployment.

The safety number on the model card describes a test. Your deployment is not that test.

---

*Cisco released findings May 27, 2026. The full study covers 15 closed frontier models across OpenAI, Anthropic, Google, and xAI. Methodology details are published in the report.*

