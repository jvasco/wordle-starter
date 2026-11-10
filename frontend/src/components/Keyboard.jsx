const rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

function Keyboard({ onKey, guesses, disabled }) {
  const letterStates = {}
  const priority = { absent: 1, present: 2, correct: 3 }

  guesses.forEach(({ word, feedback }) => {
    [...word].forEach((letter, index) => {
      const state = feedback[index]
      if (!letterStates[letter] || priority[state] > priority[letterStates[letter]]) {
        letterStates[letter] = state
      }
    })
  })

  return (
    <div className="keyboard" aria-label="On-screen keyboard">
      {rows.map((row, rowIndex) => (
        <div className="keyboard-row" key={row}>
          {rowIndex === 2 && (
            <button disabled={disabled} onClick={() => onKey('Enter')}>Enter</button>
          )}
          {[...row].map((letter) => (
            <button
              className={`key ${letterStates[letter] ? `key-${letterStates[letter]}` : ''}`}
              disabled={disabled}
              key={letter}
              onClick={() => onKey(letter)}
            >
              {letter}
            </button>
          ))}
          {rowIndex === 2 && (
            <button disabled={disabled} onClick={() => onKey('Backspace')}>⌫</button>
          )}
        </div>
      ))}
    </div>
  )
}

export default Keyboard
