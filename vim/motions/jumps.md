# Jump Navigation

Vim automatically records a history of "large" cursor movements in two separate lists: the **jumplist** and the **changelist**. You can traverse both to retrace your steps without remembering where you were.

---

## Jumplist

The jumplist records your position every time you make a significant jump: searches, `G`, mark jumps, `%`, window switches, etc. Word-by-word and character motions do *not* add to the jumplist.

| Motion   | Description |
|----------|-------------|
| `Ctrl-o` | Jump to the previous (older) position in the jumplist |
| `Ctrl-i` | Jump to the next (newer) position in the jumplist |

> `:jumps` prints the full list. Each window has its own jumplist (up to 100 entries).

---

## Changelist

The changelist records every position where a change was made. It persists across sessions via `viminfo`.

| Motion | Description |
|--------|-------------|
| `g;`   | Go to the previous (older) change position |
| `g,`   | Go to the next (newer) change position |

> `:changes` prints the full changelist.

---

## When to Use Each

| Situation | Use |
|-----------|-----|
| You jumped somewhere and want to go back | `Ctrl-o` |
| You went back too far and want to go forward again | `Ctrl-i` |
| You made an edit somewhere and want to return to it | `g;` |
| You used `g;` too many times and want to go forward | `g,` |

---

← [Back to index](README.md)
