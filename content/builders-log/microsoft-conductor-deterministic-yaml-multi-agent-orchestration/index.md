---
title: "Microsoft Conductor: When You Want Your Agents to Stop Improvising"
date: 2026-05-25
description: "Released May 14, Microsoft's open-source Conductor takes a deliberate stance against LLM-driven orchestration. You define your multi-agent workflow in YAML. Routing is deterministic. No tokens spent deciding what runs next. For workflows with known structure, that tradeoff makes a lot of sense."
content_type: "Builder's Log"
categories: ["MCP", "Agent Infrastructure", "Open Source", "Industry Analysis"]
tags: ["microsoft", "conductor", "multi-agent", "orchestration", "yaml", "deterministic", "github-copilot", "anthropic", "mcp", "open-source", "workflow", "agent-infrastructure"]
---

On May 14, 2026, Microsoft published [Conductor](https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows/) — an open-source CLI for defining multi-agent workflows in YAML. The routing between agents is not handled by a language model. It is handled by your configuration file.

That is the point. And it is a deliberate point.

## The Problem Conductor Is Solving

Every framework for multi-agent AI has to answer the same question: who decides what runs next?

The popular answer has been: another LLM. A planner model, an orchestrator agent, a supervisor layer — something with the capability to read context and decide which downstream agent should handle the next step. The appeal is flexibility. You do not need to anticipate every branch in advance. The orchestrator figures it out.

The drawback is everything that comes with putting an LLM in a control loop. Every routing decision costs tokens. The orchestrator's choices are non-deterministic — the same input does not guarantee the same routing path. Debugging why your workflow went sideways means inspecting LLM reasoning, not reading code. And if your orchestrator model is the same one doing the work, it is doing two different cognitive jobs simultaneously.

Conductor's design premise is: for workflows with known structure, you do not need an LLM to do the routing. You already know the structure. Put it in a file.

## What Conductor Actually Does

Conductor is a YAML-first CLI. You define a workflow as a file: the agents involved, the prompts they run, the tools they can access, and the conditions that determine which agent runs next. Each agent definition includes routing conditions — Jinja2 expressions evaluated against the agent's output. First matching condition wins.

A minimal workflow looks roughly like this:

```yaml
name: code-review-pipeline
entry: analyzer
agents:
  analyzer:
    prompt: "Review this code for bugs and security issues."
    routing:
      - condition: "{{ 'critical' in output }}"
        next: security-team
      - condition: "{{ exit_code == 0 }}"
        next: formatter
  formatter:
    prompt: "Format the reviewed code to style guidelines."
  security-team:
    prompt: "This code has critical issues. Escalate with full details."
```

The orchestration layer evaluates those conditions. It does not ask an LLM what to do. There is no token budget for routing decisions. The workflow runs the same way every time for the same input.

Conductor also supports shell steps — raw script execution as a workflow step. Your linter, test suite, build command, or any shell script becomes a first-class participant in the workflow without any modification. Exit codes route just like agent outputs.

## MCP Servers as Tool Providers

Agents in a Conductor workflow get their capabilities from MCP servers. You configure which MCP servers each agent has access to, and those servers provide the tools — web search, documentation lookup, code analysis, database access, whatever you have running. This is the integration point that makes Conductor composable with the rest of the MCP ecosystem.

The practical value here is separation of concerns. Your workflow file handles orchestration structure. Your agents handle reasoning. Your MCP servers handle capability. Each layer does one thing.

## Human Gates

Conductor treats human oversight as a first-class workflow step, not an afterthought. You can insert an explicit gate into any workflow that pauses execution and waits for a human to confirm before proceeding. This is not a hack or workaround — it is a defined step type in the workflow syntax.

For workflows where human review at a checkpoint matters — a security assessment before deploying, a content review before publishing, a financial check before executing a transaction — the gate is part of the specification, not something you add externally by interrupting the process.

## What Conductor Supports

Conductor requires Python 3.12 or later. It ships as a CLI tool and works with two runtime providers: the GitHub Copilot SDK and the Anthropic Agents SDK. The project is open source under the MIT license at [github.com/microsoft/conductor](https://github.com/microsoft/conductor).

The runtime provider choice is where the actual LLM work happens. The agents in your workflow are backed by Copilot or Claude. The orchestration between them — the routing, the condition evaluation, the step execution — is all deterministic.

## The Tradeoff Stated Plainly

Conductor is not a general-purpose agentic framework. It is specifically for workflows where you know the shape of the work in advance. If your pipeline is genuinely exploratory — if you need the system to figure out not just the answers but also the path — then a deterministic YAML router is the wrong tool.

But a surprising number of production workflows are not exploratory. They are repetitive. The same kind of code review runs a thousand times. The same content pipeline processes every draft. The same data validation checks every import. For those cases, the flexibility of LLM-driven orchestration is solving a problem you do not have, while adding costs and unpredictability you did not ask for.

Conductor's bet is that builders who have run agentic workflows in production long enough will recognize this distinction. The developers who shipped a dynamic orchestrator, watched it hallucinate a routing decision at 2 AM, and spent an hour reconstructing what happened — they understand the appeal of a YAML file that does exactly what it says.

## Why This Matters for the Ecosystem

Conductor is an interesting signal in how the orchestration space is maturing. Early multi-agent frameworks leaned heavily into the magic of autonomous coordination — let the models figure it out. That magic is genuinely useful for certain problem classes.

But engineering culture tends toward predictability. Code review, CI pipelines, data processing, document workflows — these are domains where engineers want deterministic behavior they can version, test, and debug. Conductor is a bet that there is significant demand for multi-agent tooling that feels more like writing a build script than prompting an orchestrator.

It also demonstrates a pattern that will probably recur: using MCP servers for capability (what the agents can do) while keeping orchestration logic in code (how the agents are sequenced). That clean separation may age well as the ecosystem accumulates more MCP-accessible tools and more opinionated opinions about where non-determinism is acceptable.

---

*Microsoft Conductor was announced May 14, 2026. Source: [Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows/) and [github.com/microsoft/conductor](https://github.com/microsoft/conductor).*
