function NewGameForm({ onStart, disabled }) {
  return (
    <form
      className="new-game-form"
      onSubmit={(event) => {
        event.preventDefault()
        onStart(Number(new FormData(event.currentTarget).get('word-length')))
      }}
    >
      <label htmlFor="word-length">Word length</label>
      <select defaultValue="5" id="word-length" name="word-length">
        {[5, 6, 7, 8].map((length) => (
          <option key={length} value={length}>{length} letters</option>
        ))}
      </select>
      <button disabled={disabled} type="submit">New game</button>
    </form>
  )
}

export default NewGameForm
