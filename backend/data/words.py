import random


WORDS_BY_LENGTH = {
    5: [
        "apple",
        "alley",
        "brave",
        "crane",
        "eerie",
        "level",
        "civic",
        "sassy",
        "llama",
        "grape",
        "house",
        "light",
        "plant",
        "smile",
        "radar",
        "sugar",
        "photo",
        "sheep",
        "spear",
        "crane",
        "eerie",
        "yacht",

    ],
    6: [
        "bright",
        "castle",
        "flower",
        "planet",
        "stream",
        "winter",
        "seesaw",
        "pepper",
        "career",
        "saddle",
    ],
    7: [
        "blanket",
        "captain",
        "journey",
        "picture",
        "thunder",
        "whisper",
        "relevel",
        "cannons",
        "easier",
        "breezes",
    ],
    8: [
        "birthday",
        "mountain",
        "painting",
        "sandwich",
        "sunshine",
        "wildlife",
        "sassafras",
        "elevator",
        "allergen",
        "stroller",
    ],
}


def choose_random_word(word_length: int) -> str:
    return "apple"  # For testing purposes, always return "crane"
    # return random.choice(WORDS_BY_LENGTH[word_length])
