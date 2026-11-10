from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import HTTPException
from pydantic import BaseModel, Field

from models.game import Game
from services.game_service import create_game as create_new_game
from services.game_service import evaluate_guess
from data.words import WORDS_BY_LENGTH

app = FastAPI()
games: dict[str, Game] = {}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

class CreateGameRequest(BaseModel):
    word_length: int = Field(ge=5, le=8)


class SubmitGuessRequest(BaseModel):
    word: str = Field(min_length=1)


@app.post("/games")
def create_game(request: CreateGameRequest):
    game = create_new_game(request.word_length)
    games[game.id] = game
    return game.public_state()


@app.get("/games/{game_id}")
def get_game(game_id: str):
    game = games.get(game_id)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    return game.public_state()


@app.post("/games/{game_id}/guesses")
def submit_guess(game_id: str, request: SubmitGuessRequest):
    game = games.get(game_id)
    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    if game.status != "active":
        raise HTTPException(status_code=409, detail="This game is already finished")

    guess = request.word.strip().lower()
    if len(guess) != game.word_length or not guess.isalpha():
        raise HTTPException(
            status_code=422,
            detail=f"Guess must contain {game.word_length} letters",
        )
    if guess not in WORDS_BY_LENGTH[game.word_length]:
        raise HTTPException(
            status_code=422,
            detail=f"Word not found in dictionary",
        )

    feedback = evaluate_guess(guess, game.target_word)
    game.guesses.append({"word": guess, "feedback": feedback})
    if guess == game.target_word:
        game.status = "won"
    elif len(game.guesses) == game.max_guesses:
        game.status = "lost"

    return game.public_state()
