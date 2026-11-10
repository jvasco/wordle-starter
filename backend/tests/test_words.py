import unittest

from data.words import WORDS_BY_LENGTH


class WordListTests(unittest.TestCase):
    def test_words_are_unique(self):
        words = [
            word
            for words_of_length in WORDS_BY_LENGTH.values()
            for word in words_of_length
        ]
        self.assertEqual(len(words), len(set(words)))

    def test_words_match_their_configured_length(self):
        for expected_length, words in WORDS_BY_LENGTH.items():
            for word in words:
                with self.subTest(word=word, expected_length=expected_length):
                    self.assertEqual(len(word), expected_length)


if __name__ == "__main__":
    unittest.main()
