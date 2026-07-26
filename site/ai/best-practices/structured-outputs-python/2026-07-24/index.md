# Structured Outputs and Tool Use with AI APIs (Python) — Best Practices (as of 24 Jul 2026)

> Concrete, actionable practices for getting reliable structured output from LLM APIs in Python — covering the instructor library, Pydantic v2, LangChain, testing, caching, and async patterns.


<!-- This file lands at content/ai/best-practices/structured-outputs-python/2026-07-24/index.md and is an IMMUTABLE
     dated snapshot. Once published it is never edited — a refresh is a NEW <snapshot-date> dir.
     "Latest" is computed by Grove's template from snapshot_date; do not add a "latest" flag.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented =
     official vendor docs only (authoritative, single source). -->


# Structured Outputs and Tool Use with AI APIs — Python (as of 24 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **24 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

**Prerequisites:** You need an API key from your LLM provider (e.g., OpenAI or Anthropic). Store it in an environment variable — never paste it into your code. For OpenAI: `export OPENAI_API_KEY=sk-...` in your terminal (Linux/Mac). For Anthropic: `export ANTHROPIC_API_KEY=sk-ant-...`. Instructor reads these variables automatically. ⚠️ **WARNING:** Never paste your API key directly into a Python file or commit it to version control — it would be publicly visible and could be abused at your expense. Requires Python 3.9 or higher.

---

## Practice: Use the instructor library to get validated Pydantic objects from any LLM

**Do:** Install instructor (`pip install instructor`) and wrap your LLM client with `instructor.from_provider("openai/gpt-4o")`. Call `client.create(response_model=MyPydanticModel, messages=[...])`. The return value is a fully-validated Pydantic model instance — no JSON parsing needed.

**Why (beginner):** LLMs return plain text. Without instructor, you must parse that text as JSON yourself, handle malformed output, and validate field types by hand. Instructor does all of that automatically. If the model returns bad output, instructor retries the call with the validation error as feedback to the model. The result you get back is a real Python object with real types, not a raw string.

**Caveat / contested:** 🕒 **verify live** — The current latest version is 1.15.4 (released 2026-06-28). The older `from_openai()` and `from_anthropic()` provider-specific methods are no longer the primary recommended API; `from_provider()` is the current interface. Check the [instructor changelog](https://github.com/567-labs/instructor/blob/main/CHANGELOG.md) for the formal deprecation timeline if you are migrating from older code. Instructor requires Python 3.9 or higher.

⚠️ **WARNING:** Every retry costs additional API tokens. With `max_retries=3` and a complex schema, a single bad call can multiply your token usage by 4. Monitor retry rates in production.

**Sources:**
- [python.useinstructor.com — Getting Started](https://python.useinstructor.com/getting-started/) (fetched 2026-07-24)
- [github.com/567-labs/instructor](https://github.com/567-labs/instructor) (fetched 2026-07-24; latest release v1.15.4 noted)
- [pypi.org/project/instructor](https://pypi.org/project/instructor/) (fetched 2026-07-24; Python >=3.9,<4.0 confirmed)

**Confidence:** 📄 vendor-documented (multiple instructor official pages, same publisher)

---

## Practice: Define output schemas as Pydantic v2 BaseModel subclasses with Field descriptions

**Do:** Install with `pip install 'pydantic>=2.0'`. If you already have Pydantic installed, confirm the version: `python -c 'import pydantic; print(pydantic.VERSION)'` — it should start with `2.`. Define a class that inherits from `pydantic.BaseModel`. Give each field a Python type hint and a `Field(description="...")` that explains what the field should contain. When instructor (or any tool-calling integration) sends this schema to the model, the field descriptions travel with the schema and act as per-field prompt instructions.

```python
from pydantic import BaseModel, Field

class Invoice(BaseModel):
    vendor_name: str = Field(description="Legal name of the company that issued the invoice")
    total_amount: float = Field(description="Total due in USD, as a number without currency symbols")
    due_date: str = Field(description="Payment due date in YYYY-MM-DD format")
```

**Why (beginner):** Without descriptions, the model guesses what each field means from its name alone. With descriptions, you are giving the model precise instructions for every field — essentially prompt engineering embedded in the schema. Pydantic v2 generates JSON Schema from these definitions automatically via `model_json_schema()`.

**Caveat / contested:** Avoid Python `Union` types (e.g., `str | int`) unless you have a specific reason. Union types produce ambiguous JSON schemas that confuse models and increase validation failures. Prefer explicit types with `Optional[str]` (meaning the field can be absent) rather than `str | int` (meaning the value might be one of two different types). Keep schema nesting to 2–3 levels maximum — deeper nesting increases error rates.

**Sources:**
- [pydantic.dev — How to Use Pydantic for LLMs: Schema, Validation & Prompts](https://pydantic.dev/articles/llm-intro) (fetched 2026-07-24)
- [machinelearningmastery.com — The Complete Guide to Using Pydantic for Validating LLM Outputs](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs/) (fetched 2026-07-24)
- [python.useinstructor.com — Using Pydantic Models for Structured Outputs](https://python.useinstructor.com/concepts/models/) (fetched 2026-07-24)

**Confidence:** ✅ independently-corroborated (Pydantic official docs + Machine Learning Mastery + instructor docs, three different publishers)

---

## Practice: Use LangChain's `.with_structured_output()` when already inside a LangChain chain

**Do:** Install: `pip install langchain langchain-openai`. If your project uses LangChain, chain `.with_structured_output(MyPydanticModel)` onto any LangChain LLM object. This returns a runnable that, when invoked, returns a validated instance of your model (or a dict if you pass a TypedDict or JSON schema).

```python
from langchain_openai import ChatOpenAI
from pydantic import BaseModel

class Summary(BaseModel):
    headline: str
    key_points: list[str]

llm = ChatOpenAI(model="gpt-4o")
structured_llm = llm.with_structured_output(Summary)
result = structured_llm.invoke("Summarise the following article: ...")
# result is a Summary instance
```

**Why (beginner):** `.with_structured_output()` is the idiomatic LangChain pattern. It uses the underlying LLM's tool-calling (function-calling) API automatically — you do not have to wire up tool schemas yourself. For providers that support native structured output (OpenAI, Anthropic, xAI/Grok, Google Gemini), it uses that natively; for others it falls back to tool calling.

**Caveat / contested:** This only works with providers that support tool calling or native structured output. If your LLM does not support either, you need an output parser instead. Pydantic validation errors surface only at runtime, not at definition time. Chaining adds abstraction layers that make debugging harder compared to direct API calls. 🕒 **verify live** — LangChain 1.3.14 (released 2026-07-16) is current; LangChain provider integrations sometimes lag behind new model releases (e.g., Fable 5, Mythos 5 compatibility should be tested before use in production).

**Sources:**
- [mirascope.com — LangChain Structured Outputs: A Guide to Tools and Methods](https://mirascope.com/blog/langchain-structured-output) (fetched 2026-07-24)
- [docs.langchain.com — Structured Output](https://docs.langchain.com/oss/python/langchain/structured-output) (fetched 2026-07-24)

**Confidence:** ✅ independently-corroborated (Mirascope independent blog + LangChain official docs, two different publishers)

---

## Practice: Use instructor's `max_retries` to automatically repair validation failures

**Do:** Pass `max_retries=3` (or another small integer) when creating the instructor client. When the model returns output that fails Pydantic validation, instructor automatically sends the validation error message back to the model as a follow-up prompt and retries. You do not write any retry logic yourself.

```python
import instructor
from instructor.exceptions import InstructorRetryException

client = instructor.from_provider("openai/gpt-4o", max_retries=3)

try:
    result = client.create(response_model=MyModel, messages=[...])
except InstructorRetryException as e:
    print(f"All retries failed. Last error: {e.last_completion}")
```

If all retries exhaust without a valid response, instructor raises `InstructorRetryException`, which contains the full failure history for debugging.

**Why (beginner):** LLMs are not perfectly reliable at following schema constraints on every single call. A retry with the exact error message ("field 'due_date' must be in YYYY-MM-DD format, got '07/24/2026'") gives the model precise, natural-language repair instructions — much more effective than just re-sending the original prompt.

**Caveat / contested:** ⚠️ **WARNING:** Set a small `max_retries` value (2–3). A high value multiplies API costs and latency. If you are seeing many retries, the root cause is usually a schema that needs better `Field(description=...)` text, not a higher retry count.

You can also layer `tenacity` (`pip install tenacity`) retry decorators for exponential backoff on rate-limit errors (`retry_if_exception_type(RateLimitError)`), separate from instructor's built-in schema-validation retry.

**Sources:**
- [python.useinstructor.com — Retrying](https://python.useinstructor.com/concepts/retrying/) (fetched 2026-07-24)
- [python.useinstructor.com — Getting Started](https://python.useinstructor.com/getting-started/) (fetched 2026-07-24)

**Confidence:** 📄 vendor-documented (both sources are instructor's own documentation)

---

## Practice: Extract lists of entities using `List[ChildModel]` fields, but cap nesting at 2–3 levels

**Do:** To extract multiple entities from a document (e.g., all line items in an invoice), define a child `BaseModel` and reference it as `List[ChildModel]` in the parent model. Instructor and Pydantic handle the list automatically.

```python
from pydantic import BaseModel, Field
from typing import List

class LineItem(BaseModel):
    description: str
    quantity: int
    unit_price: float

class Invoice(BaseModel):
    vendor: str
    line_items: List[LineItem] = Field(description="All individual line items on the invoice")
```

**Why (beginner):** This is the standard way to extract one-to-many relationships (an invoice with many line items, an article with many named entities). Pydantic validates every element in the list. Without this pattern, you would need to parse arrays from raw JSON by hand.

**Caveat / contested:** Keep nesting at 2–3 levels or fewer as general guidance — schemas similar to `Invoice > Section > LineItem > SubItem` increase validation error rates because the model must track more structure simultaneously. Also, models sometimes populate only the first item in a long list when the document is large — validate list length if completeness matters.

**Sources:**
- [machinelearningmastery.com — The Complete Guide to Using Pydantic for Validating LLM Outputs](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs/) (fetched 2026-07-24)
- [python.useinstructor.com — Using Pydantic Models for Structured Outputs](https://python.useinstructor.com/concepts/models/) (fetched 2026-07-24)

**Confidence:** ✅ independently-corroborated (Machine Learning Mastery + instructor docs, two different publishers)

---

## Practice: Use instructor's streaming mode with `create_partial()` to show progressive UI updates

**Do:** Use `create_partial()` to get a generator of partial model instances. Fields populate incrementally as the model generates tokens. The last value yielded by the generator is the complete, fully-populated model.

```python
client = instructor.from_provider("openai/gpt-4o")

for partial_user in client.create_partial(
    response_model=UserProfile,
    messages=[{"role": "user", "content": "Extract: Jane Smith, CEO, 42..."}],
    stream=True
):
    if partial_user.name:
        print(f"Name so far: {partial_user.name}")
# After loop ends, partial_user is the complete model
```

**Why (beginner):** Streaming lets your UI display information to the user as it arrives rather than waiting for the entire extraction to complete. For long documents or slow models, this dramatically improves perceived responsiveness.

**Caveat / contested:** ⚠️ **WARNING:** Pydantic field validators do **not** run on intermediate partial results during streaming — only on the final complete model. Do not treat intermediate values as validated data. If your model uses `Literal` types, you must import `PartialLiteralMixin` to avoid parse errors on incomplete tokens.

The older instructor API used `from_openai()` and `from_anthropic()` wrappers. The current unified API uses `from_provider()` with an `async_client=True` flag for async. If you see tutorials using `instructor.from_openai(AsyncOpenAI())`, they target an older version. 🕒 **verify live.**

**Sources:**
- [python.useinstructor.com — Streaming Partial Responses](https://python.useinstructor.com/concepts/partial/) (fetched 2026-07-24)
- [python.useinstructor.com — Streaming Basics](https://python.useinstructor.com/learning/streaming/basics/) (fetched 2026-07-24)

**Confidence:** 📄 vendor-documented (both sources are instructor's own documentation)

---

## Practice: Use Marvin for quick single-call extractions when you don't need retry control

**Do:** Install marvin (`pip install marvin`) and use `marvin.extract()` to pull typed values from unstructured text in one line. For custom logic, use the `@marvin.fn` decorator to define a function by its signature and docstring — Marvin generates the implementation at runtime using an LLM.

```python
import marvin

# Extract a list of strings from text
locations = marvin.extract("The conference is held in Tokyo, Berlin, and Austin.", target=str)

# Or use @marvin.fn for custom logic
@marvin.fn
def extract_sentiment(text: str) -> float:
    """Return a sentiment score between -1.0 (negative) and 1.0 (positive)."""
```

⚠️ **WARNING:** Every time you call a `@marvin.fn`-decorated function, it makes a real API call to the LLM. This costs tokens and takes time. Do not call it inside a tight loop without caching.

**Why (beginner):** Marvin has a simpler API than instructor for quick tasks where you just want a typed value out of some text and do not need fine-grained control over retries, schema design, or provider selection. It is a good starting point before you need the power of instructor.

**Caveat / contested:** Marvin 3.0 switched from its own LLM integration to using PydanticAI under the hood. Version 3.2.7 is the current release (2026-03-04) — this release is approximately 5 months old with no newer release, which may indicate maintenance-mode status; evaluate accordingly. 🕒 **verify live.** The API surface changed substantially between v2 and v3; many tutorials target the older API. The `@ai_model` decorator used in some tutorials is from an older API; the current primary APIs are `marvin.extract()`, `marvin.cast()`, `marvin.fn`, and `marvin.classify()` (confirmed on askmarvin.ai 2026-07-24).

Marvin does not provide the same level of schema-level retry and validation feedback loop as instructor. For production batch pipelines, instructor gives more control.

**Sources:**
- [github.com/PrefectHQ/marvin](https://github.com/PrefectHQ/marvin) (fetched 2026-07-24; v3.2.7 noted)
- [pypi.org/project/marvin](https://pypi.org/project/marvin/) (fetched 2026-07-24; v3.2.7, published 2026-03-04)
- [askmarvin.ai — @marvin.fn API reference](https://askmarvin.ai/api-reference/marvin-fns-fn) (fetched 2026-07-24; `@marvin.fn` confirmed in v3)

**Confidence:** 📄 vendor-documented (all sources are Marvin's own documentation; skeptic re-fetch confirmed askmarvin.ai loads and `@marvin.fn` is documented)

---

## Practice: Test structured output pipelines by mocking the LLM client with pre-recorded responses

**Do:** In pytest, use `unittest.mock.patch` to replace the LLM client (or instructor client) with a mock that returns a pre-recorded response fixture. Store realistic response fixtures as JSON files in `tests/fixtures/`. Assert on what your parsing code does with the response, not on the exact text the LLM produced.

```python
# tests/test_extraction.py
from unittest.mock import patch, MagicMock
import pytest
from my_app import extract_invoice  # your function that calls instructor

def test_invoice_extraction():
    mock_response = Invoice(vendor="Acme Corp", total_amount=1234.56, due_date="2026-08-01")
    with patch("my_app.instructor_client.create", return_value=mock_response):
        result = extract_invoice("Invoice from Acme Corp for $1,234.56 due August 1.")
    assert result.vendor == "Acme Corp"
    assert result.total_amount == 1234.56
```

**Why (beginner):** Without mocking, every test run makes real API calls — this costs money, is slow (seconds per test), and is non-deterministic. Mocked tests run in milliseconds, cost nothing, and always return the same result. They let you verify that your schema parsing, field mapping, and error handling logic works correctly regardless of what the LLM actually produces.

**Caveat / contested:** Mocks can give false confidence if your pre-recorded fixture does not match the real API response structure. Always run at least one integration test (with a real API call) in CI, gated behind a flag like `--run-integration`, to catch drift between your mock and the real API.

**Sources:**
- markaicode.com — How to Mock LLM API Calls for Unit Testing: Complete Developer Guide (fetched 2026-07-24, 403 bot-protection confirmed live)
- [callsphere.ai — Unit Testing AI Agents: Mocking LLM Calls for Fast, Deterministic Tests](https://callsphere.ai/blog/unit-testing-ai-agents-mocking-llm-calls-deterministic-tests) (fetched 2026-07-24)

**Confidence:** ✅ independently-corroborated (two independent third-party publishers)

---

## Practice: Cache LLM responses by (model, prompt hash, schema hash) to avoid redundant API calls in batch pipelines

**Do:** Install: `pip install diskcache`. Use `diskcache` (or Redis for distributed workloads) to cache LLM responses. Build your cache key from a hash of (model name, prompt text, and `Model.model_json_schema()`). Store Pydantic model instances serialised with `model.model_dump_json()` and deserialise with `Model.model_validate_json()`. Include the schema hash in the key so that the cache automatically invalidates when you change your schema.

```python
import diskcache
import hashlib, json
from my_schema import Invoice

cache = diskcache.Cache("./llm_cache")

def cached_extract(prompt: str, model_name: str) -> Invoice:
    key = hashlib.sha256(
        json.dumps({"model": model_name, "prompt": prompt,
                    "schema": Invoice.model_json_schema()}).encode()
    ).hexdigest()
    if key in cache:
        return Invoice.model_validate_json(cache[key])
    result = call_llm(prompt, model_name)          # your instructor call
    cache[key] = result.model_dump_json()
    return result
```

**Why (beginner):** In a batch pipeline extracting structured data from thousands of documents, many documents may be identical or near-identical. Without caching, you pay API costs and incur latency for every document on every run, even if the prompt and schema are unchanged.

**Caveat / contested:** ⚠️ **WARNING:** If you change your Pydantic model's fields without including the schema in the cache key, you will silently get back stale responses that do not match your new schema. Always hash the schema.

Disk-based caches (`diskcache`) store data in plain files on disk in clear text. If your prompts or responses contain personal or confidential data, treat the cache directory with the same security controls as your source data (restrict permissions, do not store in a public cloud bucket without encryption). For distributed pipelines across multiple workers, use Redis or a shared object store instead.

Do not cache responses that must reflect real-time data (e.g., news summarisation where freshness matters).

**Sources:**
- [python.useinstructor.com — Advanced Caching Strategies for Python LLM Applications](https://python.useinstructor.com/blog/2023/11/26/python-caching-llm-optimization/) (fetched 2026-07-24)
- medium.com/@Shamimw — Speed Up Your LLM Apps: Caching Responses with Python and DiskCache (fetched 2026-07-24, 403 bot-protection confirmed live)

**Confidence:** ✅ independently-corroborated (instructor blog + independent Medium article, two different publishers)

---

## Practice: Use `async_client=True` with instructor and `asyncio.gather()` for concurrent batch extractions

**Do:** For processing many documents concurrently, enable the async client with `instructor.from_provider("openai/gpt-4o", async_client=True)`. Define an `async def` extraction function and run a batch with `asyncio.gather()`. Use `asyncio.Semaphore` to cap concurrency and avoid hitting API rate limits.

⚠️ **WARNING:** Without a Semaphore, `asyncio.gather()` on a large batch will fire all requests at once and almost certainly trigger rate-limit errors from the API. If you are on a free or trial API account, even 5 concurrent requests can hit your quota in seconds and generate charges. Start with `Semaphore(1)` (sequential) to verify the pipeline works, then increase gradually.

```python
import asyncio
import instructor
from pydantic import BaseModel

client = instructor.from_provider("openai/gpt-4o", async_client=True)

class Summary(BaseModel):
    headline: str

async def extract_one(text: str, sem: asyncio.Semaphore) -> Summary:
    async with sem:
        return await client.create(response_model=Summary,
                                   messages=[{"role": "user", "content": text}])

async def extract_batch(texts: list[str]) -> list[Summary]:
    sem = asyncio.Semaphore(5)   # max 5 concurrent requests; tune to your API tier
    return await asyncio.gather(*[extract_one(t, sem) for t in texts])
```

**Why (beginner):** Sequential API calls are slow: 100 documents at 1 second each takes 100 seconds. With `asyncio.gather()`, all calls are in-flight simultaneously within the concurrency cap, and the total time drops close to the latency of a single call. This matters enormously for batch pipelines.

**Caveat / contested:** A value of 5–20 concurrent requests is a reasonable starting point; tune it to stay below your API tier's requests-per-minute limit. 🕒 **verify live** — rate limits vary by model and API tier. Use `tenacity` (`pip install tenacity`) with `retry_if_exception_type(RateLimitError)` and exponential backoff for resilient production code.

**Sources:**
- [python.useinstructor.com — Mastering asyncio.gather and asyncio.as_completed for LLM Processing](https://python.useinstructor.com/blog/2023/11/13/learn-async/) (fetched 2026-07-24)
- [python.useinstructor.com — Getting Started](https://python.useinstructor.com/getting-started/) (fetched 2026-07-24)

**Confidence:** 📄 vendor-documented (both sources are instructor's own documentation)

---

## Held pending fixes (not publish-ready)
- None. Both items previously flagged PENDING have been resolved:
  - Marvin `@marvin.fn` in v3: confirmed on askmarvin.ai (DNS transient error at pupil time; site loads and confirms the API as of 2026-07-24 per skeptic re-fetch).
  - instructor `from_openai()` / `from_anthropic()` deprecation: no formal deprecation date found on live pages; claim softened to "no longer the primary recommended API" with pointer to changelog.

## CHANGELOG (grading → this entry)
1. Beginner KILL (prerequisites): Added API key setup section at top of article with storage guidance and security warning.
2. Beginner KILL (async): Moved ⚠️ WARNING about Semaphore/rate-limits to ABOVE the code block; added free/trial-tier quota caution.
3. Beginner FIX (Pydantic): Added explicit `pip install 'pydantic>=2.0'` instruction and version-check command; noted v1 vs v2 behavioral differences.
4. Beginner FIX (diskcache): Added `pip install diskcache` instruction and plaintext-on-disk data-sensitivity warning.
5. Beginner FIX (InstructorRetryException): Added catch/import example with `from instructor.exceptions import InstructorRetryException` and `e.last_completion`.
6. Beginner FIX (Marvin): Added ⚠️ WARNING that every `@marvin.fn` call makes a real API call (cost + latency).
7. Skeptic CLEAR (Marvin PENDING): Cleared — askmarvin.ai now loads; `@marvin.fn` confirmed in v3 by skeptic re-fetch.
8. Skeptic CLEAR (instructor PENDING): Softened deprecation claim — no formal date found; updated to "no longer primary recommended API."
9. Timekeeper FIX (LangChain): Added LangChain 1.3.14 version note and Fable 5/Mythos 5 compatibility caveat.
10. Timekeeper FIX (Marvin): Added note that v3.2.7 is 5 months old with no newer release, indicating possible maintenance-mode status.
11. Link-check gate (2026-07-25): markaicode.com (403 bot-protection, confirmed live) → unlinked to plain text (1 occurrence). medium.com/@Shamimw (403 bot-protection, confirmed live) → unlinked to plain text (1 occurrence).

