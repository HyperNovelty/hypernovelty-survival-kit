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
    body = "\n".join(f"            <li>{esc(item)}</li>" for item in items)
    return f'<ul class="check-list">\n{body}\n          </ul>'


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
    :root {{ color-scheme: dark; --ink: #f7ead7; --muted: #d7c2a2; --paper: #fff7e8; --paper-ink: #261b12; --line: #6f5840; --accent: #f2b66d; --good: #b9d38b; --warn: #ffd08a; --panel: #352417; }}
    * {{ box-sizing: border-box; }}
    body {{ color: var(--ink); font-family: Georgia, "Times New Roman", serif; line-height: 1.6; margin: 0; background: #20150f; }}
    body::before {{ content: ""; position: fixed; inset: 0; pointer-events: none; background: radial-gradient(circle at top left, rgba(242, 182, 109, 0.16), transparent 34rem); }}
    main {{ max-width: 1080px; margin: 0 auto; padding: 32px 18px 44px; position: relative; }}
    header {{ border: 1px solid var(--line); border-radius: 8px; margin-bottom: 18px; padding: 24px; background: linear-gradient(135deg, #3a2617, #251810); box-shadow: 0 18px 50px rgba(0,0,0,0.25); }}
    h1 {{ color: var(--ink); font-size: clamp(2rem, 5vw, 4rem); line-height: 0.98; margin: 10px 0 14px; letter-spacing: 0; }}
    h2 {{ color: var(--paper-ink); font-size: 1.02rem; line-height: 1.2; margin: 0 0 10px; }}
    p {{ margin: 0; }}
    .eyebrow {{ color: var(--accent); font-family: Arial, Helvetica, sans-serif; font-size: 0.78rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }}
    .meta-grid {{ display: grid; gap: 12px; grid-template-columns: repeat(3, minmax(0, 1fr)); margin: 18px 0; }}
    .meta-card, section {{ background: var(--paper); border: 1px solid #dfcaa8; border-radius: 8px; color: var(--paper-ink); padding: 18px; }}
    .meta-card dt {{ color: #735230; font-family: Arial, Helvetica, sans-serif; font-size: 0.72rem; font-weight: 700; text-transform: uppercase; }}
    .meta-card dd {{ margin: 4px 0 0; font-weight: 700; }}
    .section-grid {{ display: grid; gap: 14px; grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    .section-grid section.wide {{ grid-column: 1 / -1; }}
    .chips {{ display: flex; flex-wrap: wrap; gap: 8px; }}
    .chip {{ border: 1px solid rgba(255,255,255,0.28); border-radius: 999px; color: var(--ink); display: inline-flex; font-family: Arial, Helvetica, sans-serif; font-size: 0.78rem; font-weight: 700; padding: 6px 10px; }}
    .chip.good {{ background: rgba(185, 211, 139, 0.18); color: #edf6d2; }}
    .chip.warn {{ background: rgba(255, 208, 138, 0.18); color: #ffe2ac; }}
    .check-list {{ margin: 0; padding-left: 1.2rem; }}
    .check-list li {{ margin: 0.45rem 0; padding-left: 0.15rem; }}
    .gate {{ border-color: #d99745; background: #fff1d6; }}
    .boundary {{ background: #302117; border-color: var(--line); color: var(--ink); margin-top: 14px; }}
    .boundary h2 {{ color: var(--accent); }}
    .empty {{ color: #7a6a55; font-style: italic; }}
    footer {{ color: var(--muted); font-family: Arial, Helvetica, sans-serif; font-size: 0.9rem; margin-top: 18px; }}
    @media (max-width: 760px) {{ .meta-grid, .section-grid {{ grid-template-columns: 1fr; }} header {{ padding: 20px; }} }}
    @media print {{ body {{ background: #fff; color: #000; }} body::before {{ display: none; }} main {{ max-width: none; padding: 0; }} header, section, .meta-card {{ box-shadow: none; break-inside: avoid; }} .boundary {{ color: #000; background: #fff; }} }}
  </style>
</head>
<body>
  <main>
    <header>
      <p class="eyebrow">Hypernovelty Open Lab / Survival Card</p>
      <h1>{esc(card["title"])}</h1>
      <div class="chips" aria-label="Artifact status">
        <span class="chip good">Synthetic example</span>
        <span class="chip warn">Human gate required</span>
        <span class="chip">Local review aid</span>
      </div>
    </header>

    <dl class="meta-grid" aria-label="Card metadata">
      <div class="meta-card"><dt>Card ID</dt><dd>{esc(card["id"])}</dd></div>
      <div class="meta-card"><dt>Domain</dt><dd>{esc(card["domain"])}</dd></div>
      <div class="meta-card"><dt>Audience</dt><dd>{esc(card["audience"])}</dd></div>
    </dl>

    <div class="section-grid">
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

      <section class="wide">
        <h2>Sources</h2>
        {render_list(sources)}
      </section>
    </div>

    <section class="boundary">
      <h2>Public-Safe Boundary</h2>
      <p>This rendered card is a local synthetic review aid. It is not legal, medical, financial, safety, emergency, policy, or professional advice, and it does not approve public use.</p>
    </section>
    <footer>Rendered without external assets, tracking, or network calls.</footer>
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
