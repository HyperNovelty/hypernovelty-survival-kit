# Contributing

Contributions should make the kit clearer, safer, easier to validate, or more useful for public education and research.

## Good Contributions

- Improve plain-language explanations.
- Add small checklists with clear human review gates.
- Add examples that use public, non-sensitive information.
- Improve validation without adding unnecessary dependencies.
- Clarify boundaries where a reader might over-trust a tool.

## Boundaries

Do not contribute credentials, private data, account details, client material, student records, unpublished private work, internal roadmaps, or sensitive operational procedures.

Do not present checklist content as legal, medical, financial, emergency, or safety advice. Use qualified local experts for high-stakes situations.

## Style

Keep copy sober, practical, and public-good oriented. Prefer short checklists over manifestos. Name uncertainty directly. Include sources when a claim depends on outside information.

## Local Validation

Run:

```bash
python3 scripts/validate_survival_card.py examples/survival-card.example.json
python3 -m unittest discover -s tests
```
