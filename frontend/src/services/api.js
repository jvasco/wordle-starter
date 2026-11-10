const API_URL = 'http://localhost:8000'

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })

  const data = await response.json()
  if (!response.ok) {
    throw new Error(data.detail ?? 'The request failed')
  }
  return data
}

export function createGame(wordLength) {
  return request('/games', {
    method: 'POST',
    body: JSON.stringify({ word_length: wordLength }),
  })
}

export function submitGuess(gameId, word) {
  return request(`/games/${gameId}/guesses`, {
    method: 'POST',
    body: JSON.stringify({ word }),
  })
}
