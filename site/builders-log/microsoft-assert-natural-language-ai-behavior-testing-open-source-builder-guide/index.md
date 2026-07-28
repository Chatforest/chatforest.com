# Microsoft ASSERT: Write AI Behavior Tests in Plain English

> ASSERT, released at Build 2026, converts natural-language policy descriptions into automated, scored AI behavior tests — then closes the loop with the Agent Control Standard. Here's how it works and whether your agent pipeline needs it.


Writing AI behavior tests has always had a gap between the policy and the test. A product team decides the agent shouldn't forward confidential documents to external email addresses. A safety team writes a policy doc. Then a developer reads the policy doc and writes Python test cases, interpreting it. Every step is a translation — and translation loses information.

Microsoft [announced ASSERT at Build 2026 on June 2, 2026](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/). It removes one translation step. You write the policy in plain English. ASSERT turns it into test cases.

## What ASSERT Does

**ASSERT** stands for Adaptive Spec-driven Scoring for Evaluation and Regression Testing. It's an open-source evaluation framework built on Microsoft Research and released under a permissive license at [github.com/responsibleai/ASSERT](https://github.com/responsibleai/ASSERT).

The input is natural language: a description of what your agent is supposed to do and what it's not supposed to do. The output is a structured, runnable test suite with scenarios, inputs, expected behaviors, and pass/fail scores.

From the [Microsoft Foundry blog](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/):

> "ASSERT converts your policies into concrete, measurable evaluations, so rather than generic benchmarks you get context-specific test cases tailored to your agent's intended behavior."

The four-step process, per the [ASSERT documentation](https://github.com/responsibleai/ASSERT):

1. **Specify** — describe behaviors, goals, and restrictions in plain English (a policy document, a product spec, a list of rules)
2. **Generate** — ASSERT produces a set of acceptable and unacceptable behavior descriptions, then generates test scenarios and inputs for each
3. **Run** — the framework executes tests against your agent, recording intermediate actions and tool calls, not just final outputs
4. **Score** — results are measured against the behavioral specification; failures link back to specific policy violations, not just output mismatches

The trace recording is the key practical detail. Most evals check final output: did the agent answer correctly? ASSERT [captures OpenTelemetry spans so the judge can cite tool calls, routing, model calls, and latency as evidence](https://github.com/responsibleai/ASSERT) — not just the final response. This matters when the dangerous behavior is in the middle of an agentic workflow, not the end.

## Framework Support

ASSERT is framework-agnostic. Per the [ASSERT documentation](https://github.com/responsibleai/ASSERT), it evaluates a LangGraph agent, a CrewAI / OpenAI Agents SDK / DSPy / LlamaIndex / AutoGen system, a custom multi-agent orchestration, a plain Python callable, or a hosted model directly:

- **LangChain (LangGraph)** — evaluate LangGraph agents as a native target
- **CrewAI** — evaluate CrewAI systems as a native target
- **OpenAI Agents SDK** — evaluate OpenAI Agents SDK systems as a native target
- **DSPy** and **LlamaIndex** — evaluate DSPy and LlamaIndex systems as native targets
- **AutoGen** — evaluate AutoGen systems as a native target
- **LiteLLM** — [routes to 100+ model endpoints](https://github.com/responsibleai/ASSERT) across Bedrock, Azure, OpenAI, VertexAI, Cohere, Anthropic, Sagemaker, HuggingFace, VLLM, and NVIDIA NIM for provider-independent testing

The [partner ecosystem supporting ASSERT at launch](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) includes CrewAI, Arize AI, LiteLLM, Pipecat, and Pydantic.

The framework-independence is the architectural point. You're not writing OpenAI-specific tests or LangChain-specific tests. You're writing behavioral tests that describe what the agent should do, and ASSERT adapts the test execution to whatever framework is underneath.

## The ACS Loop

ASSERT works alongside the [Agent Control Standard (ACS)](/builders-log/agent-control-standard-acs-runtime-governance-ai-agents-builder-guide/), which defines runtime controls at five checkpoints in an agent workflow (input, LLM, state, tool execution, output). The relationship is:

1. **Run ASSERT** → find which policy violations exist and where in the workflow they occur
2. **Deploy ACS controls** → add deterministic guardrails at the specific checkpoints where violations happen
3. **Re-run ASSERT** → confirm that the controls fix the violations without breaking legitimate behaviors
4. **Monitor production** → observability tools catch drift before it reaches ASSERT

This gives builders a closed loop: evaluate → control → verify. The evaluation tool and the control standard are designed to speak the same language — both express policy as portable declarations, not as hardcoded model logic.

ACS policy files are YAML. ASSERT policy specifications are natural language that ASSERT transforms into the same structured form. The intent is that the same policy document drives both tools.

## What Else Shipped in the Foundry Trust Stack

ASSERT anchors a broader set of evaluation and governance tools that [shipped or entered preview at Build 2026](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/):

**Guided Guardrail Setup** (public preview) — [a short questionnaire about your agent's audience, data access, and use case surfaces the specific risks relevant to your scenario and recommends controls](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) like PII filters, jailbreak protection, and task adherence, with no security expertise required.

**Rubric Evaluator** (public preview) — [automatically generates evaluation criteria based on your agent's specific context](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/), rather than generic "helpfulness" scores. A legal research agent has different quality criteria than a customer support agent.

**Runtime Data Loss Prevention** (public preview) — [extends Microsoft Purview DLP into agent interactions](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/), enabling real-time detection and blocking of sensitive data in prompts and across AI interaction flows within Foundry-built apps and agents.

**Multi-turn evaluation and user simulation** (public preview) — [evaluates agent quality across full multi-step conversations, not just single responses, catching degradation and safety issues that only surface when context accumulates over time](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/). The user simulator [automatically generates realistic multi-turn conversations and scenarios to evaluate how agents perform](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/).

**Agent ROI measurement** (private preview) — [measures task completion rates, time saved, and cost efficiency for agents](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/), giving stakeholders data to justify investment and prioritize improvements.

## The Problem ASSERT Solves

The AI testing gap builders run into in production isn't "does this model score well on MMLU." It's these three things:

**Policy drift** — the behavior spec lives in a Google Doc and tests live in a CI pipeline. They diverge. ASSERT makes the policy the primary artifact; tests are generated from it, so drift is caught when the policy updates.

**Intermediate action testing** — final-output evals miss agentic failures. An agent can produce a correct final response after doing something unauthorized in the middle (writing to the wrong database, calling an external API it shouldn't). ASSERT's trace recording catches this.

**Framework migration risk** — moving from LangChain to CrewAI, or switching from GPT-5.5 to Claude Sonnet 4.6, should not invalidate your test suite. ASSERT's framework-agnostic execution means the behavioral spec stays stable across infrastructure changes.

## Who Needs This Now

**Start with ASSERT if:**
- You're building agents for enterprise customers who have written security policies or compliance requirements
- You're shipping agentic pipelines where failure modes are in intermediate steps, not just final output
- You're planning to switch model providers or frameworks and need to prove behavioral equivalence

**You can wait if:**
- Your agent is a simple RAG pipeline with no tool calls or external actions
- You're still in prototype phase before your behavioral spec has stabilized
- You're already running a comprehensive eval suite with framework-specific tooling that covers your risk surface

**Watch for ASSERT if:**
- You use ACS — ASSERT is designed to drive the ACS deployment loop
- You're on Azure and want the evaluation output to feed directly into Foundry observability

## Access

ASSERT is available now at [github.com/responsibleai/ASSERT](https://github.com/responsibleai/ASSERT). Documentation is at [aka.ms/assert](https://aka.ms/assert). The framework works independent of Azure — local development, any CI system, any cloud.

The [Guided Guardrail Setup, Rubric Evaluator, and Runtime DLP tools are in public preview](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/) in Microsoft Foundry. Agent ROI measurement is private preview.

