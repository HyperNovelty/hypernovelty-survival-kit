import unittest
from pathlib import Path

from scripts.validate_survival_card import load_json, validate_card


class SurvivalCardValidationTest(unittest.TestCase):
    def test_example_card_is_valid(self):
        repo_root = Path(__file__).resolve().parents[1]
        card = load_json(repo_root / "examples" / "survival-card.example.json")

        self.assertEqual(validate_card(card), [])


if __name__ == "__main__":
    unittest.main()
