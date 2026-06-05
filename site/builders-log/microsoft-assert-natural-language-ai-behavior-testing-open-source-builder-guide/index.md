# Microsoft ASSERT: Write AI Behavior Tests in Plain English

> ASSERT, released at Build 2026, converts natural-language policy descriptions into automated, scored AI behavior tests — then closes the loop with the Agent Control Standard. Here's how it works and whether your agent pipeline needs it.


Writing AI behavior tests has always had a gap between the policy and the test. A product team decides the agent shouldn't forward confidential documents to external email addresses. A safety team writes a policy doc. Then a developer reads the policy doc and writes Python test cases, interpreting it. Every step is a translation — and translation loses information.

Microsoft announced ASSERT at Build 2026 on June 2, 2026. It removes one translation step. You write the policy in plain English. ASSERT turns it into test cases.

## What ASSERT Does

**ASSERT** stands for Adaptive Spec-driven Scoring for Evaluation and Regression Testing. It's an open-source evaluation framework built on Microsoft Research and released under a permissive license at [github.com/responsibleai/ASSERT](https://github.com/responsibleai/ASSERT).

The input is natural language: a description of what your agent is supposed to do and what it's not supposed to do. The output is a structured, runnable test suite with scenarios, inputs, expected behaviors, and pass/fail scores.

From the Microsoft Foundry blog:

> "ASSERT converts organizational policies into concrete, measurable evaluations specifically tailored to agent behavior rather than using generic benchmarks."

The four-step process:

1. **Specify** — describe behaviors, goals, and restrictions in plain English (a policy document, a product spec, a list of rules)
2. **Generate** — ASSERT produces a set of acceptable and unacceptable behavior descriptions, then generates test scenarios and inputs for each
3. **Run** — the framework executes tests against your agent, recording intermediate actions and tool calls, not just final outputs
4. **Score** — results are measured against the behavioral specification; failures link back to specific policy violations, not just output mismatches

The trace recording is the key practical detail. Most evals check final output: did the agent answer correctly? ASSERT records the path: did the agent make the right tool calls in the right order? This matters when the dangerous behavior is in the middle of an agentic workflow, not the end.

## Framework Support

ASSERT is framework-agnostic. The integration list at launch:

- **LangChain** — works with LCEL chains and LangGraph agents
- **CrewAI** — crew-level and agent-level policy evaluation
- **LiteLLM** — provider-independent routing, test across model switches
- **OpenAI** — Responses API and Assistants API
- **Pydantic AI** — structured output validation with policy overlay

The partner ecosystem supporting ASSERT at launch includes CrewAI, Arize AI, LiteLLM, Pipecat, and Pydantic.

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

ASSERT anchors a broader set of evaluation and governance tools that shipped or entered preview at Build 2026:

**Guided Guardrail Setup** (public preview) — a questionnaire-driven interface for configuring content filters and safety controls without writing code. Personalized recommendations based on your agent's use case, audience, and risk profile.

**Rubric Evaluator** (public preview) — context-aware quality scoring. Instead of generic "helpfulness" scores, rubrics let you define what quality means for your specific use case. A legal research agent has different quality criteria than a customer support agent.

**Runtime Data Loss Prevention** (public preview) — real-time detection of sensitive data leaving your agent system via tool calls or output generation. Configurable to specific data categories (PII, financial data, code repositories).

**Multi-turn evaluation and user simulation** — ASSERT-adjacent tooling for evaluating agents across full conversation trajectories, not just single-turn interactions. The user simulator generates realistic multi-turn inputs based on behavioral specifications.

**Agent ROI measurement** (private preview) — tracks agent-driven outcomes against business metrics so you can connect evaluation results to business value. Still in early access.

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

The Guided Guardrail Setup, Rubric Evaluator, and Runtime DLP tools are in public preview in Microsoft Foundry. Agent ROI measurement is private preview with an application process.

