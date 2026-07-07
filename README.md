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

Read `docs/open-lab-positioning.md` for how this umbrella kit relates to the five satellite public proof repos.

## Run Validation

This repo uses Python standard library only.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_survival_card.py examples/survival-card.example.json
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests
```

The validator checks that a survival card has the required public fields and that `sources` is a non-empty list.

There is no renderer in this umbrella repo. The satellite repos include renderers where a structured review artifact benefits from a static HTML view.

## What This Repo Does Not Do

This repo does not provide legal, medical, financial, safety, or emergency advice. It does not replace teachers, local officials, licensed professionals, emergency services, or domain experts. It does not certify that a technology, source, claim, workflow, school policy, business process, or climate decision is safe.

It also does not make predictions for you. It helps you slow down, name uncertainty, check sources, and decide where human review is required.

## Public-Safe Boundaries

Use this repo for education and research. Treat every checklist as a starting point, not an authority. For high-stakes decisions, consult qualified local experts and applicable rules in your jurisdiction.

Do not put private data, student records, client data, credentials, secrets, unpublished material, or sensitive operational details into public survival cards.

## Related Public Hypernovelty Repos

Six-repo proof footprint:

- [hypernovelty-survival-kit](https://github.com/HyperNovelty/hypernovelty-survival-kit)
- [agent-run-receipts](https://github.com/HyperNovelty/agent-run-receipts)
- [ai-workflow-safety-screen](https://github.com/HyperNovelty/ai-workflow-safety-screen)
- [source-card-schema](https://github.com/HyperNovelty/source-card-schema)
- [hypernovelty-verification-literacy-kit](https://github.com/HyperNovelty/hypernovelty-verification-literacy-kit)
- [ai-school-readiness-kit](https://github.com/HyperNovelty/ai-school-readiness-kit)

Adjacent public projects:

- [agent-policy-cards](https://github.com/HyperNovelty/agent-policy-cards)
- [education-adaptation-cards](https://github.com/HyperNovelty/education-adaptation-cards)
- [ipublishos-source-research-intake](https://github.com/HyperNovelty/ipublishos-source-research-intake)
- [surviving-hypernovelty](https://github.com/HyperNovelty/surviving-hypernovelty)

## License

This starter repo is released under the MIT License. See `LICENSE`.
