---
title: "AI Agent Supply Chain Verification — Python (as of 13 Jul 2026)"
date: 2026-07-13
snapshot_date: 2026-07-13
topic: ai-agent-supply-chain-python
track: best-practices
audience: "technically comfortable readers"
description: "Practices for verifying the integrity and provenance of Python packages used in AI agent pipelines: hash pinning, lock files, vulnerability scanning, SBOM generation, typosquatting defenses, private indexes, and CVE monitoring for AI libraries."
content_type: "Best Practice"
categories: ["Python", "Supply Chain Security", "AI Agents"]
tags: ["python", "pip", "uv", "poetry", "pypi", "sbom", "supply-chain", "cve", "sigstore"]
last_refreshed: 2026-07-13
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-13"
grading_result: "0 fabrications; 12 corrections applied; 0 gaps filed as project-33 issues"
---

<!-- This file lands at content/ai/best-practices/ai-agent-supply-chain-python/2026-07-13/index.md and is
     an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a NEW snapshot-date dir.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented = official
     vendor docs only (authoritative, single source). -->

# AI Agent Supply Chain Verification — Python (as of 13 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **13 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

AI agent pipelines typically pull dozens of third-party Python packages — ML frameworks, orchestration libraries, and SDK wrappers — each of which is an attack surface. Supply chain attacks on PyPI (typosquatting, account takeover, dependency confusion, and LLM-hallucinated "slopsquatting" package names) have been documented in real incidents targeting torch, transformers, langchain, and litellm. The practices below layer defenses across install time, CI, and runtime to reduce that risk.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Pin every dependency with cryptographic hashes

**Do:** Commit a lock file that records SHA-256 hashes for every direct and transitive package. With **uv**, run `uv lock`; hashes are stored in `uv.lock` automatically. With **Poetry**, commit `poetry.lock` — hashes are included by default. With plain **pip**, generate a hashed requirements file: `pip-compile --generate-hashes requirements.in -o requirements.txt`, then install with `pip install --require-hashes -r requirements.txt`. Never leave `--require-hashes` off in production deploys.

**Why:** A version number alone (`requests==2.32.3`) does not guarantee you get the file you expect — an attacker who compromises a mirror or CDN cache can serve a different file with the same version number. A cryptographic hash makes a swap detectable at install time: pip, Poetry, and uv will all refuse to install a file whose hash does not match.

**Caveat / contested:** Hash pinning stops tampering *after* the lock file was generated, but it will not protect you from a malicious package that was already present on PyPI when you first resolved. You still need vulnerability scanning and a cooldown period. Also, `--require-hashes` in pip mode is "all-or-nothing" — every entry in the requirements file must include a hash, so mixing pinned and unpinned entries will fail.

⚠️ **WARNING:** `pip install --extra-index-url <private-url>` does **not** isolate your install to the private index — pip still checks public PyPI and will install the highest-version package it finds across both indexes (CVE-2018-20225). This is a dangerous default for AI teams who think they are isolated. See the private-index practice below.

**Sources:** [pip.pypa.io — Secure installs](https://pip.pypa.io/en/stable/topics/secure-installs/) (fetched 2026-07-13) · [pydevtools.com — Pin dependencies with hashes in uv](https://pydevtools.com/handbook/how-to/how-to-pin-dependencies-with-hashes-in-uv/) (fetched 2026-07-13) · [lucasgabrielb.com — Protecting Python projects against supply chain attacks](https://lucasgabrielb.com/en/posts/protecting-your-python-projects-against-supply-chain-attacks/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (pip official docs + two independent developer guides)

---

## Practice: Run pip-audit (or uv audit) in CI on every pull request

**Prerequisite:** Install pip-audit first: `pip install pip-audit` (current version: 2.10.1, released 2026-06-10). For uv-based projects, `uv audit` is built-in but is currently in **preview / unstable** — breaking changes are possible; verify against your installed uv version before relying on it in CI.

**Do:** Add a vulnerability scanning step to every CI run. With pip-audit: `pip-audit -r requirements.txt --strict --format json -o audit.json`. With uv: `uv audit`. Both query the OSV database (which aggregates PyPI Advisory Database, GitHub Advisory Database, and NVD) and flag known CVEs. Gate the build on fixable findings only to avoid blocking on advisories with no upstream fix:

```bash
jq -e '[.vulnerabilities[] | select(.fix_versions | length > 0)] | length == 0' audit.json
```

For unfixable findings, record a time-boxed suppression (no longer than 90 days) with a documented reason rather than an open-ended ignore.

**Why:** AI projects depend on rapidly evolving libraries — langchain-core had a critical deserialization flaw (CVE-2025-68664, CVSS 9.3 GitHub CNA / 8.2 NVD) disclosed December 2025 that allowed exfiltration of API keys. Running a scanner on every PR means the pipeline rejects a merge before a vulnerable library ships to production.

**Caveat / contested:** pip-audit is "not a static code analyzer" and cannot detect malicious packages that have no CVE advisory yet (zero-days, newly uploaded malware). Combine with `UV_MALWARE_CHECK=1` (see next practice) and a cooldown window. Safety CLI overlaps with pip-audit on some advisories and occasionally catches findings the other misses, so running both quarterly is reasonable but not required daily.

**Sources:** [pypi.org/project/pip-audit](https://pypi.org/project/pip-audit/) (fetched 2026-07-13) · [stackharbor.com — Python pip-audit and Safety](https://stackharbor.com/en/knowledge-base/python-pip-audit-safety/) (fetched 2026-07-13) · [cyata.ai — CVE-2025-68664](https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (PyPI official project page + two independent guides + CVE incident report)

---

## Practice: Use uv's install-cooldown and malware-check to block brand-new malicious packages

**Do:** In `pyproject.toml` or `uv.toml`, set a rolling exclusion window so uv ignores packages published in the last 7 days:

```toml
[tool.uv]
exclude-newer = "7 days"
```

This friendly-duration syntax (`"7 days"`, `"1 week"`) requires uv 0.9.17 or later (PR #16814 merged December 2025). **Note:** `UV_EXCLUDE_NEWER` env var does NOT yet support duration strings — only TOML/CLI flags do. Also enable the OSV malware advisory check in CI:

```yaml
- name: Sync dependencies
  run: uv sync --locked
  env:
    UV_MALWARE_CHECK: "1"
```

`UV_MALWARE_CHECK` requires uv ≥ 0.11.16 and is currently in **preview / unstable** — verify it is available in your uv version. For packages that need urgent patches before the cooldown expires, add a per-package override: `exclude-newer-package = { critical-fix-pkg = false }` (note: this option has known edge-case bugs in active uv issues — 🕒 verify live).

**Why:** Most malicious packages uploaded to PyPI are detected and removed within 24–72 hours. A 7-day cooldown means your project never installs a package that appeared on PyPI in the last week unless you explicitly override it. `UV_MALWARE_CHECK=1` provides a second layer: during `uv sync`, uv looks up every locked package against the MAL-prefixed advisories in the OSV database and refuses to install flagged ones.

**Caveat / contested:** The cooldown has a real cost: it delays security patches by up to 7 days. Teams with strict SLAs on vulnerability remediation should use 1–2 days rather than 7. The malware check only catches packages already in the OSV database — a newly uploaded, yet-to-be-reported malicious package will still pass. **OpenAI acquired Astral (uv's maintainer) on March 19, 2026;** Astral's founder publicly committed to keeping uv and ruff open source under MIT/Apache 2.0, but regulatory approval is still pending as of mid-2026 — verify the project's open-source status if this concerns your organization's supply-chain policy.

**Sources:** [pydevtools.com — Protect against Python supply chain attacks with uv](https://pydevtools.com/handbook/how-to/how-to-protect-against-python-supply-chain-attacks-with-uv/) (fetched 2026-07-13) · [byteiota.com — uv audit Python supply chain defense](https://byteiota.com/uv-audit-python-supply-chain-defense/) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13) · openai.com — OpenAI to acquire Astral (fetched 2026-07-13; URL confirmed live via search but returns 403 to automated checks — unlinked per gate policy)

**Confidence:** ✅ independently-corroborated (two independent guides plus the defence-in-depth article; acquisition fact from OpenAI official announcement)

---

## Practice: Use PyPI Trusted Publishing and Sigstore attestations when you publish packages

**Do:** If your AI team publishes internal libraries to PyPI or a private index, replace long-lived API tokens with Trusted Publishing. In the PyPI project settings, register your GitHub repository and workflow as a Trusted Publisher. In the workflow, add `permissions: id-token: write` and use the `pypa/gh-action-pypi-publish` action — it now generates Sigstore-based attestations by default (via PEP 740) with no extra steps. Short-lived OIDC tokens replace stored API tokens; they expire in 15 minutes.

**Why:** Long-lived API tokens are the #1 mechanism for supply chain takeover via CI secret theft (the Ultralytics and GhostAction incidents both exploited stolen tokens). An OIDC token that expires in 15 minutes is useless to an attacker who finds it in a leaked log file. Sigstore attestations cryptographically bind the published artifact to the exact repository and workflow run that produced it, so downstream consumers can verify provenance.

**Caveat / contested:** As of mid-2026, downstream verification (having `pip` or `uv` automatically check attestations at install time) is not yet universally enforced — 🕒 verify live against pip/uv changelogs for your installed version. Attestations provide transparency and auditability now, but automated consumer-side enforcement remains in progress. Attestations also cannot detect malicious code introduced *before* the build; they only prove the package was built from a claimed repo.

**Sources:** [docs.pypi.org — Trusted Publishers](https://docs.pypi.org/trusted-publishers/) (fetched 2026-07-13) · [docs.pypi.org — Attestations security model](https://docs.pypi.org/attestations/security-model/) (fetched 2026-07-13) · [blog.trailofbits.com — Attestations: a new generation of signatures on PyPI](https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/) (fetched 2026-07-13) · [blog.sigstore.dev — PyPI attestations GA](https://blog.sigstore.dev/pypi-attestations-ga/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (two official PyPI docs pages as one vendor source; Trail of Bits blog; Sigstore GA post co-authored by Trail of Bits and two Google engineers — partial author overlap noted; label reflects two distinct organizations)

---

## Practice: Generate an SBOM at build time to enable rapid CVE triage

**Do:** Add a CycloneDX SBOM (Software Bill of Materials) generation step to your CI pipeline immediately after installing dependencies:

```bash
pip install cyclonedx-bom   # current version: 7.3.0 — 🕒 verify live
cyclonedx-py environment -o sbom.cdx.json --of json
```

For Poetry projects use `cyclonedx-py poetry`; for Pipenv use `cyclonedx-py pipenv`. Commit or publish the SBOM artifact alongside each release. Use `pip-audit --format cyclonedx-json` to merge vulnerability findings into the same format.

**Why:** When a critical vulnerability drops in a library like langchain or torch, the first question is "are we affected?" Without an SBOM, answering that requires manually checking every deployed environment. With an SBOM, you query a machine-readable inventory in minutes.

**Caveat / contested:** An SBOM records what was installed, not what is actually *called* at runtime. You may be vulnerable to a CVE in a transitive dependency that your code never exercises — the SBOM will flag it, but the real risk is lower than it appears. SBOM formats (CycloneDX vs SPDX) are not yet universally interoperable, so choose one and stick to it per project.

**Sources:** [pypi.org/project/cyclonedx-bom](https://pypi.org/project/cyclonedx-bom/) (fetched 2026-07-13) · [github.com/CycloneDX/cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) (fetched 2026-07-13) · [openssf.org — Choosing an SBOM generation tool](https://openssf.org/blog/2025/06/05/choosing-an-sbom-generation-tool/) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (PyPI + GitHub repo as one vendor source; OpenSSF blog + bernat.tech as two independent publishers)

---

## Practice: Defend against typosquatting and slopsquatting before you pip install anything

**Do:** Before installing any new Python package into an AI agent project, perform three checks: (1) Verify the exact package name against official documentation or the project's GitHub page — never copy-paste a package name from AI-generated code without checking it on [pypi.org](https://pypi.org). (2) Check the package's creation date, download count, and owner on PyPI — a package registered last week with zero history for a popular-sounding name is a red flag. (3) Use `pip install --dry-run` or `uv add --dry-run` to see what would be installed before committing.

If your organization uses a private index, name-space internal packages with a company prefix (e.g., `acme-utils` not `utils`) so that even if the wrong index is queried, the name does not collide with a public package.

**Why:** Researchers found that roughly 20% of package names recommended by LLMs do not exist on PyPI — attackers are registering those names with malicious payloads ("slopsquatting"). Classic typosquatting (e.g., `transformers` vs `transfomers`) is also active against AI/ML packages. Checkmarx identified over 10,000 malicious packages on PyPI specifically targeting ML developers (as cited in GLACIS's 2026 AI supply chain security guide).

**Caveat / contested:** As of April 2025, no confirmed *successful* slopsquatting attack had been publicly reported, though the attack surface is considered actionable by researchers. Typosquatting attacks on PyPI remain documented and active. The 10,000 malicious-packages figure is Checkmarx's research (cited secondary via GLACIS); the methodology was not independently reviewed for this draft.

**Sources:** [rescana.com — AI hallucinated dependencies and slopsquatting](https://www.rescana.com/post/ai-hallucinated-dependencies-in-pypi-and-npm-the-2025-slopsquatting-supply-chain-risk-explained) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13) · [glacis.io — AI supply chain security guide](https://www.glacis.io/guide-ai-supply-chain-security) (fetched 2026-07-13) · [optiv.com — Securing software supply chain from typosquatting](https://www.optiv.com/insights/discover/blog/securing-software-supply-chain-typosquatting-attacks) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (academic/research source on slopsquatting + independent security practitioner blogs; Checkmarx 10,000-packages figure attributed as Checkmarx research, cited via GLACIS)

---

## Practice: Configure private indexes correctly to block dependency confusion attacks

**Do:** When using a private PyPI mirror (devpi, Artifactory, bandersnatch, or a cloud artifact registry), always use `--index-url` (not `--extra-index-url`) to designate your private registry as the *sole* index. In `pip.conf`:

```ini
[global]
index-url = https://private.company.com/simple/
```

With **uv**, set private indexes first in `pyproject.toml` and use `explicit = true` to prevent packages from falling back to PyPI unless explicitly pinned to it. uv's default `first-index` strategy stops resolution at the first index where a package is found, which blocks the classic dependency confusion path.

⚠️ **WARNING:** `--extra-index-url` is the source of CVE-2018-20225. When pip finds a package name on both indexes, it installs whichever has the *higher version number* — meaning an attacker who publishes version `9999.0` of your private package name on public PyPI wins automatically. This is a documented, unfixed behavior in pip itself.

⚠️ **WARNING:** The `--trusted-host` flag in pip disables TLS certificate verification for that host. Never use `--trusted-host` on a network host — package downloads over unencrypted connections are subject to interception and substitution. `--trusted-host` is only acceptable on `localhost` (127.0.0.1) for local development.

**Why:** In a dependency confusion attack, an attacker registers your internal package name on public PyPI with an artificially high version number. If your pip config queries both your private registry and public PyPI (the default when using `--extra-index-url`), pip chooses the public attacker-controlled version.

**Caveat / contested:** For air-gapped deployments, use **bandersnatch** to create a full local mirror or **devpi** to proxy and cache. Devpi and Artifactory can proxy PyPI on first download and serve packages offline thereafter. Always use HTTPS even for internal mirrors and rotate credentials.

**Sources:** [inventivehq.com — Private Python package repositories guide](https://inventivehq.com/blog/private-python-package-repositories-guide) (fetched 2026-07-13) · [docs.astral.sh/uv/concepts/indexes](https://docs.astral.sh/uv/concepts/indexes/) (fetched 2026-07-13) · [cowlicks.website — Arbitrary code execution from pip's extra-index-url](https://cowlicks.website/posts/arbitrary-code-execution-from-pips-extra-index-url.html) (fetched 2026-07-13) · [lucasgabrielb.com — Protecting Python projects against supply chain attacks](https://lucasgabrielb.com/en/posts/protecting-your-python-projects-against-supply-chain-attacks/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (uv official docs + independent security articles + CVE reference)

---

## Practice: Monitor CVEs in AI-specific libraries as a distinct discipline

**Do:** Subscribe to GitHub security alerts for each AI library your agents use: `langchain-ai/langchain`, `pytorch/pytorch`, `huggingface/transformers`, `openai/openai-python`, `anthropics/anthropic-sdk-python`. In CI, run `pip-audit` or `uv audit` against your pinned lock file — not just a `requirements.txt` — so transitive dependencies (like `langgraph-checkpoint-sqlite`) are also checked. When a critical advisory drops (CVSS ≥ 7.0), treat it as P1: check your SBOM, identify all affected environments, and patch within 24 hours.

Document a triage process for the common AI-library CVE patterns:
- CVE-2025-68664 (langchain-core deserialization, CVSS 9.3 CNA / 8.2 NVD, patched in 1.2.5 / 0.3.81)
- CVE-2026-34070 (langchain-core path traversal, CVSS 7.5, patched in 1.2.22 / 0.3.86 for the 0.3.x branch)
- CVE-2025-67644 (langgraph-checkpoint-sqlite SQL injection, CVSS 7.3, patched in 3.0.1)

🕒 **verify live** — patch versions correct as of 2026-07-13; check advisory feeds for newer releases.

**Why:** AI framework libraries move extremely fast and have not historically had mature security-review processes. CVE-2025-68664 in langchain-core allowed an attacker to extract your API keys (OpenAI, Anthropic, AWS) simply by passing a crafted payload to a streaming endpoint. AI agents often run with broad environment variable access, making secrets-exfiltration CVEs especially dangerous.

**Caveat / contested:** The published CVSS scores for these findings vary between GitHub CNA and NVD (e.g., CVE-2025-68664 is 9.3 on GitHub CNA vs 8.2 on NVD) — use the higher score to be conservative. Some AI libraries (torch, transformers) have long release cycles and applying patches may break model compatibility; always test patched versions against your model-serving code before deploying.

**Sources:** [labs.cloudsecurityalliance.org — LangChain/LangGraph critical vulnerabilities](https://labs.cloudsecurityalliance.org/research/csa-research-note-langchain-langgraph-critical-vulns-framewo/) (fetched 2026-07-13) · [cyata.ai — CVE-2025-68664](https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/) (fetched 2026-07-13) · [stackharbor.com — Python pip-audit and Safety](https://stackharbor.com/en/knowledge-base/python-pip-audit-safety/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (CSA research note + independent security blog + managed-ops practitioner guide)

---

## Practice: Treat source distributions (sdist) as higher-risk than wheels in agent pipelines

**Do:** Prefer binary wheel installations (`--only-binary :all:`) for packages in production AI agent deployments. Where only an sdist is available, review the `setup.py` / `pyproject.toml` build hooks before installing, or build the wheel in an isolated environment (e.g., a container sandbox) and then deploy the built wheel. With uv, use `--no-build` to prevent implicit sdist compilation.

**Why:** Source distributions execute arbitrary Python code at install time via `setup.py`. This is an intentional Python packaging feature enabling C/C++ extensions in libraries like torch and numpy — but it also means a malicious sdist can run attacker code the instant a developer types `pip install`. Wheels are pre-built and do not execute code on install.

**Caveat / contested:** Many AI/ML packages (especially those with CUDA extensions) only publish wheels for specific Python/CUDA version combinations; you may have no choice but to install an sdist for niche hardware configurations. In those cases, pin the exact hash of the sdist and review the build script before the first install on a new platform.

**Sources:** [github.com/lirantal/pypi-security-best-practices](https://github.com/lirantal/pypi-security-best-practices) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13)

**Confidence:** thin — both sources are independent practitioners; the underlying fact (setup.py executes code at install time) is uncontested Python packaging behavior. `--no-build` uv flag advice is single-sourced.

---

## Held pending fixes
- Consumer-side pip/uv attestation verification: status as of mid-2026 is in-progress per draft; check pip/uv changelogs for enforcement rollout ⚠ (verify live, no project issue filed — gap not grading-blockable)

## CHANGELOG (grading → this entry)
1. Beginner KILL: Added `pip install pip-audit` prerequisite note and current version (2.10.1, 2026-06-10) to the CI practice — novices had no instruction for installing the tool.
2. Beginner KILL: Promoted `--trusted-host` TLS-bypass warning from buried caveat paragraph to its own `⚠️ WARNING` block in the private-index practice.
3. Skeptic FIX: Trusted Publishing confidence label reworded — the Sigstore GA post (blog.sigstore.dev) is co-authored by William Woodruff (Trail of Bits) alongside two Google engineers; label now reflects "two distinct organizations" rather than a clean "two independent publishers" claim.
4. Skeptic FIX: "10,000 malicious packages targeting ML developers" — attribution corrected to Checkmarx as primary source (GLACIS guide cites Checkmarx research; updated caveat accordingly).
5. Skeptic FLAG: Removed the Ultralytics SBOM narrative comparison ("teams with SBOMs triaged faster") — not stated in the cited PyPI post-mortem; replaced with a factual description of the practice's value.
6. Timekeeper FIX: Updated "as of late 2024, downstream attestation verification not yet implemented" → "as of mid-2026 … not yet universally enforced" with verify-live tag.
7. Timekeeper FIX: Updated OpenAI/Astral acquisition note — acquisition announced March 19, 2026; open-source commitment is public (MIT/Apache 2.0); regulatory approval still pending as of mid-2026; UV_MALWARE_CHECK requires uv ≥ 0.11.16.
8. Timekeeper FIX: pip-audit version now stated: 2.10.1 (released 2026-06-10).
9. Timekeeper FLAG: `uv audit` marked "in preview / unstable" per Astral's own documentation — breaking changes expected.
10. Timekeeper KILL note: Added that `UV_EXCLUDE_NEWER` env var does NOT support duration strings; the `exclude-newer = "7 days"` TOML/CLI syntax requires uv ≥ 0.9.17. Clarified that `exclude-newer-package` override has known edge-case bugs.
11. Timekeeper FIX: CVE-2026-34070 older-branch patch — listed as 0.3.86 (separate from the 0.3.81 fix for CVE-2025-68664); the two CVEs have distinct fix versions in the 0.3.x series.
12. Link-check gate (2026-07-14): openai.com/index/openai-to-acquire-astral/ confirmed live via web search but returns 403 to automated curl — unlinked to plain text per gate policy. Citation retained.
