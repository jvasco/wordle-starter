from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class Game:
    target_word: str
    id: str = field(default_factory=lambda: str(uuid4()))
    guesses: list[dict] = field(default_factory=list)
    status: str = "active"

    @property
    def word_length(self) -> int:
        return len(self.target_word)

    @property
    def max_guesses(self) -> int:
        return self.word_length + 1

    def public_state(self) -> dict:
        state = {
            "game_id": self.id,
            "word_length": self.word_length,
            "max_guesses": self.max_guesses,
            "guesses": self.guesses,
            "guesses_remaining": self.max_guesses - len(self.guesses),
            "status": self.status,
        }
        if self.status != "active":
            state["answer"] = self.target_word
        return state