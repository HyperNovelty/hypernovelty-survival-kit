# Hypernovelty Survival Kit

Practical tools for staying oriented when AI, climate, media, education, markets, and institutions change faster than normal playbooks can update.

This repository is the umbrella map for a small Hypernovelty Open Lab public proof footprint. It is designed to show practical review habits, not to claim certification, compliance coverage, or proprietary AWSE internals.

## What Hypernovelty Means

Hypernovelty is the condition of facing many new, fast-changing situations at once. The tools, habits, and institutions people normally rely on may still matter, but they may not update quickly enough for the current environment.

This kit treats hypernovelty as a practical problem: people need better questions, clear boundaries, visible sources, human review gates, and small checklists that can be used before decisions get expensive or hard to reverse.

## Who This Kit Helps

This starter repo is for teachers, parents, students, small teams, journalists, community groups, founders, public-interest researchers, and anyone trying to make sense of fast-moving change without turning uncertainty into hype.

It is designed for lightweight use: read a domain note, copy a checklist, adapt a survival card, and keep a human accountable for the final decision.

## Domains Covered

- AI readiness
- Agent workflow safety
- Education and kids
- Source and provenance literacy
- Climate adaptation signals
- Quantum literacy and hype triage
- Forecast discipline and uncertainty
- Memory, identity, and governance
- Small-business AI workflow safety
- Human review gates

## Quick Start

Open `START_HERE.html` in a browser for a readable map of the repo.

Review the domain notes in `docs/`, then choose a checklist in `kits/`:

- `kits/school-ai-readiness/checklist.md`
- `kits/small-business-ai-workflow-safety/checklist.md`
- `kits/source-provenance-literacy/checklist.md`
- `kits/climate-signal-checklist/checklist.md`
- `kits/quantum-hype-triage/checklist.md`

Create or adapt a survival card using:

- `schemas/survival-card.schema.json`
- `examples/survival-card.example.json`
- `examples/rendered/survival-card.example.html`

Read `docs/open-lab-positioning.md` for project positioning, `docs/OSS_PORTFOLIO_MAP.md` for the current ten-repo public portfolio map, and `docs/CLAUDE_FOR_OSS_EVIDENCE.md` for truthful Claude for OSS evidence notes.

## Run Validation

This repo uses Python standard library only.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_survival_card.py examples/survival-card.example.json
PYTHONDONTWRITEBYTECODE=1 python3 scripts/render_survival_card_html.py examples/survival-card.example.json examples/rendered/survival-card.example.html
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
```

The validator checks that a survival card has the required public fields and that `sources` is a non-empty list. The renderer writes a local static HTML review page that can be opened in a browser.

## What This Repo Does Not Do

This repo does not provide legal, medical, financial, safety, or emergency advice. It does not replace teachers, local officials, licensed professionals, emergency services, or domain experts. It does not certify that a technology, source, claim, workflow, school policy, business process, or climate decision is safe.

It also does not make predictions for you. It helps you slow down, name uncertainty, check sources, and decide where human review is required.

## Public-Safe Boundaries

Use this repo for education and research. Treat every checklist as a starting point, not an authority. For high-stakes decisions, consult qualified local experts and applicable rules in your jurisdiction.

Do not put private data, student records, client data, credentials, secrets, unpublished material, or sensitive operational details into public survival cards.

## Related Public Hypernovelty Repos

Current ten-repo OSS footprint:

- [hypernovelty-survival-kit](https://github.com/HyperNovelty/hypernovelty-survival-kit) — umbrella map and survival/checklist kit.
- [agent-run-receipts](https://github.com/HyperNovelty/agent-run-receipts) — AI/coding-agent accountability receipts.
- [ai-workflow-safety-screen](https://github.com/HyperNovelty/ai-workflow-safety-screen) — review-gate screens for AI-involved workflows.
- [source-card-schema](https://github.com/HyperNovelty/source-card-schema) — portable source/claim cards.
- [hypernovelty-verification-literacy-kit](https://github.com/HyperNovelty/hypernovelty-verification-literacy-kit) — verification mini-labs.
- [ai-school-readiness-kit](https://github.com/HyperNovelty/ai-school-readiness-kit) — school AI readiness cards and checklists.
- [surviving-hypernovelty](https://github.com/HyperNovelty/surviving-hypernovelty) — companion orientation materials.
- [agent-policy-cards](https://github.com/HyperNovelty/agent-policy-cards) — agent boundary/policy card fixtures.
- [education-adaptation-cards](https://github.com/HyperNovelty/education-adaptation-cards) — education adaptation card examples.
- [ipublishos-source-research-intake](https://github.com/HyperNovelty/ipublishos-source-research-intake) — source/research intake workflows.

See `docs/OSS_PORTFOLIO_MAP.md` for the organized map.

## License

This starter repo is released under the MIT License. See `LICENSE`.
