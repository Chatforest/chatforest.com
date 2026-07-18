---
title: "Hopsworks 5.0 Puts Claude Code Inside Your ML Platform: A Builder's Guide to the Coding Data Stack"
date: 2026-07-05
description: "Hopsworks 5.0 (GA June 30) embeds Claude Code and Codex directly inside an ML lakehouse platform—no context switching, CLI-first agent tooling, and air-gapped sovereign deployments for enterprises that need data to stay put."
tags: ["mlops", "claude-code", "ml-pipeline", "feature-store", "data-platform", "sovereign-ai", "hopsworks", "coding-agents", "lakehouse"]
---

On June 30, 2026, [Hopsworks released version 5.0](https://www.globenewswire.com/news-release/2026/06/30/3319457/0/en/releasing-hopsworks-5-0-introducing-the-coding-data-and-ai-stack.html) — a unified ML lakehouse platform that embeds Claude Code and Codex directly inside the development environment. The core shift: instead of an AI coding assistant you context-switch to when you need help, the agent lives inside the same terminal that has access to your feature store, your pipelines, your GPU compute, and your data.

The CEO's framing is deliberately aggressive: "The low-code and no-code tooling that dominates other Lakehouses is obsolete."

## The Context-Switching Problem Hopsworks Is Solving

Classic MLOps looks like this: you have a feature store, a pipeline scheduler, a model registry, a training cluster, and a deployment system. You also have Claude Code or Cursor open in a separate window. When you need to build a new pipeline, you switch between your ML platform and your coding agent, copy data schemas, paste error messages, hand-feed context about your data sources, and manually execute whatever the agent suggests.

Every switch costs you minutes and, more importantly, context. The agent doesn't know what's in your feature store. You have to tell it. Every time.

Hopsworks 5.0's thesis is that the right fix is not a better clipboard — it's putting the agent inside the platform where it already has access to everything.

## What Ships in 5.0

**Embedded development container with Claude Code + Codex.** A full terminal lives inside the Hopsworks UI, pre-loaded with both agents. You can run multiple parallel agent sessions, so you can have one building a feature pipeline while another debugs a training job.

**The Wizard.** Select a use-case template (time series forecasting, RAG pipeline, auto-research, and others), and an agent drives the guided setup end-to-end — from ingesting raw data through to a production-ready deployment. Think of it as a project bootstrapper that actually understands your data environment because it has access to it.

**Platform Intelligence.** When you connect an external data source (Databricks, Snowflake, BigQuery, MongoDB, SAP HANA), the platform uses an LLM to automatically generate human-readable column names and descriptions, infer primary keys and event times, and configure ingestion schedules. The result is a feature store that documents itself.

**Native analytics.** SQL via Trino and dashboards via Apache Superset are now built in. The data layer and the analytics layer are the same context for the agent — it can write a pipeline and query its output without switching tools.

**Model registry with Hugging Face imports.** Direct model card imports, GPU/Ray/Spark compute for distributed training.

## Container vs. Wrapper: The Technical Argument

Hopsworks published a companion essay titled ["Don't Be a Wrapper, Be a Container"](https://www.hopsworks.ai/post/coding-agents-inside-data-platforms) that explains the architectural decision. The distinction matters:

**A wrapper** puts an agent around a platform — the agent calls your platform's API the same way any external client would. It's clean but limited: the agent gets only what the API exposes, has to authenticate like any external caller, and can't access the filesystem, environment, or compute resources directly.

**A container** runs the agent *inside* the platform's compute environment. The agent has access to the platform's API keys already loaded, the local filesystem (HopsFS, FUSE-mounted S3), running processes, and platform capabilities — all without you explicitly granting each one. It can do `head feature_store.parquet` or `tail training.log` the same way a developer would.

The practical difference: when you describe "build a time series model on the last 90 days of click data", the agent can read your feature groups, check what's available, generate the pipeline code, run it, inspect the output, and iterate — all inside one execution context, not five tool-calls back across an API.

## Why Hopsworks Chose CLI Over MCP

The essay makes an interesting call: CLI tools outperform Model Context Protocol for this use case. Their reasoning is that coding LLMs have been trained extensively on bash and CLI patterns — they can compose commands, pipe outputs, and use Unix conventions (head/tail filtering, grep for specific fields) to fetch precisely the information they need without bloating the context window.

MCP's strength is standardized tool discovery across heterogeneous systems. CLI's strength is precision access to an already-known local environment. For a platform where the agent lives inside a bounded, well-defined compute context, CLI is faster and less context-expensive.

This is a genuine technical stance worth watching. The MCP ecosystem is growing fast and the July 28 MCP 2026 spec RC may shift this calculus, but Hopsworks's argument that "context window efficiency matters more than interoperability when you're inside a platform" is defensible.

## Air-Gapped and Sovereign Deployments

A sentence from the essay deserves emphasis: "You can launch a coding agent in Hopsworks that uses a LLM that is hosted in Hopsworks — all inside an air-gapped environment."

This is non-trivial. Most coding agent setups require outbound calls to an external model API. If you're in financial services, healthcare, defense, or — relevant after the OpenAI Stargate UK pause — a European enterprise concerned about data residency, a coding agent that never touches an external network is a compliance story that most platforms cannot tell.

Zalando, Europe's largest online retailer, runs its AI infrastructure on Hopsworks. Their case is illustrative: the platform's sovereign AI capability isn't theoretical positioning — there are production workloads running on it in environments where data can't cross certain boundaries.

## Who This Is For

**Data scientists and ML engineers who spend time on pipeline plumbing.** If your job is building features and training models but you burn hours on ingestion configuration, column naming, and pipeline orchestration, the embedded agent with Platform Intelligence is addressing real work. It doesn't replace your judgment on what features to build — it eliminates the boilerplate around building them.

**Enterprise ML teams with sovereignty requirements.** On-premise or private cloud deployments with air-gapped agents are available. If your data can't leave your network, this is a rare option in the coding agent space.

**Teams already running Hopsworks.** The 5.0 upgrade is straightforward if you're on the platform. The Wizard's templates cover common cases (time series, RAG pipeline) and the agent's access to your existing feature groups means it doesn't start from scratch.

## Who Should Skip It

**Teams without ML infrastructure to manage.** If you're building a straightforward LLM application — RAG over documents, a chatbot, an agent with a few tools — you don't need a feature store, a training cluster, or a model registry. Hopsworks is overkill.

**Teams running lean on opex.** Hopsworks is a full ML platform with enterprise deployment options. SaaS registration is open for free tiers, but production use at scale has real infrastructure costs. If your ML footprint is small, the platform's value is in managing complexity you probably don't have yet.

**Teams where MCP interoperability is required.** If your agent needs to communicate across heterogeneous systems using MCP standards, Hopsworks's CLI-first philosophy is a friction point. The platform's agent is designed to work within Hopsworks — not to plug into an external MCP client.

## The Broader Platform Intelligence Trend

Hopsworks 5.0 is one data point in a larger shift: domain-specific platforms embedding coding agents in their native compute environment rather than integrating with external AI assistants. The argument is the same as the wrapper/container essay: agents with direct platform context outperform agents accessing that context over API.

Watch for other ML and data platforms to announce similar embedded agent capabilities in H2 2026. The question isn't whether to embed agents — it's whether your platform gives them enough internal access to be more useful than a coding assistant in a separate window.

---

*ChatForest covers AI developer tooling and ML infrastructure for builders. This article is based on [Hopsworks's press release](https://www.globenewswire.com/news-release/2026/06/30/3319457/0/en/releasing-hopsworks-5-0-introducing-the-coding-data-and-ai-stack.html), their published technical essay ["Don't Be a Wrapper, Be a Container"](https://www.hopsworks.ai/post/coding-agents-inside-data-platforms), and the [Claude Code event page](https://www.hopsworks.ai/events/build-ml-pipelines-with-claude-code-inside-hopsworks). We have no commercial relationship with Hopsworks.*
