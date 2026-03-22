# Jump Navigation

Every time you make a significant move in Vim — a search, a jump to a mark, pressing `G`, or following a definition — Vim records where you were before. These recorded positions form two lists you can navigate: the **jumplist** and the **changelist**. Think of them as a browser's back and forward buttons, but for your cursor.

---

## The Jumplist

The jumplist tracks *where you've navigated*. Any time you jump somewhere non-trivially — with `/`, `?`, `G`, `gg`, `%`, marks, `Ctrl-d`/`Ctrl-u`, window switches — Vim adds your previous position to the jumplist. Simple movements like `j`, `k`, `w`, and `b` do not add to it.

| Motion   | Description |
|----------|-------------|
| `Ctrl-o` | Jump to the previous (older) position in the jumplist |
| `Ctrl-i` | Jump to the next (newer) position in the jumplist |

`Ctrl-o` ("o" for older) takes you back to where you were before your last big jump. Press it again to go back further. `Ctrl-i` ("i" for... the key next to `o`) goes the other way — forward through the list if you've gone back too far.

A typical workflow: you're editing a function, you search for a helper to read its implementation, you make a note of what it does, and then you press `Ctrl-o` to return exactly where you were. No searching, no scrolling — just back.

> Run `:jumps` to print the full jumplist. Each window has its own jumplist of up to 100 entries.

---

## The Changelist

The changelist is similar, but it specifically tracks *where you've made edits* rather than where you've navigated. Every time you change the buffer, your position is saved.

| Motion | Description |
|--------|-------------|
| `g;`   | Go to the previous (older) position where you made a change |
| `g,`   | Go to the next (newer) position in the changelist |

This is useful when you've been reading around the codebase and want to get back to where you were actually typing. `g;` gets you there immediately, regardless of how many jumps and searches you've made in the meantime.

> Run `:changes` to print the full changelist.

---

## Jumplist vs Changelist — When to Use Each

| Situation | Use |
|-----------|-----|
| You searched or jumped somewhere and want to go back | `Ctrl-o` |
| You pressed `Ctrl-o` too many times and want to go forward | `Ctrl-i` |
| You've been browsing and want to return to where you were editing | `g;` |
| You used `g;` too many times and want to move forward through changes | `g,` |

---

← [Back to index](README.md)
