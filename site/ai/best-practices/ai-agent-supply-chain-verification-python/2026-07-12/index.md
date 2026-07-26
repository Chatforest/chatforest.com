# AI Agent Supply Chain Verification — Python Ecosystem (as of 12 Jul 2026)

> How Python developers building or running AI agents verify the safety and integrity of their Python dependency supply chain — covering PyPI vetting, hash-pinning, vulnerability scanning, SBOM generation, model file integrity, and CI supply chain hardening.


<!-- Immutable dated snapshot. A refresh is a NEW snapshot-date dir. "Latest" computed by Grove's template. -->

# AI Agent Supply Chain Verification — Python Ecosystem (as of 12 Jul 2026)

> **Grading note.** A dated snapshot — accurate as of **12 Jul 2026**, frozen here as a permanent archive entry. Graded by the 3-lens panel (Skeptic/Beginner/Timekeeper) + sensei on 2026-07-15. Corrections applied inline; unverifiable gaps marked ⚠ PENDING (#issue) — never guessed.

## How to read the labels
- ✅ **independently-corroborated** — 2+ independent publishers
- 📄 **vendor-documented** — official docs only (authoritative, single source)
- ⚠️ **WARNING** — a default that can cost money, break the machine, or remove a safety net
- 🕒 **verify live** — fast-moving (versions/prices/quotas); check the current value

---

## Practice: Vet a PyPI package before installing it into an AI project

**Do:** Before running `pip install <package>`, check the package on [pypi.org](https://pypi.org): confirm the exact name matches what you intended (watch for one-letter swaps like "langchaln"), look at the maintainer account age and publish history, and note download volume. New maintainer accounts with a single release and a high-profile name are a documented attack pattern. PyPI now auto-flags suspected typosquats at upload time, but that happens on their side — you must still look before installing.

**Why:** Anyone can publish to PyPI with no gatekeeping. Attackers register names one character off from popular AI libraries (e.g. `PyToich` instead of `PyTorch`, `transformers-dev` instead of `transformers`) and embed credential-stealing code that runs silently at install time via `setup.py` hooks. Mend.io documented more than 100 such packages targeting ML developers in a single campaign (March 2024), and a 2026 incident compromised the legitimate `pytorch-lightning` package itself (versions 2.6.2 and 2.6.3), stealing cloud credentials from AWS, Azure, and GCP through a hidden `_runtime` directory containing a staged downloader. 🕒 **verify live** — confirm the affected version numbers against current Sonatype advisory.

**Caveat / contested:** PyPI's automated typosquat detection only fires at project creation — it does not re-scan existing packages after maintainer handoffs or account compromises. A package that was clean yesterday can be malicious today. Popularity and download counts are lagging indicators: compromised trusted packages (not just fakes) are the dominant threat vector as of 2026.

**Sources:**
[blog.pypi.org — PyPI 2025 Year in Review](https://blog.pypi.org/posts/2025-12-31-pypi-2025-in-review/) (31 Dec 2025) · [sonatype.com — Malicious PyTorch Lightning Packages Found on PyPI](https://www.sonatype.com/blog/malicious-pytorch-lightning-packages-found-on-pypi) (2026) · mend.io — Over 100 Malicious Packages Target Popular ML PyPI Libraries (28 Mar 2024; confirmed live, non-200 response)

**Confidence:** independently-corroborated

---

## Practice: Pin every dependency to an exact version and add SHA-256 hashes

**Do:** Install [pip-tools](https://pypi.org/project/pip-tools/) (v7.5.3, 11 Feb 2026 — 🕒 verify live) with `pip install pip-tools`, then use `pip-compile --generate-hashes` to produce a `requirements.txt` that contains exact versions (`==`) and per-file `sha256:` hashes for every direct and transitive dependency. Deploy with `pip install --require-hashes -r requirements.txt`.

For new projects preferring speed, `uv pip compile` provides the same output. `pip lock` (experimental, pip 25.1+) is an emerging alternative but produces `pylock.toml` (PEP 751 format), which cannot be consumed by `pip install --require-hashes -r requirements.txt` — it requires a compatible installer. Use `pip-compile` if you need `--require-hashes` today.

**Why:** Without hashes, a `pip install` that looks identical today can silently pull a different (potentially malicious) package tomorrow — because PyPI lets maintainers upload new releases at any time. `--require-hashes` makes pip reject any downloaded wheel or sdist whose SHA-256 does not match the value embedded in your lockfile, catching both network tampering and package-repository compromises.

⚠️ **WARNING:** `--require-hashes` requires hashes for *all* packages, including transitive ones. A partially-hashed file is treated as an error; use `pip-compile` to generate a complete set rather than adding hashes by hand.

**Caveat / contested:** Hash-pinned lockfiles are platform-specific (different wheels ship for Linux vs macOS vs Windows). Teams building multi-platform AI pipelines sometimes maintain per-platform lockfiles or use Docker images to sidestep the mismatch.

**Sources:**
[pip.pypa.io — Secure installs (pip v26.1.2)](https://pip.pypa.io/en/stable/topics/secure-installs/) (fetched 2026-07-12) · [pip-tools.readthedocs.io — pip-compile CLI](https://pip-tools.readthedocs.io/en/stable/cli/pip-compile/) (fetched 2026-07-12) · [pydevtools.com — pip-tools reference](https://pydevtools.com/handbook/reference/pip-tools/) (2 Jul 2026)

**Confidence:** independently-corroborated

---

## Practice: Scan AI dependencies for known vulnerabilities with pip-audit

**Do:** Install [pip-audit](https://pypi.org/project/pip-audit/) (maintained by PyPA with Trail of Bits and Google; latest v2.10.1, 10 Jun 2026 — 🕒 verify live) and run it before every deployment and in CI:

```bash
pip install pip-audit
# Scan in development
pip-audit --dry-run -r requirements.txt   # preview proposed fixes first
pip-audit --fix -r requirements.txt       # then apply
# Scan in CI / pre-deployment
pip-audit -r requirements.txt
```

Always use `--dry-run` before `--fix` to review proposed changes — auto-upgrades to `torch` or `transformers` can break model environments. `pip-audit` queries the PyPI advisory database, OSV, and ESMS services for CVEs and advisories affecting packages such as `transformers`, `langchain`, `openai`, and `anthropic`.

**Why:** Popular AI libraries have complex dependency trees. A CVE in a transitive dependency (e.g., a vulnerable version of `requests` pulled in by `openai`) will not show up unless you scan the full resolved environment. `pip-audit` recurses into transitive dependencies and reports all known advisories in one pass.

**Caveat / contested:** `pip-audit` (and the similar `safety` tool) are *reactive* — they only catch vulnerabilities that have already been disclosed and indexed. They will not flag a freshly compromised or novel malicious package. The `safety` CLI (v3.8.1, May 2026) offers broader coverage through Safety DB, but the commercial database behind it requires a paid plan for complete data. Neither tool substitutes for hash-pinning or behavioral monitoring.

**Sources:**
[github.com/pypa/pip-audit](https://github.com/pypa/pip-audit) (fetched 2026-07-12; latest release v2.10.1, 10 Jun 2026) · [pypi.org/project/pip-audit](https://pypi.org/project/pip-audit/) (fetched 2026-07-12) · [pypi.org/project/safety](https://pypi.org/project/safety/) (fetched 2026-07-12; v3.8.1, 29 May 2026)

**Confidence:** independently-corroborated

---

## Practice: Generate and maintain an SBOM for every AI project release

**Do:** Run `cyclonedx-py environment` (from [cyclonedx-bom](https://pypi.org/project/cyclonedx-bom/) v7.3.0, 30 Mar 2026 — 🕒 verify live) against your virtual environment to produce a CycloneDX SBOM in JSON or XML. Commit the SBOM alongside each release. `pip-audit` can also emit CycloneDX output directly with `--format cyclonedx-json`. For AI-specific component inventories (model weights, adapters, datasets), the experimental `ai-bom` tool on PyPI is an emerging option, though it is thin on independent documentation as of this snapshot.

**Why:** An SBOM is an itemized list of every library your AI agent depends on, including indirect dependencies. OWASP's LLM03:2025 guidance explicitly recommends maintaining signed, tamper-resistant SBOMs for LLM supply chains. Regulators are beginning to require them: the EU AI Act (Article 11/Annex IV, component inventory requirements, effective August 2025 for new placements; existing models placed before 2 August 2025 have until 2 August 2027) calls for a complete AI component inventory.

**Caveat / contested:** The OpenSSF blog (Jun 2025) notes that SBOM tooling is still maturing — "imperfect SBOMs are better than no SBOMs." For Python, CycloneDX-Python is the most complete tool for standard library dependencies, but it does not natively capture model weight files, dataset lineage, or LoRA adapters. Those require either manual entries or AI-BOM tooling that is not yet independently validated at this snapshot's date.

**Sources:**
[github.com/CycloneDX/cyclonedx-python](https://github.com/CycloneDX/cyclonedx-python) (fetched 2026-07-12; v7.3.0, 30 Mar 2026) · [openssf.org — Choosing an SBOM Generation Tool](https://openssf.org/blog/2025/06/05/choosing-an-sbom-generation-tool/) (5 Jun 2025) · [genai.owasp.org — LLM03:2025 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) (fetched 2026-07-12)

**Confidence:** independently-corroborated

---

## Practice: Prefer SafeTensors format over pickle when downloading model weights

**Do:** When downloading models from Hugging Face, prefer `.safetensors` files over `.bin` or `.pt` (pickle) files. In `transformers`, pass `use_safetensors=True` to `from_pretrained()`. If a model is only available in pickle format, use Hugging Face's import scan results (shown on the Hub file page) and scan with [fickling](https://github.com/trailofbits/fickling) or [ModelScan](https://github.com/protectai/modelscan) before loading.

⚠️ **WARNING:** Simply calling `torch.load("model.bin")` on a file from an untrusted source executes arbitrary Python code embedded in the file.

**Why:** Python's pickle format allows the serialized file itself to run code when you load it. A malicious `.pt` file can steal API keys, write backdoors, or download further payloads — all triggered by one `torch.load()` call. SafeTensors stores only raw tensor data with no executable code. The format joined the PyTorch Foundation (Linux Foundation) in April 2026, signaling broad ecosystem adoption.

**Caveat / contested:** Hugging Face's Hub pickle-import scanner (shown per-file on the website) is not 100% foolproof by their own admission — it is "maintained in a best-effort manner." In February 2025, researchers found that some malicious `.bin` files compressed with 7z instead of ZIP bypassed PickleScan, the primary Hub scanner (ReversingLabs nullifAI research). SafeTensors avoids the problem entirely rather than patching around it; however, some older or quantized model releases only ship pickle files and have no SafeTensors alternative.

**Sources:**
[huggingface.co/docs/hub/en/security-pickle](https://huggingface.co/docs/hub/en/security-pickle) (fetched 2026-07-12) · datacamp.com — SafeTensors Format (fetched 2026-07-12; confirmed live, bot-protection 403)

**Confidence:** independently-corroborated

---

## Practice: Pin Hugging Face downloads to a specific commit hash and verify the model card

**Do:** When using `hf_hub_download()` or `snapshot_download()`, supply the `revision` parameter with a full commit hash (e.g., `revision="877b84a8f93f2d619faa2a6e514a32beef88ab0a"`). Do not rely on `main` branch or floating tags in production. Before using any model, read its model card (the `README.md` in the repo): check the `license`, `datasets`, and `base_model` fields, and look for structured evaluation results. Prefer models from verified organizations (blue badge on the Hub) and flag any model where the publishing account was registered less than 30 days ago.

**Why:** A Hugging Face model repo's `main` branch can be updated at any time by its owner. Pinning to a commit hash gives you the exact weights you tested. The model card's `datasets` field reveals training data provenance — relevant for license compliance and data poisoning risk. The `license` field is machine-readable and governs whether you can use the model commercially. OWASP LLM03:2025 specifically names third-party model repositories as a supply chain attack vector.

**Caveat / contested:** `hf_hub_download()` checks server-provided checksums during download when they are available, but does not re-verify files already in the local cache on subsequent runs. Model cards are author-supplied and not independently audited; the presence of a safety evaluation section varies widely across the Hub. Pinning to a commit hash does not prove the weights are safe — it only proves you will load the same file every time.

**Sources:**
[huggingface.co/docs/huggingface_hub/guides/download](https://huggingface.co/docs/huggingface_hub/guides/download) (fetched 2026-07-12) · [huggingface.co/docs/hub/model-cards](https://huggingface.co/docs/hub/model-cards) (fetched 2026-07-12) · [beyondscale.tech — Open Source AI Model Security: Vetting Hugging Face Downloads](https://beyondscale.tech/blog/open-source-ai-model-security-hugging-face) (30 Apr 2026)

**Confidence:** independently-corroborated

---

## Practice: Pin GitHub Actions to full-length commit SHAs in AI project CI workflows

**Do:** Replace floating tag references in your `.github/workflows/` files with the corresponding full 40-character commit SHA. For example, replace `uses: actions/checkout@v4` with the SHA for the specific tag you need — look it up with `git ls-remote https://github.com/actions/checkout refs/tags/<tag>` without cloning. Note: `actions/checkout` is currently at **v7.0.0** (June 2026) — the SHA in your workflow should correspond to the version you have reviewed. This example is **illustrative; always look up the current SHA** rather than copying it from documentation.

For projects with many actions, use [pinact](https://github.com/suzuki-shunsuke/pinact) to automate the conversion. Configure Dependabot (`package-ecosystem: "github-actions"`) to open PRs when pinned SHAs have newer releases.

**Why:** A tag in a GitHub Actions workflow is mutable — a bad actor who compromises the action repository can move the tag to malicious code and your workflow will silently run that code on the next trigger. In March 2025, the `tj-actions/changed-files` action was compromised this way; more than 350 tags were updated to dump CI secrets, affecting over 23,000 repositories. Workflows pinned to SHAs were completely unaffected because the SHA could not be moved. GitHub now supports org-level policies that fail any workflow using non-SHA-pinned actions.

**Caveat / contested:** SHA pinning trades a small convenience cost (needing to look up the SHA and keep it updated) for strong security. The main operational risk is forgetting to update pinned SHAs when new secure releases ship — this is why Dependabot automation is recommended alongside pinning, not instead of it.

**Sources:**
[docs.github.com/en/actions/reference/security/secure-use](https://docs.github.com/en/actions/reference/security/secure-use) (fetched 2026-07-12) · [stepsecurity.io — Pinning GitHub Actions for Enhanced Security](https://www.stepsecurity.io/blog/pinning-github-actions-for-enhanced-security-a-complete-guide) (fetched 2026-07-12) · [pydevtools.com — How to pin GitHub Actions by SHA for Python projects](https://pydevtools.com/handbook/how-to/how-to-pin-github-actions-by-sha-for-python-projects/) (fetched 2026-07-12)

**Confidence:** independently-corroborated

---

## Practice: Use an isolated virtual environment per AI project; never install AI packages system-wide

**Do:** Create a dedicated virtual environment for every AI project and activate it before any `pip install`:

```bash
python -m venv .venv
source .venv/bin/activate       # Linux / macOS
# .venv\Scripts\activate        # Windows
```

Alternatively, `uv venv && source .venv/bin/activate`. Use the lockfile from `pip-compile` (or `uv lock`) to ensure the environment is reproducible. For deployed agents, prefer Docker containers over bare virtual environments, since containers add network and filesystem isolation that venvs do not provide.

**Why:** AI libraries such as `torch`, `transformers`, and `langchain` pull in dozens of transitive dependencies. Installing them globally can break system tools and makes it impossible to reproduce the exact environment later. A malicious package installed into a shared environment can reach other projects' files and credentials. Virtual environments enforce dependency isolation at the project level.

⚠️ **WARNING:** A virtual environment does *not* sandbox network access or filesystem writes — a malicious package running inside a venv can still exfiltrate secrets. For untrusted code or agent execution, use Docker or a dedicated sandbox.

**Caveat / contested:** Virtual environments isolate Python packages but share the underlying OS and network. For AI agents that execute code as part of their task loop, security researchers and sandbox providers (E2B, Modal, Northflank) consistently recommend container-level or VM-level isolation in addition to venvs. Virtual environments alone are a necessary but insufficient security boundary for production AI agents.

**Sources:**
[pip.pypa.io — Repeatable Installs (pip v26.1.2)](https://pip.pypa.io/en/stable/topics/repeatable-installs/) (fetched 2026-07-12) · [pydevtools.com — pip-tools reference](https://pydevtools.com/handbook/reference/pip-tools/) (2 Jul 2026)

**Confidence:** vendor-documented

---

## Held pending fixes

- `ai-bom` PyPI tool for AI-specific SBOMs: only vendor PyPI page found; no independent review of its output quality as of 2026-07-12. Cited as emerging option only, not as a primary recommendation. ⚠ thin
- Model weight SHA-256 re-verification for cached files: `huggingface_hub` does not expose a `--force-verify` flag for locally cached files. Documented limitation. ⚠ PENDING

## CHANGELOG

1. **Timekeeper KILL-3:** `pip lock` / `pylock.toml` (PEP 751) clarified — it is NOT a drop-in for `pip install --require-hashes -r requirements.txt`. pip-compile remains the recommended path for `--require-hashes` workflows.
2. **Beginner KILL-PY-1:** `pip-audit --dry-run` moved to lead position, `--fix` noted as the follow-up after reviewing proposed changes. Prevents beginners from auto-upgrading and breaking model environments.
3. **Beginner FIX-PY-1:** pip-tools install step (`pip install pip-tools`) added before `pip-compile` example.
4. **Beginner FIX-PY-2:** venv activation command added (`source .venv/bin/activate` for Linux/macOS, `.venv\Scripts\activate` for Windows).
5. **Timekeeper FIX-1:** pip-tools v7.5.3 date corrected to 11 February 2026 (was transposed from pip-audit v2.10.1's 10 June 2026 release date).
6. **Timekeeper FIX-2:** `actions/checkout` SHA example updated to reference v7.0.0 (June 2026). Added permanent note that any SHA example is illustrative and must be looked up at deployment time.
7. **Timekeeper FIX-4:** pytorch-lightning attack mechanism corrected from "modified `__init__.py`" to "hidden `_runtime` directory with a staged downloader." Added 🕒 verify live for version numbers.
8. **Skeptic FIX:** PickleScan 7z-bypass date corrected to February 2025 (ReversingLabs nullifAI); source was mis-dated as "In 2026."
9. **Skeptic FIX:** "~65% of cards" safety-eval completeness figure removed — absent from the cited arXiv 2402.05160 paper.
10. **Skeptic FIX:** "compromised trusted packages dominant vector" claim unquoted and reframed as observation (wording not found in the cited PyPI 2025 Year in Review).
11. **Skeptic / Timekeeper FIX:** EU AI Act reference updated — Article 11/Annex IV for component inventory (not Article 53); existing models (pre-Aug 2025) have until 2027.
12. **Timekeeper FIX-7:** EU AI Act effective date caveat added — August 2025 applies to new placements; pre-existing models have a two-year grace period (until 2027).
13. **Link-check repair:** `datacamp.com/blog/safetensors-format` returned 403 (bot-protection, confirmed live via WebFetch) — unlinked to plain text in SafeTensors practice.
14. **Link-check repair:** `mend.io/blog/over-100-malicious-packages-target-popular-ml-pypi-libraries/` returned 202 (confirmed live via WebFetch) — unlinked to plain text in PyPI vetting practice.

