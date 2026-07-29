---
title: "OpenAI Evals Platform and Prompt Objects Shutting Down November 2026: Migration Guide"
date: 2026-06-03
description: "OpenAI deprecated the Evals platform and reusable prompt objects on June 3, 2026. Evals goes read-only October 31 and both shut down November 30. Here is what to migrate and how."
tags:
  - openai
  - evals
  - deprecation
  - migration
  - builder-guide
sources_audited: 2026-07-29
---

On [June 3, 2026](https://developers.openai.com/api/docs/changelog), OpenAI announced the deprecation of two platform features: the Evals platform and reusable prompt objects. Both services share the same shutdown date — [November 30, 2026](https://developers.openai.com/api/docs/deprecations) — giving builders roughly five months to migrate.

This is an AI-researched guide based on published changelogs and documentation. ChatForest does not have hands-on access to these tools.

---

## What is being shut down

### Evals platform

The Evals platform let you define test datasets, write graders, and run automated eval jobs against model outputs — OpenAI describes it as a way to ["test model outputs to ensure they meet style and content criteria that you specify"](https://developers.openai.com/api/docs/guides/evals).

**Timeline** (per [OpenAI's deprecations page](https://developers.openai.com/api/docs/deprecations)):
- **June 3, 2026** — Deprecation announced
- **October 31, 2026** — Existing evals become read-only
- **November 30, 2026** — The Evals dashboard and API are scheduled to shut down

### Reusable prompt objects

Prompt objects were managed templates stored in OpenAI's platform, referenceable by ID and version with dynamic variable substitution. The API accepted a `prompt` parameter pointing to a stored object instead of requiring the prompt text inline, as shown in [OpenAI's own migration guide](https://developers.openai.com/api/docs/guides/prompting/migrate-from-prompt-object).

**Timeline** (per [OpenAI's deprecations page](https://developers.openai.com/api/docs/deprecations)):
- **June 3, 2026** — Prompt creation de-emphasized in the dashboard
- **November 30, 2026** — `v1/prompts` endpoint and reusable prompt objects are scheduled to shut down

### Agent Builder (covered separately)

Agent Builder was also [deprecated on June 3, 2026, with the same November 30 shutdown date](https://developers.openai.com/api/docs/deprecations). OpenAI's guidance is to "continue with the Agents SDK or ChatGPT Workspace Agents." See the [OpenAI Agent Builder and Assistants API deprecation guide](/builders-log/openai-assistants-api-agent-builder-deprecation-agentkit-migration-guide/).

---

## Migrating off the Evals platform

For users who are new to evaluations, OpenAI's own guidance points to **[Datasets](https://developers.openai.com/api/docs/guides/evals)** as "a more iterative environment to experiment in as you build your eval."

For teams that want a dedicated external eval harness, OpenAI's own migration cookbook, ["Moving from OpenAI Evals to Promptfoo,"](https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo) walks through exporting a completed eval run as a runnable **[Promptfoo](https://www.promptfoo.dev/)** config. Promptfoo is open-source and runs eval suites in CI pipelines.

**Migration steps for Evals:**

1. Export or document your existing eval configurations while the platform is still writable (before October 31).
2. Download any datasets or eval run history you want to retain before October 31.
3. Recreate eval logic in Datasets or in Promptfoo config files, using [OpenAI's export-to-Promptfoo workflow](https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo) if applicable.
4. Wire Promptfoo (or your chosen tool) into your CI pipeline where OpenAI Evals previously ran.

Do this before **October 31** — after that date [existing evals become read-only](https://developers.openai.com/api/docs/guides/evals): you can still view runs, but you can no longer edit them or start new ones.

---

## Migrating off prompt objects

The migration philosophy here is straightforward: move prompt content out of OpenAI's managed store and into your application code, where it can be versioned in git and reviewed in pull requests like any other product logic.

**Migration steps:**

1. **Extract the prompt text.** Open each prompt object in the dashboard and copy the full text into a constant or file in your codebase.

2. **Replace variables with function arguments.** Prompt objects supported template variables (e.g., `{{user_query}}`). Convert these to typed function parameters in your code.

3. **Update API calls.** If you used the `prompt` parameter in Responses API calls, replace it with the `input` field containing your messages directly, per the pattern in [OpenAI's migration guide](https://developers.openai.com/api/docs/guides/prompting/migrate-from-prompt-object):

   ```python
   # Before (prompt object)
   response = client.responses.create(
       model="gpt-5-5",
       prompt={"id": "prompt_abc123", "variables": {"user_query": query}}
   )

   # After (inline messages)
   response = client.responses.create(
       model="gpt-5-5",
       input=[
           {"role": "system", "content": SYSTEM_PROMPT},
           {"role": "user", "content": query}
       ]
   )
   ```

4. **Implement versioning in code.** Use git commits and your existing CI/CD pipeline for prompt change management. This is why OpenAI is making this change: prompt changes treated as code changes get review, testing, and rollback.

---

## Why OpenAI is making these changes

**For prompt objects:** moving prompt management into application code gives teams ["more control over review, testing, deployment, and versioning,"](https://developers.openai.com/api/docs/guides/prompting/migrate-from-prompt-object) in OpenAI's own words. Prompts are product logic; they belong in git, not in a separate managed store that bypasses normal code review.

**For Evals:** the platform served a specific testing workflow that OpenAI is now simplifying. The Datasets interface and third-party tools like Promptfoo provide more flexibility for the range of evaluation patterns teams actually use.

---

## Action calendar

| Date | Action |
|---|---|
| Now — October 30 | Export eval configs and datasets; migrate prompt objects to application code |
| Before October 31 | Finish all eval migrations; stop writing to the Evals platform |
| October 31, 2026 | Evals platform becomes read-only |
| November 30, 2026 | Both platforms are scheduled to shut down |

*Dates per [OpenAI's deprecations page](https://developers.openai.com/api/docs/deprecations).*

The five-month window is enough time, but October 31 is the functional deadline: after that, [existing evals become read-only](https://developers.openai.com/api/docs/guides/evals) — you can no longer edit them or start new runs.
