import unittest

from scripts.render_survival_card_html import render_survival_card_html


def valid_card() -> dict[str, object]:
    return {
        "id": "example-001",
        "title": "Example",
        "domain": "ai-readiness",
        "audience": "Small teams",
        "problem": "A fast-moving claim may be used before it is checked.",
        "practical_step": "Name the decision and source check before use.",
        "caveat": "Synthetic example only.",
        "human_gate": "A named reviewer signs off before public use.",
        "sources": ["https://example.org/public-source"],
    }


class SurvivalCardRenderTest(unittest.TestCase):
    def test_render_includes_core_sections(self):
        output = render_survival_card_html(valid_card())

        self.assertIn("<h2>Problem</h2>", output)
        self.assertIn("<h2>Practical Step</h2>", output)
        self.assertIn("<h2>Human Gate</h2>", output)
        self.assertIn("Public-Safe Boundary", output)

    def test_render_escapes_card_content(self):
        card = valid_card()
        card["title"] = "Example <unsafe>"
        card["problem"] = "Avoid <script>alert('x')</script> content."

        output = render_survival_card_html(card)

        self.assertIn("Example &lt;unsafe&gt;", output)
        self.assertIn("&lt;script&gt;alert(&#x27;x&#x27;)&lt;/script&gt;", output)
        self.assertNotIn("<script>alert", output)


if __name__ == "__main__":
    unittest.main()
