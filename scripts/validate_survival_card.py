#!/usr/bin/env python3
"""Validate a Hypernovelty survival card using Python stdlib only."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = (
    "id",
    "title",
    "domain",
    "audience",
    "problem",
    "practical_step",
    "caveat",
    "human_gate",
    "sources",
)


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_card(card: Any) -> list[str]:
    """Return a list of validation errors. An empty list means valid."""
    errors: list[str] = []

    if not isinstance(card, dict):
        return ["card must be a JSON object"]

    for field in REQUIRED_FIELDS:
        if field not in card:
            errors.append(f"missing required field: {field}")

    for field in REQUIRED_FIELDS:
        if field == "sources" or field not in card:
            continue
        if not _is_non_empty_string(card[field]):
            errors.append(f"{field} must be a non-empty string")

    sources = card.get("sources")
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
    elif not all(_is_non_empty_string(source) for source in sources):
        errors.append("sources items must be non-empty strings")

    return errors


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 1:
        print("usage: validate_survival_card.py <path-to-card.json>", file=sys.stderr)
        return 2

    path = Path(args[0])
    try:
        card = load_json(path)
    except FileNotFoundError:
        print(f"error: file not found: {path}", file=sys.stderr)
        return 2
    except json.JSONDecodeError as exc:
        print(f"error: invalid JSON in {path}: {exc}", file=sys.stderr)
        return 1

    errors = validate_card(card)
    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        return 1

    print(f"valid: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
