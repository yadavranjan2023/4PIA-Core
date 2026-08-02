# 4PIA: 4 People in AI (`SKILL.md` Executive Framework)

> **Operationalizing Rights-by-Design Across the C-Suite** > *Based on the theoretical framework in ["Constitutional Democracy in the Algorithmic Age: A Practical Framework for Preserving Citizen Rights"](https://link.springer.com/book/9783032346032) (Springer) by Rani Yadav-Ranjan.*

---

## 📌 Overview

As enterprise workflows transition from static automation to autonomous AI agents, standard corporate policy memos, static PDFs, and generic system prompts suffer from severe **context drift**, hallucinations, and governance failures. 

**4PIA (4 People in AI)** translates executive leadership intent into machine-executable, open-standard **`SKILL.md`** manifests. By embedding **Rights-by-Design**, explicit user consent, and zero-trust boundaries directly into runtime agent workflows, 4PIA ensures that autonomous AI copilots acting across enterprise leadership execute tasks within non-negotiable ethical, legal, and operational guardrails.

---

## 📂 Repository Structure

```text
4PIA/
├── .well-known/
│   └── skills/
│       ├── rights-by-design/
│       │   └── SKILL.md                          <-- Foundational Core Governance Skill
│       ├── 4PIA-manifests/
│       │   ├── CEO.SKILL.md                      <-- Strategy, Governance & HITL Triggers
│       │   ├── CTO.SKILL.md                      <-- Zero-Trust Architecture & Logging
│       │   ├── CPO.SKILL.md                      <-- User Rights, Consent & Accessibility
│       │   ├── CLO.SKILL.md                      <-- Real-time Compliance & Auditability
│       │   ├── CRCO.SKILL.md                     <-- Risk Management & Threat Assessment
│       │   ├── CISO.SKILL.md                     <-- Prompt Injection & DLP Defense
│       │   ├── CMO.SKILL.md                      <-- Brand Integrity & Truth in Advertising
│       │   └── CHRO.SKILL.md                     <-- Workplace Fairness & DE&I Controls
│       └── examples/
│           ├── RaniYadavRanjan.SKILL.md          <-- Constitutional Framework Core Manifest
│           └── VisionaryFounder.CEO.SKILL.md     <-- Privacy-First Founder Archetype
├── tooling/
│   └── validate_manifest.py                     <-- Manifest Linter & CI/CD Validator
├── index.php                                     <-- 4PIA.ai Landing Page Source
├── LICENSE                                       <-- Apache 2.0 License
└── README.md                                     <-- System Documentation

```

---

## 🏛️ The Extended C-Suite Suite

Every C-suite role carries distinct governance requirements. The 4PIA executive manifests inherit directly from the foundational **`rights-by-design`** skill while applying role-specific decision logic:

| Role Manifest | Primary Focus | Key Circuit Breaker |
| --- | --- | --- |
| **`CEO.SKILL.md`** | Strategic Alignment & Oversight | Halts high-risk automated workflows lacking Human-in-the-Loop (HITL) triggers. |
| **`CTO.SKILL.md`** | Zero-Trust & System Integrity | Blocks code or deployments bypassing authentication, encryption, or telemetry. |
| **`CPO.SKILL.md`** | Responsible Product & UX | Rejects dark patterns, unconsented user profiling, and non-WCAG 2.1 AA UI specs. |
| **`CLO.SKILL.md`** | Regulatory Compliance | Triggers immediate compliance blocks on non-auditable automated decision logic. |
| **`CRCO.SKILL.md`** | Enterprise Risk Management | Halts execution pipelines exceeding defined operational risk thresholds. |
| **`CISO.SKILL.md`** | Security & Prompt Injection | Blocks unauthorized privilege escalation and raw data exfiltration. |
| **`CMO.SKILL.md`** | Brand Integrity & Provenance | Flags un-substantiated marketing claims and un-labeled synthetic media. |
| **`CHRO.SKILL.md`** | Workplace Fairness | Rejects automated hiring disqualifications or terminations without human review. |

---

## 💡 Executive Manifest Examples

Explore custom governance manifests in `.well-known/skills/examples/`:

* **`RaniYadavRanjan.SKILL.md`**: The authorial manifest operationalizing the four constitutional pillars of algorithmic democracy across autonomous AI workflows.
* **`VisionaryFounder.CEO.SKILL.md`**: A consumer-tech founder archetype enforcing strict privacy-first constraints and halting surveillance ad targeting.

---

## ⚡ Two-Tier Execution Strategy

To prevent governance controls from causing operational gridlock, every 4PIA manifest utilizes a **Two-Tier Runtime Architecture**:

1. **Tier 1: Hard Circuit Breakers (Silent Background Rules)** Binary `IF/THEN` constraints that run automatically. If an agent attempts to breach user privacy, process unconsented PII, introduce dark patterns, or bypass audit logging, execution halts immediately with a compliance refusal alert.
2. **Tier 2: Dynamic Guidance (Tactical Lenses)** For routine tasks (drafting strategy, coding, evaluating vendors), the AI completes the request while automatically appending a **Governance Impact Summary** to highlight risk trade-offs and recommended mitigations.

---

## 🛠️ CI/CD & Linter Validation

This repository includes an automated linter script to ensure all `.SKILL.md` manifests adhere to valid YAML frontmatter formatting and markdown structural standards.

### Running the Linter Locally

```bash
python tooling/validate_manifest.py

```

### GitHub Actions Integration

To enforce manifest validity across pull requests, add the following workflow to `.github/workflows/validate.yml`:

```yaml
name: Validate 4PIA Manifests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Run Manifest Linter
        run: python tooling/validate_manifest.py

```

---

## 📖 Theoretical Foundation & Citation

The 4PIA framework is built upon the academic principles established in:

> **Yadav-Ranjan, R.** (2023). *Constitutional Democracy in the Algorithmic Age: A Practical Framework for Preserving Citizen Rights*. Springer.
> **ISBN:** 978-3-032-34603-2
> **Link:** [https://link.springer.com/book/9783032346032](https://link.springer.com/book/9783032346032)

---

## 📄 License

This repository is open-source software licensed under the [Apache 2.0 License](https://www.google.com/search?q=LICENSE).
