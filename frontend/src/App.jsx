import { useCallback, useEffect, useState } from 'react'
import './App.css'
import GameBoard from './components/GameBoard.jsx'
import Keyboard from './components/Keyboard.jsx'
import NewGameForm from './components/NewGameForm.jsx'
import { createGame, submitGuess } from './services/api.js'

function App() {
  const [game, setGame] = useState(null)
  const [draft, setDraft] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)

  const startGame = async (wordLength) => {
    setLoading(true)
    setError('')
    setDraft('')
    try {
      setGame(await createGame(wordLength))
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setLoading(false)
    }
  }

  const handleKey = useCallback(async (key) => {
    if (!game || game.status !== 'active' || loading) return
    setError('')

    if (key === 'Backspace') {
      setDraft((current) => current.slice(0, -1))
    } else if (key === 'Enter') {
      if (draft.length !== game.word_length) {
        setError(`Enter ${game.word_length} letters to submit a guess.`)
        return
      }
      setLoading(true)
      try {
        setGame(await submitGuess(game.game_id, draft))
        setDraft('')
      } catch (requestError) {
        setError(requestError.message)
      } finally {
        setLoading(false)
      }
    } else if (/^[a-z]$/i.test(key) && draft.length < game.word_length) {
      setDraft((current) => current + key.toLowerCase())
    }
  }, [draft, game, loading])

  useEffect(() => {
    const onKeyDown = (event) => {
      if (/^[a-z]$/i.test(event.key) || event.key === 'Enter' || event.key === 'Backspace') {
        event.preventDefault()
        handleKey(event.key)
      }
    }
    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [handleKey])

  return (
    <main className="app">
      <header className="app-header">
        <p className="eyebrow">A little word game</p>
        <h1>Wordle</h1>
        <p>Guess the hidden word. Green is right, yellow is misplaced.</p>
      </header>
      <NewGameForm onStart={startGame} disabled={loading} />
      {error && <p className="message error" role="alert">{error}</p>}
      {game && (
        <>
          <GameBoard game={game} draft={draft} />
          <Keyboard onKey={handleKey} guesses={game.guesses} disabled={loading || game.status !== 'active'} />
          <p aria-live="polite" className="message">
            {loading ? 'Working…' : game.status === 'won' ? 'You got it!' : game.status === 'lost' ? `The word was ${game.answer}.` : `${game.guesses_remaining} guesses left`}
          </p>
        </>
      )}
    </main>
  )
}

export default App
