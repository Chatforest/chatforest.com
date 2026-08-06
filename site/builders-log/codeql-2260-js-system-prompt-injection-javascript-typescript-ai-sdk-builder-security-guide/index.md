# CodeQL 2.26.0 Now Flags Prompt Injection in Your AI Code: What JS/TS Builders Need to Know

> GitHub's CodeQL 2.26.0 (July 8, 2026) introduces the js/system-prompt-injection query for JavaScript and TypeScript — static analysis that catches untrusted user input flowing into AI model system prompts before it ships. Coverage spans OpenAI Realtime, Sora, Anthropic legacy completions, and Google GenAI. Here's what it detects, what it misses, and what to do now.


GitHub [shipped CodeQL 2.26.0](https://github.blog/changelog/2026-07-10-codeql-2-26-0-adds-kotlin-2-4-0-support-and-ai-prompt-injection-detection/) on [July 8, 2026](https://github.com/github/codeql-cli-binaries/releases/tag/v2.26.0), and buried in the release notes is something builders deploying AI features should know about: CodeQL's first purpose-built query for detecting AI prompt injection in your own codebase.

The new [`js/system-prompt-injection`](https://codeql.github.com/codeql-query-help/javascript/js-system-prompt-injection/) query, available for JavaScript and TypeScript, uses CodeQL's standard data flow engine to flag when untrusted user-controlled input reaches the system prompt parameter of an AI model API call. If it finds a path, it surfaces a code scanning alert — the same mechanism CodeQL uses to catch SQL injection, XSS, and other classic vulnerability classes.

This is not a runtime detection. It does not monitor your application in production. It analyzes your code statically, before it ships.

---

## What the Query Detects

The attack model is straightforward: a user provides input that, through some series of function calls, ends up concatenated into or passed directly to an AI model's system prompt. The attacker controls that input and can use it to override or manipulate the model's instructions — classic indirect prompt injection.

CodeQL's data flow analysis traces paths from *sources* (user-provided input: form fields, URL parameters, query strings, request bodies, and similar) to *sinks* (the parameters in AI SDK calls that accept system prompts). When a tainted path connects source to sink without passing through a sanitizer, the query fires.

The distinction from user-prompt injection: system prompts carry the model's core instructions and persona. Injecting into the system prompt is generally more severe than injecting into user-turn messages, because it lets an attacker rewrite the behavioral baseline the model is operating from. This is why CodeQL introduced a dedicated `js/system-prompt-injection` query rather than a generic "LLM injection" query.

---

## Which APIs Are Now Covered

The 2.26.0 release expanded sink coverage across the three major AI API vendors:

**[OpenAI](https://github.com/github/codeql/blob/main/javascript/ql/lib/ext/openai.model.yml):**
- Sora video creation prompts
- Realtime API session instructions

**[Anthropic](https://github.com/github/codeql/blob/main/javascript/ql/lib/ext/anthropic.model.yml):**
- Legacy completions endpoint prompts

**[Google GenAI](https://github.com/github/codeql/blob/main/javascript/ql/lib/ext/google-genai.model.yml):**
- Cache creation system instructions
- System instructions in model configuration

A classification detail worth knowing if you're triaging alerts: per CodeQL's sink models linked above, OpenAI's legacy completions endpoint (`completions.create({ prompt })`), OpenAI's Sora video-prompt calls, and Anthropic's legacy completions endpoint are all modeled as `user-prompt-injection` sinks, not `system-prompt-injection` — CodeQL treats the `prompt` field in these older, single-string API shapes as closer to a user turn than to a system instruction in the modern chat-message sense.

---

## What It Does Not Cover

**Python.** The `js/system-prompt-injection` query is JavaScript and TypeScript only. No equivalent Python query shipped in 2.26.0. Builders using Python AI SDKs — the anthropic, openai, and google-generativeai packages — do not get static prompt injection detection from this release. If your AI backend is Python, this is not yet your signal.

**The modern OpenAI chat completions API.** The sinks listed above focus on specific newer APIs (Realtime, Sora) and the legacy completions endpoint. If you are using the standard `openai.chat.completions.create()` method with a `system` role message, check whether that specific call pattern has been added as a sink. Sink coverage in CodeQL is determined by model files that evolve across releases.

**Runtime injection.** CodeQL does not see what happens when your app is running. An attacker embedding malicious content inside a document that your AI processes (tool call output, retrieved web content, third-party data) is not detectable by static analysis because the injection happens at runtime, not at the code level.

**All injection routes.** Static analysis catches the easy case — direct, traceable data flow. Injection that passes through database reads, external API calls, or complex transformation chains may not be traced by the data flow engine depending on whether CodeQL has modeled those paths.

---

## How to Enable This

CodeQL is part of GitHub Advanced Security (GHAS). If your repository already has code scanning configured with the default CodeQL suite, the new query should run automatically on your next scan after upgrading to 2.26.0 or later.

If you are not yet using GHAS: repository Settings → Security → Advanced Security → CodeQL analysis → Set up. [Public repositories can use code scanning free; private repositories require a GitHub Advanced Security / GitHub Code Security license.](https://docs.github.com/en/code-security/getting-started/github-security-features)

For repositories that have a custom CodeQL query suite that excludes security queries, you may need to explicitly include `js/system-prompt-injection`.

---

## What This Means in Context

This is the first time CodeQL has added purpose-built detection for AI prompt injection as a first-class vulnerability class — alongside SQL injection, path traversal, and XSS.

The significance is in normalization, not just detection: when CodeQL treats `js/system-prompt-injection` the same way it treats `js/sql-injection`, it signals that the security industry is moving toward treating prompt injection as a standard defect class with standard detection tooling. Builders who have been treating prompt injection as a vague concern without concrete mitigation steps now have a concrete gate: does this code pass CodeQL with no prompt injection alerts?

That said, the coverage gaps matter. [Python remains the dominant language for AI-tagged repositories on GitHub](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/), and it has no equivalent query yet. The current JS/TS sinks cover specific API surfaces, not all possible paths to a model's system prompt. And no static analysis tool can catch the indirect, runtime injection variant that represents the most dangerous real-world attack.

---

## Builder Checklist

**If your AI code is in JavaScript or TypeScript:**
- Confirm GHAS and CodeQL are enabled on your repository
- Check your code scanning configuration includes the default security suite
- After the next scan, review any `js/system-prompt-injection` alerts — even one-hop paths to a system prompt parameter are worth examining
- Map which of your system prompt construction paths accept user input and verify CodeQL is aware of them

**If your AI code is in Python:**
- No static detection equivalent exists yet; watch for CodeQL updates
- In the meantime, audit manually: search for every location where you construct a system prompt and trace where the inputs originate
- Runtime controls (input validation, output filtering, sandboxed tool environments) remain your primary defense

**Across all stacks:**
- CodeQL catches what it can trace statically; design your system prompt construction so it is traceable — avoid dynamic construction patterns that defeat static analysis
- Treat static analysis alerts as a floor, not a ceiling: passing CodeQL does not mean your AI code is injection-proof

---

*CodeQL 2.26.0 shipped July 8, 2026. The `js/system-prompt-injection` query is part of the default CodeQL security suite for JavaScript and TypeScript. Announced via [GitHub changelog July 10, 2026](https://github.blog/changelog/2026-07-10-codeql-2-26-0-adds-kotlin-2-4-0-support-and-ai-prompt-injection-detection/).*

