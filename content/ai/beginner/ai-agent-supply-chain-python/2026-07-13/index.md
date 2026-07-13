---
title: "AI Agent Supply Chain Verification — Python (Beginner Guide, as of 13 Jul 2026)"
date: 2026-07-13
snapshot_date: 2026-07-13
topic: ai-agent-supply-chain-python
track: beginner
audience: "people new to AI"
description: "Plain-English guide for beginners: how to protect the Python packages your AI agent depends on from tampering, malware, and fake package names — covering hash pinning, vulnerability scanning, cooldown windows, safe private registries, and more."
content_type: "Best Practice"
categories: ["Python", "Supply Chain Security", "AI Agents"]
tags: ["python", "pip", "uv", "poetry", "pypi", "sbom", "supply-chain", "cve", "sigstore"]
last_refreshed: 2026-07-13
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-13"
grading_result: "0 fabrications; 12 corrections applied; 0 gaps filed as project-33 issues"
---

<!-- This file lands at content/ai/beginner/ai-agent-supply-chain-python/2026-07-13/index.md and is
     an IMMUTABLE dated snapshot. Once published it is never edited — a refresh is a NEW snapshot-date dir.
     Source tiers: independently-corroborated = 2+ DIFFERENT publishers; vendor-documented = official
     vendor docs only (authoritative, single source). -->

# AI Agent Supply Chain Verification — Python (Beginner Guide, as of 13 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **13 Jul 2026**, frozen here and kept as
> a permanent archive entry. Research-drafted by a pupil, graded by the 3-lens panel + sensei.
> Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## What this page is about

When you build an AI agent in Python, your code relies on dozens of helper packages — things like `langchain`, `torch`, or `openai` — that you download from the internet. Each of those packages is a potential entry point for an attacker. This kind of threat has its own name: a **supply chain attack**.

Real incidents have targeted popular AI packages on PyPI (Python's main package repository) through several methods:

- **Typosquatting** — uploading a package with a name almost identical to a popular one (e.g., `transfomers` instead of `transformers`) hoping someone makes a typo.
- **Slopsquatting** — registering package names that AI assistants hallucinate and recommend but that do not actually exist on PyPI, then putting malware in them.
- **Account takeover** — stealing a developer's credentials and publishing a poisoned update to a real, popular package.
- **Dependency confusion** — tricking your package manager into downloading an attacker-controlled public package instead of your private internal one.

The practices below are layered defenses — each one stops a different kind of attack. None of them is hard to do once you understand why it matters.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Pin every dependency with cryptographic hashes

⚠️ **WARNING:** `pip install --extra-index-url <private-url>` does **not** isolate your install to the private index — pip still checks public PyPI and will install the highest-version package it finds across both indexes (CVE-2018-20225 — a documented vulnerability where pip's behavior allows an attacker's public package to win just by having a higher version number). This is a dangerous default for AI teams who think they are isolated. See the private-index practice below.

### What this means for a beginner

A Python **package manager** (pip, uv, or Poetry) downloads and installs packages for you. By default it just checks that the version number matches — it does not check whether the actual file you received is the one the original author uploaded.

A **cryptographic hash** (specifically SHA-256) is a short fingerprint computed from a file's contents. If even one byte changes, the hash changes. When you record hashes in your lock file, your package manager can verify each download against that fingerprint and refuse to install anything that does not match.

A **lock file** is an auto-generated file that records the exact version and hash of every package (including packages your packages depend on — called **transitive dependencies**). You commit this file to version control so every team member and every automated system installs exactly the same thing.

**Do:**

Choose one of the three approaches below based on which tool you use.

**Option A — uv (recommended default for new projects):**

`uv lock` generates a `uv.lock` file that already includes SHA-256 hashes for every package. Run it once after adding a dependency:

```bash
uv lock
```

Commit `uv.lock` to git. Done.

**Option B — Poetry:**

Poetry automatically includes hashes in `poetry.lock`. After adding a package:

```bash
poetry lock
```

Commit `poetry.lock` to git.

**Option C — plain pip with pip-tools:**

`pip-tools` is a package that adds the `pip-compile` command. First install it:

```bash
pip install pip-tools
```

`requirements.in` is a short file you write by hand listing only the packages your project directly needs (e.g., `langchain>=0.2`). `requirements.txt` is the full expanded list with pinned versions and hashes that `pip-compile` generates from your `.in` file — you never edit the `.txt` file manually.

Generate the pinned, hashed `requirements.txt` from your hand-written `requirements.in`:

```bash
pip-compile --generate-hashes requirements.in -o requirements.txt
```

Install with hash verification enforced:

```bash
pip install --require-hashes -r requirements.txt
```

Never leave `--require-hashes` off in production deploys.

**Why (beginner):** A version number alone (`requests==2.32.3`) does not guarantee you get the file you expect. An attacker who compromises a mirror or CDN cache can serve a different file with the same version number. A cryptographic hash makes a swap detectable at install time: pip, Poetry, and uv will all refuse to install a file whose hash does not match. The concrete failure this prevents: a poisoned package silently installs malware into your agent without any error message.

**Caveat / contested:** Hash pinning stops tampering *after* the lock file was generated, but it will not protect you from a malicious package that was already present on PyPI when you first resolved. You still need vulnerability scanning and a cooldown period (see the next two practices). Also, `--require-hashes` in pip mode is "all-or-nothing" — every entry in the requirements file must include a hash, so mixing pinned and unpinned entries will fail.

**Sources:** [pip.pypa.io — Secure installs](https://pip.pypa.io/en/stable/topics/secure-installs/) (fetched 2026-07-13) · [pydevtools.com — Pin dependencies with hashes in uv](https://pydevtools.com/handbook/how-to/how-to-pin-dependencies-with-hashes-in-uv/) (fetched 2026-07-13) · [lucasgabrielb.com — Protecting Python projects against supply chain attacks](https://lucasgabrielb.com/en/posts/protecting-your-python-projects-against-supply-chain-attacks/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (pip official docs + two independent developer guides)

---

## Practice: Run pip-audit (or uv audit) in CI on every pull request

### What this means for a beginner

A **CVE** (Common Vulnerabilities and Exposures) is a publicly registered security flaw with an ID number (for example, CVE-2025-68664). When a CVE is found in a package you use, a database records it. **pip-audit** is a tool that checks your installed packages against that database and tells you which ones have known flaws.

**CI** (continuous integration) is an automated system that runs checks every time code is proposed for merging. Adding pip-audit to CI means every proposed change is automatically checked for vulnerable packages before it can be merged — nobody has to remember to do it by hand.

**Prerequisite:** Install pip-audit first:

```bash
pip install pip-audit
```

(Current version: 2.10.1, released 2026-06-10 — 🕒 verify live.)

For uv-based projects, `uv audit` is built-in but is currently in **preview / unstable** — breaking changes are possible. Verify against your installed uv version before relying on it in CI.

**Do:**

Add a vulnerability scanning step to every CI run. With pip-audit, run:

```bash
pip-audit -r requirements.txt --strict --format json -o audit.json
```

This scans every package listed in `requirements.txt`, queries the OSV database (which aggregates PyPI Advisory Database, GitHub Advisory Database, and NVD), and writes findings to `audit.json`.

With uv, the equivalent is simply:

```bash
uv audit
```

To gate your CI build on fixable findings only (so you are not blocked by a vulnerability that has no available fix yet), run this check on the output:

```bash
jq -e '[.vulnerabilities[] | select(.fix_versions | length > 0)] | length == 0' audit.json
```

This command uses `jq` (a tool for reading JSON files) to count how many vulnerabilities have a fix available; the build fails only if that number is not zero.

For unfixable findings, record a time-boxed suppression — no longer than 90 days — with a documented reason, rather than an open-ended ignore.

**Why (beginner):** AI projects depend on rapidly evolving libraries. CVE-2025-68664 in langchain-core (CVSS score 9.3 on GitHub CNA / 8.2 on NVD — higher score means more severe) allowed an attacker to extract your API keys (OpenAI, Anthropic, AWS) just by sending a specially crafted message to a streaming endpoint. Running a scanner on every PR means the pipeline rejects a merge before a vulnerable library ships to production. The concrete failure prevented: your API keys get stolen and used to run up charges on your account.

**Caveat / contested:** pip-audit is "not a static code analyzer" and cannot detect malicious packages that have no CVE advisory yet (zero-days, newly uploaded malware). Combine with the cooldown window in the next practice. Safety CLI is another tool that overlaps with pip-audit on some advisories and occasionally catches findings the other misses; running both quarterly is reasonable but not required daily.

**Sources:** [pypi.org/project/pip-audit](https://pypi.org/project/pip-audit/) (fetched 2026-07-13) · [stackharbor.com — Python pip-audit and Safety](https://stackharbor.com/en/knowledge-base/python-pip-audit-safety/) (fetched 2026-07-13) · [cyata.ai — CVE-2025-68664](https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (PyPI official project page + two independent guides + CVE incident report)

---

## Practice: Use uv's install-cooldown and malware-check to block brand-new malicious packages

### What this means for a beginner

Even with vulnerability scanning, a brand-new malicious package has no CVE yet — it was just uploaded. The good news is that most malicious packages on PyPI are detected and removed within 24 to 72 hours. A **cooldown window** tells your package manager to refuse to install any package that appeared on PyPI in the last N days. An attacker's freshly uploaded malware is invisible to your project until it has survived long enough to be vetted.

This practice is specific to **uv**, the package manager. If you are using plain pip or Poetry, the cooldown feature is not available; rely more heavily on the other practices in this guide.

**Do:**

Set a 7-day cooldown in your `pyproject.toml` or `uv.toml` file. Open the file and add:

```toml
[tool.uv]
exclude-newer = "7 days"
```

This requires uv version 0.9.17 or later (the friendly duration string like `"7 days"` was added in December 2025 in PR #16814).

Important: `UV_EXCLUDE_NEWER` as an environment variable does NOT yet support duration strings — only the TOML/CLI flags do. Use the config file shown above.

Enable the malware check in your CI workflow file (for GitHub Actions, this goes in your `.yml` workflow file):

```yaml
- name: Sync dependencies
  run: uv sync --locked
  env:
    UV_MALWARE_CHECK: "1"
```

`UV_MALWARE_CHECK` requires uv version 0.11.16 or later and is currently in **preview / unstable** — verify it is available in your uv version before relying on it.

What `UV_MALWARE_CHECK=1` does: during `uv sync`, uv looks up every locked package against MAL-prefixed advisories in the OSV database and refuses to install any that are flagged as malware.

If a package needs an urgent security patch before the 7-day cooldown expires, you can override it per-package:

```toml
exclude-newer-package = { critical-fix-pkg = false }
```

Note: this per-package override option has known edge-case bugs in active uv issues — 🕒 verify live before using it.

**Why (beginner):** Most malicious packages uploaded to PyPI are caught and removed within 24 to 72 hours. A 7-day cooldown means your project will never install a package that appeared on PyPI in the last week unless you explicitly override it. `UV_MALWARE_CHECK=1` adds a second layer: it checks against a database of already-identified malware. The concrete failure prevented: your AI agent silently downloads and runs attacker code the moment you run `uv sync`.

**Caveat / contested:** The cooldown has a real cost — it delays security patches by up to 7 days. Teams with strict deadlines on vulnerability remediation should use 1 to 2 days rather than 7. The malware check only catches packages already in the OSV database; a newly uploaded, not-yet-reported malicious package will still pass. Also note: **OpenAI acquired Astral (uv's maintainer) on March 19, 2026.** Astral's founder publicly committed to keeping uv and ruff open source under MIT/Apache 2.0, but regulatory approval is still pending as of mid-2026 — verify the project's open-source status if this is important to your organization's policies.

**Sources:** [pydevtools.com — Protect against Python supply chain attacks with uv](https://pydevtools.com/handbook/how-to/how-to-protect-against-python-supply-chain-attacks-with-uv/) (fetched 2026-07-13) · [byteiota.com — uv audit Python supply chain defense](https://byteiota.com/uv-audit-python-supply-chain-defense/) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13) · openai.com — OpenAI to acquire Astral (fetched 2026-07-13; URL confirmed live via search but returns 403 to automated checks — unlinked per gate policy)

**Confidence:** ✅ independently-corroborated (two independent guides plus the defence-in-depth article; acquisition fact from OpenAI official announcement)

---

## Practice: Use PyPI Trusted Publishing and Sigstore attestations when you publish packages

### What this means for a beginner

This practice applies if your team **publishes** Python packages — either to public PyPI or to a private package registry your organization runs. If you only install packages and never publish them, you can read this for awareness and move on.

**Long-lived API tokens** are passwords you generate once and store forever (in a CI secret, a config file, etc.) so that automated tools can publish packages on your behalf. If an attacker steals a long-lived token from a log file or leaked environment variable, they can publish a malicious version of your package. Real incidents (the Ultralytics and GhostAction incidents) exploited exactly this.

**Trusted Publishing** is a newer approach: instead of a stored password, PyPI checks that the publish request is coming from a specific GitHub repository and workflow. It uses a short-lived **OIDC token** (Open ID Connect — a standard for proving identity) that expires in 15 minutes. A 15-minute token found in a leaked log is useless.

**Sigstore attestations** are cryptographic proofs that a package was built from a specific repository and workflow run. They are generated automatically — you do not need to do anything extra.

**Do:**

1. In your PyPI project settings, register your GitHub repository and workflow as a Trusted Publisher.
2. In your GitHub Actions workflow file, add this permission so the workflow can request a short-lived token:

```yaml
permissions:
  id-token: write
```

3. Use the `pypa/gh-action-pypi-publish` action to publish. It now generates Sigstore-based attestations by default (via PEP 740 — a Python standard for package attestations) with no extra steps.

Short-lived OIDC tokens replace stored API tokens and expire in 15 minutes.

**Why (beginner):** Long-lived API tokens are the number-one mechanism for supply chain takeover via CI secret theft. An OIDC token that expires in 15 minutes is useless to an attacker who finds it in a leaked log file. Sigstore attestations cryptographically bind the published artifact to the exact repository and workflow run that produced it, so anyone downloading your package can verify it came from your code. The concrete failure prevented: an attacker uses a stolen token to publish a malicious update under your package name, silently hitting all your users.

**Caveat / contested:** As of mid-2026, downstream verification — having `pip` or `uv` automatically check attestations when installing — is not yet universally enforced. 🕒 Verify live against pip/uv changelogs for your installed version. Attestations provide transparency and auditability now, but automated consumer-side enforcement is still in progress. Attestations also cannot detect malicious code introduced *before* the build; they only prove the package was built from the claimed repository.

**Sources:** [docs.pypi.org — Trusted Publishers](https://docs.pypi.org/trusted-publishers/) (fetched 2026-07-13) · [docs.pypi.org — Attestations security model](https://docs.pypi.org/attestations/security-model/) (fetched 2026-07-13) · [blog.trailofbits.com — Attestations: a new generation of signatures on PyPI](https://blog.trailofbits.com/2024/11/14/attestations-a-new-generation-of-signatures-on-pypi/) (fetched 2026-07-13) · [blog.sigstore.dev — PyPI attestations GA](https://blog.sigstore.dev/pypi-attestations-ga/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (two official PyPI docs pages as one vendor source; Trail of Bits blog; Sigstore GA post co-authored by Trail of Bits and two Google engineers — partial author overlap noted; label reflects two distinct organizations)

---

## Practice: Generate an SBOM at build time to enable rapid CVE triage

### What this means for a beginner

An **SBOM** (Software Bill of Materials) is a machine-readable list of every package your project uses, including the exact versions. Think of it as an ingredient list for your software.

When a critical security flaw is announced for a library (say, langchain), the first question is "do any of our deployed systems use this library?" Without an SBOM, someone has to check every server by hand. With an SBOM, you query the file in seconds.

**CycloneDX** is a standard format for SBOMs. There is a Python tool called `cyclonedx-bom` that generates one automatically from whatever is installed in your Python environment.

**Do:**

Install the tool (🕒 current version: 7.3.0 — verify live):

```bash
pip install cyclonedx-bom
```

Generate an SBOM from your current environment immediately after installing dependencies in CI:

```bash
cyclonedx-py environment -o sbom.cdx.json --of json
```

This creates `sbom.cdx.json` — a JSON file listing every installed package and version. Commit or publish this file alongside each release.

If you use Poetry, use:

```bash
cyclonedx-py poetry
```

If you use Pipenv, use:

```bash
cyclonedx-py pipenv
```

To merge vulnerability findings into the same SBOM format:

```bash
pip-audit --format cyclonedx-json
```

**Why (beginner):** When a critical vulnerability drops in a library like langchain or torch, the first question is "are we affected?" Without an SBOM, answering that requires manually checking every deployed environment. With an SBOM, you query a machine-readable inventory in minutes. The concrete failure prevented: you spend hours or days checking systems by hand during a security incident, during which time your agent may be actively exploited.

**Caveat / contested:** An SBOM records what was installed, not what is actually called at runtime. You may be flagged as vulnerable to a CVE in a transitive dependency that your code never uses — the SBOM will flag it, but the real risk may be lower than it appears. SBOM formats (CycloneDX vs SPDX) are not yet universally interoperable, so choose one and stick to it per project.

**Sources:** [pypi.org/project/cyclonedx-bom](https://pypi.org/project/cyclonedx-bom/) (fetched 2026-07-13) · [github.com/CycloneDX/cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) (fetched 2026-07-13) · [openssf.org — Choosing an SBOM generation tool](https://openssf.org/blog/2025/06/05/choosing-an-sbom-generation-tool/) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (PyPI + GitHub repo as one vendor source; OpenSSF blog + bernat.tech as two independent publishers)

---

## Practice: Defend against typosquatting and slopsquatting before you pip install anything

### What this means for a beginner

**Typosquatting** is when an attacker registers a package name that looks almost like a real one — for example `transfomers` (missing an 'r') instead of `transformers`. If you make a typo while typing a package name, you install malware instead.

**Slopsquatting** is newer and specific to AI tools: AI assistants sometimes confidently recommend Python package names that do not exist. Attackers register those non-existent names on PyPI with malicious payloads. Researchers found that roughly 20% of package names recommended by LLMs do not exist on PyPI. The concrete failure: you ask an AI assistant how to do something, it suggests `pip install some-package`, and that package is malware.

**Do:**

Before installing any new Python package into an AI agent project, perform three checks:

1. **Verify the exact package name** against official documentation or the project's GitHub page. Never copy-paste a package name from AI-generated code without first looking it up at [pypi.org](https://pypi.org).

2. **Check the package's creation date, download count, and owner on PyPI.** A package registered last week with zero download history but a popular-sounding name is a red flag.

3. **Do a dry run** before actually installing. This shows you what would be installed without downloading anything:

   With pip:
   ```bash
   pip install --dry-run <package-name>
   ```

   With uv:
   ```bash
   uv add --dry-run <package-name>
   ```

If your organization uses a private package index, name internal packages with a company prefix (for example, `acme-utils` rather than just `utils`). This prevents name collisions with public packages even if the wrong index is accidentally queried.

**Why (beginner):** Typosquatting attacks on PyPI are documented and ongoing against AI/ML packages. Researchers also found roughly 20% of package names suggested by LLMs do not exist on PyPI — attackers register those names with malicious payloads. Checkmarx research (cited via the GLACIS AI supply chain security guide) identified over 10,000 malicious packages on PyPI specifically targeting ML developers. The concrete failure prevented: you install what looks like a legitimate package and it silently exfiltrates your API keys or installs a backdoor.

**Caveat / contested:** As of April 2025, no confirmed successful slopsquatting attack had been publicly reported, though the attack surface is considered actionable by researchers. Typosquatting attacks on PyPI remain documented and active. The 10,000 malicious-packages figure is Checkmarx's research (cited secondarily via GLACIS); the methodology was not independently reviewed for this entry.

**Sources:** [rescana.com — AI hallucinated dependencies and slopsquatting](https://www.rescana.com/post/ai-hallucinated-dependencies-in-pypi-and-npm-the-2025-slopsquatting-supply-chain-risk-explained) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13) · [glacis.io — AI supply chain security guide](https://www.glacis.io/guide-ai-supply-chain-security) (fetched 2026-07-13) · [optiv.com — Securing software supply chain from typosquatting](https://www.optiv.com/insights/discover/blog/securing-software-supply-chain-typosquatting-attacks) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (academic/research source on slopsquatting + independent security practitioner blogs; Checkmarx 10,000-packages figure attributed as Checkmarx research, cited via GLACIS)

---

## Practice: Configure private indexes correctly to block dependency confusion attacks

### What this means for a beginner

A **private index** (also called a private package registry) is a server your organization runs internally to host Python packages that are not public. Tools like devpi, Artifactory, and bandersnatch can serve this purpose.

A **dependency confusion attack** works like this: your package manager is told to check both your private registry and public PyPI. An attacker finds out the name of one of your private internal packages and registers that same name on public PyPI with a very high version number (like 9999.0). Your package manager sees version 9999.0 on public PyPI and version 1.0 on your private registry — and installs the attacker's version because it looks newer. This has happened in real incidents.

**Do:**

The safe setting is `--index-url` (not `--extra-index-url`). Using `--index-url` tells pip to use only that one index and not fall back to public PyPI.

In your `pip.conf` file (usually at `~/.config/pip/pip.conf` on Linux), set:

```ini
[global]
index-url = https://private.company.com/simple/
```

With uv, list private indexes first in `pyproject.toml` and use `explicit = true`:

```toml
[[tool.uv.index]]
url = "https://private.company.com/simple/"
explicit = true
```

uv's default `first-index` strategy stops resolution at the first index where a package is found, which blocks the classic dependency confusion path.

⚠️ **WARNING:** `--extra-index-url` is the source of CVE-2018-20225 (a documented vulnerability in pip). When pip finds a package name on both indexes, it installs whichever has the *higher version number* — meaning an attacker who publishes version `9999.0` of your private package name on public PyPI wins automatically. This is a documented, unfixed behavior in pip itself.

⚠️ **WARNING:** The `--trusted-host` flag in pip disables TLS certificate verification for that host. **Never use `--trusted-host` on a network host** — package downloads over unencrypted connections are subject to interception and substitution. `--trusted-host` is only acceptable on `localhost` (127.0.0.1) for local development.

**Why (beginner):** In a dependency confusion attack, an attacker registers your internal package name on public PyPI with an artificially high version number. If your pip config queries both your private registry and public PyPI — the default when using `--extra-index-url` — pip chooses the public attacker-controlled version. The concrete failure prevented: a package that looks like your own internal library installs attacker-controlled code across your entire team.

**Caveat / contested:** For air-gapped deployments (systems with no internet access), use bandersnatch to create a full local mirror or devpi to proxy and cache. Devpi and Artifactory can proxy PyPI on first download and serve packages offline thereafter. Always use HTTPS even for internal mirrors and rotate credentials regularly.

**Sources:** [inventivehq.com — Private Python package repositories guide](https://inventivehq.com/blog/private-python-package-repositories-guide) (fetched 2026-07-13) · [docs.astral.sh/uv/concepts/indexes](https://docs.astral.sh/uv/concepts/indexes/) (fetched 2026-07-13) · [cowlicks.website — Arbitrary code execution from pip's extra-index-url](https://cowlicks.website/posts/arbitrary-code-execution-from-pips-extra-index-url.html) (fetched 2026-07-13) · [lucasgabrielb.com — Protecting Python projects against supply chain attacks](https://lucasgabrielb.com/en/posts/protecting-your-python-projects-against-supply-chain-attacks/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (uv official docs + independent security articles + CVE reference)

---

## Practice: Monitor CVEs in AI-specific libraries as a distinct discipline

### What this means for a beginner

AI framework libraries like langchain, torch, and transformers move extremely fast and have not historically had mature security-review processes. New vulnerabilities are found regularly. This practice is about making sure you find out about those vulnerabilities quickly and fix them before an attacker exploits them.

**CVSS** (Common Vulnerability Scoring System) is a number from 0 to 10 that rates how severe a security flaw is. A score of 7.0 or higher is considered high severity; 9.0 or higher is critical.

**Do:**

Subscribe to GitHub security alerts for each AI library your agents use. Go to the GitHub page for each repo and enable "Watch" with "Security alerts":

- `langchain-ai/langchain`
- `pytorch/pytorch`
- `huggingface/transformers`
- `openai/openai-python`
- `anthropics/anthropic-sdk-python`

In CI, run `pip-audit` or `uv audit` against your pinned lock file — not just a `requirements.txt` — so transitive dependencies (packages that your packages depend on, like `langgraph-checkpoint-sqlite`) are also checked.

When a critical advisory drops (CVSS score 7.0 or higher), treat it as a top-priority issue: check your SBOM, identify all affected environments, and patch within 24 hours.

Document a triage process for the common AI-library CVE patterns your team should be aware of:

- CVE-2025-68664 (langchain-core deserialization flaw, CVSS 9.3 GitHub CNA / 8.2 NVD, patched in versions 1.2.5 / 0.3.81)
- CVE-2026-34070 (langchain-core path traversal, CVSS 7.5, patched in versions 1.2.22 / 0.3.86 for the 0.3.x branch)
- CVE-2025-67644 (langgraph-checkpoint-sqlite SQL injection, CVSS 7.3, patched in version 3.0.1)

🕒 **verify live** — patch versions correct as of 2026-07-13; check advisory feeds for newer releases.

**Why (beginner):** CVE-2025-68664 in langchain-core allowed an attacker to extract your API keys (OpenAI, Anthropic, AWS) simply by passing a crafted payload to a streaming endpoint. AI agents often run with broad access to environment variables, making secrets-exfiltration vulnerabilities especially dangerous. The concrete failure prevented: an attacker sends a single malicious message to your AI agent and walks away with every API key in your environment.

**Caveat / contested:** The published CVSS scores for these findings vary between GitHub CNA and NVD (for example, CVE-2025-68664 is 9.3 on GitHub CNA vs 8.2 on NVD) — use the higher score to be conservative. Some AI libraries (torch, transformers) have long release cycles, and applying patches may break model compatibility; always test patched versions against your model-serving code before deploying.

**Sources:** [labs.cloudsecurityalliance.org — LangChain/LangGraph critical vulnerabilities](https://labs.cloudsecurityalliance.org/research/csa-research-note-langchain-langgraph-critical-vulns-framewo/) (fetched 2026-07-13) · [cyata.ai — CVE-2025-68664](https://cyata.ai/blog/langgrinch-langchain-core-cve-2025-68664/) (fetched 2026-07-13) · [stackharbor.com — Python pip-audit and Safety](https://stackharbor.com/en/knowledge-base/python-pip-audit-safety/) (fetched 2026-07-13)

**Confidence:** ✅ independently-corroborated (CSA research note + independent security blog + managed-ops practitioner guide)

---

## Practice: Treat source distributions (sdist) as higher-risk than wheels in agent pipelines

### What this means for a beginner

When you install a Python package, it comes in one of two formats:

- A **wheel** (file ending in `.whl`) is a pre-built package. Your package manager unpacks it and puts the files in place. No code runs during installation.
- A **source distribution** (called an **sdist**, file ending in `.tar.gz` or `.zip`) contains the raw source code. Your package manager must *build* it first, which means it runs `setup.py` — a Python file that executes arbitrary code.

This is an intentional Python packaging feature (it allows packages like torch and numpy to compile C/C++ extensions). But it also means a malicious sdist can run attacker code the instant you type `pip install`.

**Do:**

Prefer wheel installations for packages in production AI agent deployments. Pass `--only-binary :all:` to pip to enforce this:

```bash
pip install --only-binary :all: -r requirements.txt
```

With uv, use `--no-build` to prevent implicit sdist compilation:

```bash
uv sync --no-build
```

Where only an sdist is available, review the `setup.py` or `pyproject.toml` build hooks before installing, or build the wheel in an isolated environment (such as a container or sandbox) and then deploy only the built wheel.

**Why (beginner):** A malicious sdist can run attacker code the instant a developer types `pip install`. Wheels are pre-built and do not execute code on install. The concrete failure prevented: installing a package triggers a hidden script that exfiltrates your SSH keys, API tokens, or environment variables before you see any output.

**Caveat / contested:** Many AI/ML packages (especially those with CUDA extensions for running on graphics cards) only publish wheels for specific Python and CUDA version combinations. You may have no choice but to install an sdist for niche hardware configurations. In those cases, pin the exact hash of the sdist and review the build script before the first install on a new platform.

**Sources:** [github.com/lirantal/pypi-security-best-practices](https://github.com/lirantal/pypi-security-best-practices) (fetched 2026-07-13) · [bernat.tech — Securing Python supply chain](https://bernat.tech/posts/securing-python-supply-chain/) (fetched 2026-07-13)

**Confidence:** thin — both sources are independent practitioners; the underlying fact (setup.py executes code at install time) is uncontested Python packaging behavior. `--no-build` uv flag advice is single-sourced.

---

## Held pending fixes
- Consumer-side pip/uv attestation verification: status as of mid-2026 is in-progress per draft; check pip/uv changelogs for enforcement rollout ⚠ (verify live, no project issue filed — gap not grading-blockable)

## CHANGELOG
1. Re-leveled from technical entry (snapshot 2026-07-13) by rings-beginner-author. Facts unchanged.
2. Added plain-English introductions ("What this means for a beginner") for every practice.
3. Defined all acronyms on first use: CVE, SBOM, CI, CVSS, OIDC, sdist, TOML, CNA, NVD, TLS, SBOM format names (CycloneDX/SPDX).
4. Explained the `requirements.in` vs `requirements.txt` distinction in the hash-pinning practice.
5. Added install instructions for pip-audit (`pip install pip-audit`) and pip-tools (`pip install pip-tools`) as directed — both were already present in the source entry; made explicit for novices.
6. Kept all ⚠️ WARNING blocks verbatim; moved the hash-pinning `--extra-index-url` WARNING to the top of that practice per beginner-track rules.
7. Added "concrete failure prevented" callouts in plain words (stolen keys, malware install, etc.) to every Why section.
8. Presented three tool options (uv / Poetry / pip) sequentially rather than interleaved for readability; recommended uv as default for new projects as a framing choice (not a new fact).
9. All source URLs and Confidence labels carried through verbatim from the technical entry.
10. All 8 practices from the source entry are kept; none dropped.
11. Link-check gate (2026-07-14): openai.com/index/openai-to-acquire-astral/ confirmed live via web search but returns 403 to automated curl — unlinked to plain text per gate policy. Citation retained.
