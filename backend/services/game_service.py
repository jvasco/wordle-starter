from collections import Counter

from data.words import choose_random_word
from models.game import Game


def create_game(word_length: int) -> Game:
    return Game(target_word=choose_random_word(word_length))


def evaluate_guess(guess: str, target: str) -> list[str]:
    result = ["absent"] * len(target)
    remaining = Counter()

    for index, letter in enumerate(guess):
        if letter == target[index]:
            result[index] = "correct"
        else:
            remaining[target[index]] += 1

    for index, letter in enumerate(guess):
        if result[index] == "correct":
            continue
        if remaining[letter]:
            result[index] = "present"
            remaining[letter] -= 1

    return result
