#!/usr/bin/env python3
"""Render a local Hypernovelty survival card JSON file as static HTML."""

from __future__ import annotations

import html
import sys
from pathlib import Path

try:
    from validate_survival_card import load_json, validate_card
except ModuleNotFoundError:
    from scripts.validate_survival_card import load_json, validate_card


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def render_list(items: list[str]) -> str:
    if not items:
        return '<p class="empty">None listed.</p>'
    body = "\n".join(f"          <li>{esc(item)}</li>" for item in items)
    return f"<ul>\n{body}\n        </ul>"


def render_survival_card_html(card: dict[str, object]) -> str:
    sources = card["sources"]
    assert isinstance(sources, list)

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(card["title"])} - Hypernovelty Survival Card</title>
  <style>
    body {{ color: #1f2933; font-family: Arial, Helvetica, sans-serif; line-height: 1.55; margin: 0; background: #f7f8fa; }}
    main {{ max-width: 900px; margin: 0 auto; padding: 36px 20px; background: #ffffff; min-height: 100vh; }}
    header {{ border-bottom: 1px solid #d8dee6; margin-bottom: 24px; padding-bottom: 18px; }}
    h1 {{ color: #111827; line-height: 1.15; margin: 0 0 8px; }}
    h2 {{ border-bottom: 1px solid #d8dee6; color: #111827; font-size: 1.08rem; margin-top: 26px; padding-bottom: 6px; }}
    .meta {{ color: #4b5563; margin: 0; }}
    .gate {{ background: #fff7ed; border: 1px solid #fdba74; padding: 12px 14px; }}
    .boundary {{ background: #f4f7fa; border-left: 4px solid #52616f; padding: 12px 14px; }}
    .empty {{ color: #6b7280; font-style: italic; }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>{esc(card["title"])}</h1>
      <p class="meta">Card ID: {esc(card["id"])} | Domain: {esc(card["domain"])} | Audience: {esc(card["audience"])}</p>
    </header>

    <section>
      <h2>Problem</h2>
      <p>{esc(card["problem"])}</p>
    </section>

    <section>
      <h2>Practical Step</h2>
      <p>{esc(card["practical_step"])}</p>
    </section>

    <section class="gate">
      <h2>Human Gate</h2>
      <p>{esc(card["human_gate"])}</p>
    </section>

    <section>
      <h2>Caveat</h2>
      <p>{esc(card["caveat"])}</p>
    </section>

    <section>
      <h2>Sources</h2>
      {render_list(sources)}
    </section>

    <section class="boundary">
      <h2>Public-Safe Boundary</h2>
      <p>This rendered card is a local review aid. It is not legal, medical, financial, safety, emergency, policy, or professional advice.</p>
    </section>
  </main>
</body>
</html>
"""


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if len(args) != 2:
        print("usage: render_survival_card_html.py <card.json> <out.html>", file=sys.stderr)
        return 2

    input_path = Path(args[0])
    output_path = Path(args[1])
    try:
        card = load_json(input_path)
        errors = validate_card(card)
        if errors:
            for error in errors:
                print(f"error: {error}", file=sys.stderr)
            return 1
        output_path.write_text(render_survival_card_html(card), encoding="utf-8")
    except OSError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"rendered: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
