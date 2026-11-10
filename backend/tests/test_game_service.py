import unittest
from services.game_service import evaluate_guess

class EvaluateGuessTests(unittest.TestCase):
    def test_duplicate_letters_only_match_available_letters(self):
        self.assertEqual(
            evaluate_guess("allee", "apple"),
            ["correct", "present", "absent", "absent", "correct"],
        )

    def test_exact_matches_take_priority(self):
        self.assertEqual(
            evaluate_guess("eerie", "serve"),
            ["absent", "correct", "correct", "absent", "correct"],
        )

    def test_crane_with_eerie_has_expected_pattern(self):
        # EERIE against CRANE -> X X Y X G
        self.assertEqual(
            evaluate_guess("eerie", "crane"),
            ["absent", "absent", "present", "absent", "correct"],
        )


if __name__ == "__main__":
    unittest.main()
