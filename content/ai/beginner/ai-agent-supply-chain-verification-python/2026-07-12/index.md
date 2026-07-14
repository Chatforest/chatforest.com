---
title: "AI Agent Supply Chain Verification — Python — Beginner Guide (as of 12 Jul 2026)"
date: 2026-07-12
snapshot_date: 2026-07-12
topic: ai-agent-supply-chain-verification-python
track: beginner
audience: "people new to AI"
description: "Beginner-friendly guide to checking that the Python packages and AI models you download are safe before using them."
content_type: "Best Practice"
categories: ["Python", "AI Agents", "Supply Chain Security"]
tags: ["python", "pypi", "supply-chain", "pip-audit", "safetensors", "hugging-face", "github-actions"]
last_refreshed: 2026-07-12
graded_by: "RingS panel (Skeptic/Beginner/Timekeeper) + sensei, 2026-07-15"
grading_result: "0 fabrications; beginner re-level by rings-beginner-author"
---

<!-- Immutable dated snapshot. A refresh is a NEW snapshot-date dir. "Latest" computed by Grove's template. -->

# AI Agent Supply Chain Verification — Python — Beginner Guide (as of 12 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **12 Jul 2026**, frozen here as a permanent archive entry. Graded by the 3-lens panel (Skeptic/Beginner/Timekeeper) + sensei on 2026-07-15. Re-leveled for beginners; all facts are unchanged from the technical entry.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## What this guide is about

When you build an AI project in Python, you download software from the internet: Python packages from PyPI and AI model files from sites like Hugging Face. Any of those downloads could be tampered with or outright fake. "Supply chain" is the term security people use for the chain of software you depend on — and "supply chain verification" means checking that every link in that chain is safe before you use it.

This guide walks you through eight concrete practices, in plain language, with the exact commands you need.

---

## Practice: Check a PyPI package before you install it

**What is PyPI?** PyPI (the Python Package Index, at [pypi.org](https://pypi.org)) is the public store where anyone can upload Python packages for others to install with `pip install`. There is no gatekeeping — anyone can publish anything.

**Do:** Before you run `pip install <package-name>`, visit [pypi.org](https://pypi.org) and look the package up. Check three things:

1. The name is spelled exactly right. Attackers register names that differ by one character — for example `PyToich` instead of `PyTorch`, or `transformers-dev` instead of `transformers`.
2. The maintainer account has a history of releases, not a single upload from a brand-new account.
3. The download count is plausible. A famous library with almost no downloads is suspicious.

**Why (beginner):** Because anyone can publish to PyPI, attackers plant fake packages with names nearly identical to popular AI libraries. When you `pip install` one of these fakes, code hidden inside runs silently and can steal your passwords, API keys, or cloud credentials — before you ever see an error. In March 2024, Mend.io documented more than 100 such packages targeting machine-learning developers in a single campaign. In 2026, attackers also compromised the *real* `pytorch-lightning` package (versions 2.6.2 and 2.6.3), using a hidden `_runtime` directory with a staged downloader to steal cloud credentials from AWS, Azure, and GCP. 🕒 **verify live** — confirm the affected version numbers against the current Sonatype advisory.

**What goes wrong if you skip this:** You install a package that looks legitimate, it steals your cloud credentials in the background, and you get a surprise bill — or your account is used to attack others.

**Caveat / contested:** PyPI does flag suspected fakes automatically, but only at upload time. A package that was safe when first published can become dangerous later if its maintainer account is taken over. Popularity and download counts are therefore not a guarantee of safety.

**Sources:**
[blog.pypi.org — PyPI 2025 Year in Review](https://blog.pypi.org/posts/2025-12-31-pypi-2025-in-review/) (31 Dec 2025) · [sonatype.com — Malicious PyTorch Lightning Packages Found on PyPI](https://www.sonatype.com/blog/malicious-pytorch-lightning-packages-found-on-pypi) (2026) · mend.io — Over 100 Malicious Packages Target Popular ML PyPI Libraries (28 Mar 2024; confirmed live, non-200 response)

**Confidence:** ✅ independently-corroborated

---

## Practice: Give every AI project its own isolated environment

**What is a virtual environment (venv)?** A virtual environment is a self-contained folder that holds a specific Python installation and its packages, separate from every other project on your machine. Think of it as a clean room: packages you install inside it do not interfere with anything outside, and vice versa.

**Do:** Before installing any packages for a project, create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate       # Linux / macOS
# .venv\Scripts\activate        # Windows
```

After running `source .venv/bin/activate`, your terminal prompt changes (usually showing `(.venv)`) to confirm you are inside the environment. Every `pip install` you run after that goes into this project's private folder.

Install packages using a lockfile (see the next practice) to keep the environment reproducible. For deployed agents, Docker containers add an extra layer of protection that a virtual environment alone cannot provide.

**Why (beginner):** AI libraries like `torch`, `transformers`, and `langchain` drag in dozens of other packages. Putting them in a shared global Python installation can break your system tools and makes it nearly impossible to know exactly what you have installed. Separate environments also limit the blast radius: if a malicious package slips into one project's environment, it cannot directly reach the files or credentials of your other projects.

**What goes wrong if you skip this:** Installing AI packages globally can break unrelated Python scripts, make your environment impossible to reproduce later, and allow a compromised package to reach across all your projects.

⚠️ **WARNING:** A virtual environment does *not* block network access or disk writes. A malicious package running inside a venv can still connect to the internet and steal secrets. For untrusted code or AI agent execution, use Docker or a dedicated sandbox — not just a venv.

**Caveat / contested:** Venvs isolate Python packages but share the underlying operating system and network. For AI agents that run code as part of their task loop, security researchers consistently recommend container-level or VM-level isolation in addition to venvs.

**Sources:**
[pip.pypa.io — Repeatable Installs (pip v26.1.2)](https://pip.pypa.io/en/stable/topics/repeatable-installs/) (fetched 2026-07-12) · [pydevtools.com — pip-tools reference](https://pydevtools.com/handbook/reference/pip-tools/) (2 Jul 2026)

**Confidence:** 📄 vendor-documented

---

## Practice: Lock every package to an exact version with a hash fingerprint

**What is a lockfile?** A lockfile is a file that records the exact version of every package your project uses, including packages that your direct dependencies pulled in automatically. It means anyone who sets up your project later gets the exact same software.

**What is a SHA-256 hash?** SHA-256 is a mathematical fingerprint. Every file has one. If a package file is changed — even by one byte — its SHA-256 changes. Storing hashes in your lockfile lets pip reject any download that has been tampered with.

**What is pip?** `pip` is Python's built-in package installer. `pip-tools` is a separate package that extends pip to generate hash-pinned lockfiles.

**Do:** Install [pip-tools](https://pypi.org/project/pip-tools/) (v7.5.3, 11 Feb 2026 — 🕒 verify live) and generate a locked requirements file:

```bash
pip install pip-tools
pip-compile --generate-hashes
```

This creates a `requirements.txt` file containing exact version numbers (like `requests==2.32.3`) and SHA-256 hashes for every package, direct and indirect. Deploy with:

```bash
pip install --require-hashes -r requirements.txt
```

**Why (beginner):** Without hashes, `pip install` downloads whatever the latest version of a package is at that moment. If a package is updated between your test and your deployment — whether by a legitimate release or by an attacker — you could silently get different code. `--require-hashes` makes pip refuse any download whose fingerprint does not match the one in your lockfile, catching both network tampering and repository compromises.

**What goes wrong if you skip this:** You test with one version of a library, deploy with a silently different version, and your AI agent behaves unexpectedly — or worse, runs attacker-supplied code.

⚠️ **WARNING:** `--require-hashes` requires hashes for *all* packages, including indirect ones. A partially-hashed file causes an error. Use `pip-compile --generate-hashes` to produce the complete set rather than adding hashes by hand.

**A note on `pip lock` / `pylock.toml`:** pip 25.1 introduced an experimental `pip lock` command that produces a `pylock.toml` file (PEP 751 format). This is *not* a drop-in replacement for `requirements.txt` — it requires a compatible installer and cannot be used with `pip install --require-hashes -r requirements.txt` today. Use `pip-compile` if you need `--require-hashes`.

**Caveat / contested:** Hash-pinned lockfiles are platform-specific — Linux, macOS, and Windows each download different package files. Teams building for multiple platforms sometimes maintain separate lockfiles per platform, or use Docker images to sidestep the mismatch.

**Sources:**
[pip.pypa.io — Secure installs (pip v26.1.2)](https://pip.pypa.io/en/stable/topics/secure-installs/) (fetched 2026-07-12) · [pip-tools.readthedocs.io — pip-compile CLI](https://pip-tools.readthedocs.io/en/stable/cli/pip-compile/) (fetched 2026-07-12) · [pydevtools.com — pip-tools reference](https://pydevtools.com/handbook/reference/pip-tools/) (2 Jul 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice: Scan your packages for known security vulnerabilities

**What is a vulnerability?** A vulnerability (also called a CVE — Common Vulnerabilities and Exposures) is a documented security flaw in a piece of software. Databases track these so tools can warn you when you are using a package that has a known flaw.

**What is pip-audit?** `pip-audit` is a free, open-source tool maintained by the Python Packaging Authority (PyPA), Trail of Bits, and Google. It reads your packages and checks them against vulnerability databases.

**Do:** Install [pip-audit](https://pypi.org/project/pip-audit/) (latest v2.10.1, 10 Jun 2026 — 🕒 verify live) and run it before every deployment:

```bash
pip install pip-audit
# Preview proposed fixes first — do not apply yet
pip-audit --dry-run -r requirements.txt
# After reviewing, apply the fixes
pip-audit --fix -r requirements.txt
# In automated pipelines (CI), run without flags to just report
pip-audit -r requirements.txt
```

Always run `--dry-run` before `--fix`. The `--dry-run` flag shows you what changes pip-audit wants to make without actually making them, so you can review before committing. This matters especially for AI libraries: upgrading `torch` or `transformers` automatically can break a carefully tuned model environment.

**Why (beginner):** Popular AI libraries have long chains of dependencies. A security flaw in an indirect dependency — for example, a vulnerable version of `requests` that was pulled in by `openai` — will not show up unless you scan the full environment. pip-audit checks every package, direct and indirect, and reports all known security issues in one pass.

**What goes wrong if you skip this:** You ship an AI agent that contains a package with a known flaw, which an attacker exploits to steal data or credentials from you or your users.

**Caveat / contested:** pip-audit only catches vulnerabilities that have already been disclosed and indexed. It will not flag a brand-new malicious package or a zero-day exploit. It is a reactive safety net, not a complete substitute for hash-pinning and careful installation hygiene.

**Sources:**
[github.com/pypa/pip-audit](https://github.com/pypa/pip-audit) (fetched 2026-07-12; latest release v2.10.1, 10 Jun 2026) · [pypi.org/project/pip-audit](https://pypi.org/project/pip-audit/) (fetched 2026-07-12) · [pypi.org/project/safety](https://pypi.org/project/safety/) (fetched 2026-07-12; v3.8.1, 29 May 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice: Keep a software ingredient list (SBOM) for your AI project

**What is an SBOM?** SBOM stands for Software Bill of Materials. Just as a food product lists its ingredients, an SBOM lists every library your AI project depends on, including the indirect ones you never installed yourself. This makes it easier to find out quickly whether you are affected when a new vulnerability is discovered.

**What is CycloneDX?** CycloneDX is a standard format for SBOMs. The `cyclonedx-bom` Python package generates SBOMs in that format from your virtual environment.

**Do:** With your virtual environment active, run:

```bash
pip install cyclonedx-bom
cyclonedx-py environment
```

This produces a CycloneDX SBOM file (v7.3.0, 30 Mar 2026 — 🕒 verify live) that lists every package in the environment. Commit this file alongside each release of your project. You can also generate it directly from pip-audit: `pip-audit --format cyclonedx-json -r requirements.txt`.

For AI-specific components (model weight files, adapters, datasets), an experimental tool called `ai-bom` exists on PyPI, but it lacks independent documentation as of this snapshot and should be treated as an emerging option only.

**Why (beginner):** OWASP (the Open Worldwide Application Security Project) explicitly recommends maintaining signed, tamper-resistant SBOMs for AI supply chains. Regulators are beginning to require them too: the EU AI Act (Article 11/Annex IV) calls for a complete AI component inventory, effective August 2025 for new model placements; existing models placed before August 2025 have until August 2027. Even setting regulation aside, an SBOM means you can search one file to find out "am I using the package that just had a security alert?" instead of trying to remember what you installed six months ago.

**What goes wrong if you skip this:** A vulnerability is announced, you have no record of what your project uses, and you spend hours manually checking whether you are affected.

**Caveat / contested:** SBOM tooling is still maturing. The OpenSSF (Open Source Security Foundation) notes that "imperfect SBOMs are better than no SBOMs." CycloneDX-Python covers standard library dependencies well but does not automatically capture model weight files, dataset lineage, or LoRA adapters (fine-tuning checkpoint files). Those require manual entries or the not-yet-validated `ai-bom` tool.

**Sources:**
[github.com/CycloneDX/cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) (fetched 2026-07-12; v7.3.0, 30 Mar 2026) · [openssf.org — Choosing an SBOM Generation Tool](https://openssf.org/blog/2025/06/05/choosing-an-sbom-generation-tool/) (5 Jun 2025) · [genai.owasp.org — LLM03:2025 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) (fetched 2026-07-12)

**Confidence:** ✅ independently-corroborated

---

## Practice: Use SafeTensors model files instead of pickle files

**What are model weight files?** When you download an AI model from Hugging Face, you are downloading a large file containing the model's "weights" — the numbers that define how it behaves. These files come in different formats.

**What is pickle?** Python's pickle format is a way of saving Python objects to a file. The problem is that a pickle file can contain instructions that run automatically when the file is opened. Attackers can embed malicious code in a `.pt` or `.bin` file that executes the moment you load the model.

**What is SafeTensors?** SafeTensors is a newer format that stores only raw numerical data — no executable code. Loading a SafeTensors file cannot run arbitrary code. The format joined the PyTorch Foundation (Linux Foundation) in April 2026.

**Do:** When downloading models from Hugging Face, prefer files with the `.safetensors` extension. In code using the `transformers` library, add `use_safetensors=True`:

```python
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained("model-name", use_safetensors=True)
```

If a model is only available in pickle format (`.bin` or `.pt`), use Hugging Face's import scan results shown on the Hub file page, and scan the file with [fickling](https://github.com/trailofbits/fickling) or [ModelScan](https://github.com/protectai/modelscan) before loading it.

⚠️ **WARNING:** Simply calling `torch.load("model.bin")` on a file from an untrusted source executes arbitrary Python code embedded in the file. This can steal API keys, write backdoors, or download further malware — triggered by one line of code.

**Why (beginner):** Downloading a model from a random Hugging Face account is like downloading an executable from a stranger. If the file uses pickle format, opening it is enough to run attacker code on your machine. SafeTensors eliminates this risk by design.

**What goes wrong if you skip this:** You load a model weight file that silently steals your API keys, installs malware, or gives an attacker remote access to your computer.

**Caveat / contested:** Hugging Face's built-in pickle scanner on the Hub is described by Hugging Face itself as "maintained in a best-effort manner" — it is not foolproof. In February 2025, researchers found that some malicious `.bin` files compressed with 7z instead of ZIP bypassed the Hub's primary scanner (PickleScan). SafeTensors avoids the problem entirely rather than trying to detect malicious pickles. Some older or quantized models only ship in pickle format with no SafeTensors alternative available.

**Sources:**
[huggingface.co/docs/hub/en/security-pickle](https://huggingface.co/docs/hub/en/security-pickle) (fetched 2026-07-12) · datacamp.com — SafeTensors Format (fetched 2026-07-12; confirmed live, bot-protection 403)

**Confidence:** ✅ independently-corroborated

---

## Practice: Pin a Hugging Face model to an exact commit and read its model card

**What is a commit hash?** On Hugging Face (and on GitHub), every change to a repository is recorded as a "commit" with a unique identifier — a long string of letters and numbers called a commit hash. If you specify the hash instead of a branch name like `main`, you will always get exactly the same files, even if the repository is updated later.

**What is a model card?** A model card is the `README.md` file in a Hugging Face model repository. It describes the model: who made it, what data it was trained on, what license it uses, and sometimes how it performs on safety evaluations.

**Do:** When downloading a model in Python, add the `revision` parameter with the full commit hash:

```python
from huggingface_hub import snapshot_download
snapshot_download(
    "organization/model-name",
    revision="877b84a8f93f2d619faa2a6e514a32beef88ab0a"  # example — look up the actual hash
)
```

Find the hash on the model's Hugging Face page under the "Files and versions" tab — copy the full 40-character hash for the commit you have reviewed.

Before using any model, read its model card. Check the `license` field (governs whether you can use it commercially), the `datasets` field (where the training data came from), and the `base_model` field (what it was built on). Prefer models from verified organizations (shown as a blue badge on the Hub), and be cautious about models from accounts registered less than 30 days ago.

**Why (beginner):** A Hugging Face model repository's `main` branch can be updated at any time by its owner. If you rely on `main`, you might test with one set of weights and then deploy with different ones after an update — potentially malicious ones. Pinning to a commit hash means you will always load exactly what you reviewed and tested.

**What goes wrong if you skip this:** The model author (or an attacker who has taken over the account) updates the model after you test it. Your production AI agent silently runs different, potentially malicious weights.

**Caveat / contested:** `hf_hub_download()` checks server-provided checksums during the initial download when they are available, but it does not re-verify files already stored in your local cache on subsequent runs. The model card is author-supplied and not independently audited. Pinning to a commit hash guarantees you load the same file every time — it does not guarantee that file is safe.

**Sources:**
[huggingface.co/docs/huggingface_hub/guides/download](https://huggingface.co/docs/huggingface_hub/guides/download) (fetched 2026-07-12) · [huggingface.co/docs/hub/model-cards](https://huggingface.co/docs/hub/model-cards) (fetched 2026-07-12) · [beyondscale.tech — Open Source AI Model Security: Vetting Hugging Face Downloads](https://beyondscale.tech/blog/open-source-ai-model-security-hugging-face) (30 Apr 2026)

**Confidence:** ✅ independently-corroborated

---

## Practice: Pin GitHub Actions to a full commit hash in your automated workflows

**What is GitHub Actions?** GitHub Actions is GitHub's built-in system for running automated tasks — such as running tests or deploying your project — every time you push code. The instructions live in `.github/workflows/` files in your repository.

**What is a "tag" in this context?** GitHub Actions steps reference external actions using either a tag (like `@v4`) or a full 40-character commit SHA (like `@abc123...`). Tags are labels that can be moved to point at different code at any time.

**What is CI/CD?** CI/CD stands for Continuous Integration / Continuous Delivery — the automated pipeline that builds, tests, and deploys your code. GitHub Actions is a common tool for this.

**Do:** In your `.github/workflows/` files, replace floating tag references like this:

```yaml
# Insecure — the tag can be moved to malicious code
uses: actions/checkout@v4
```

with the full 40-character commit SHA for the version you have reviewed. Look up the SHA without cloning using:

```bash
git ls-remote https://github.com/actions/checkout refs/tags/<tag>
```

Note: `actions/checkout` is currently at **v7.0.0** (June 2026). The SHA in your workflow must correspond to the version you have reviewed. **Always look up the current SHA yourself — never copy a SHA from documentation.**

For repositories with many actions, use [pinact](https://github.com/suzuki-shunsuke/pinact) to automate the conversion. Configure Dependabot (`package-ecosystem: "github-actions"`) to open pull requests automatically when pinned SHAs have newer releases.

**Why (beginner):** A GitHub Actions tag is a mutable pointer — whoever controls the action's repository can point the tag at completely different code. In March 2025, the `tj-actions/changed-files` action was compromised: attackers updated more than 350 tags to dump CI secrets, affecting over 23,000 repositories. Workflows pinned to SHAs were completely unaffected because a SHA cannot be moved.

**What goes wrong if you skip this:** An attacker compromises a GitHub Action your workflow uses, updates the tag to malicious code, and your automated pipeline silently uploads your secrets to the attacker's server on the next code push.

**Caveat / contested:** SHA pinning means you need to remember to update the SHA when new secure releases of the action ship. This is why Dependabot automation is recommended alongside pinning — not instead of it.

**Sources:**
[docs.github.com/en/actions/reference/security/secure-use](https://docs.github.com/en/actions/reference/security/secure-use) (fetched 2026-07-12) · [stepsecurity.io — Pinning GitHub Actions for Enhanced Security](https://www.stepsecurity.io/blog/pinning-github-actions-for-enhanced-security-a-complete-guide) (fetched 2026-07-12) · [pydevtools.com — How to pin GitHub Actions by SHA for Python projects](https://pydevtools.com/handbook/how-to/how-to-pin-github-actions-by-sha-for-python-projects/) (fetched 2026-07-12)

**Confidence:** ✅ independently-corroborated

---

## Held pending fixes

- `ai-bom` PyPI tool for AI-specific SBOMs: only vendor PyPI page found; no independent review of its output quality as of 2026-07-12. Cited as emerging option only, not as a primary recommendation. ⚠ thin
- Model weight SHA-256 re-verification for cached files: `huggingface_hub` does not expose a `--force-verify` flag for locally cached files. Documented limitation. ⚠ PENDING

---

## CHANGELOG

Re-leveled from the 2026-07-12 technical entry; facts unchanged.

1. All technical terms defined on first use: PyPI, pip, virtual environment (venv), SHA-256, lockfile, SBOM, CycloneDX, pickle, SafeTensors, commit hash, model card, GitHub Actions, CI/CD.
2. Lead default path is one tool per practice; alternatives mentioned briefly at the end of each practice.
3. Each practice includes a plain-English "What goes wrong if you skip this" consequence.
4. All ⚠️ WARNING blocks preserved verbatim.
5. pip-audit `--dry-run` order preserved: dry-run shown before `--fix`, with explanation of why to review before applying.
6. venv activation command included for both Linux/macOS and Windows.
7. `pip lock` / `pylock.toml` distinction preserved: explicitly noted as not a drop-in for `pip install --require-hashes -r requirements.txt`.
8. All source URLs preserved as clickable Markdown links, verbatim.
9. No new facts or URLs introduced.
10. **Link-check repair:** `datacamp.com/blog/safetensors-format` returned 403 (bot-protection, confirmed live via WebFetch) — unlinked to plain text in SafeTensors practice.
11. **Link-check repair:** `mend.io/blog/over-100-malicious-packages-target-popular-ml-pypi-libraries/` returned 202 (confirmed live via WebFetch) — unlinked to plain text in PyPI vetting practice.
