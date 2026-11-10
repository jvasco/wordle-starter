function GameBoard({ game, draft }) {
  if (!game) return null

  const rows = Array.from({ length: game.max_guesses }, (_, rowIndex) => {
    const submittedGuess = game.guesses[rowIndex]
    const letters = submittedGuess?.word ?? (rowIndex === game.guesses.length ? draft : '')

    return (
      <div className="board-row" key={rowIndex}>
        {Array.from({ length: game.word_length }, (_, columnIndex) => (
          <div
            className={`tile ${submittedGuess ? `tile-${submittedGuess.feedback[columnIndex]}` : ''}`}
            key={columnIndex}
          >
            {letters[columnIndex] ?? ''}
          </div>
        ))}
      </div>
    )
  })

  return <section className="board" aria-label="Guess board">{rows}</section>
}

export default GameBoard
