# File, Window, and Semantic Navigation

Large-scale navigation: jump across an entire file, reposition within the visible window, or follow code references.

---

## File-Level

| Motion      | Description |
|-------------|-------------|
| `gg`        | Go to the top of the file |
| `G`         | Go to the end of the file |
| `{line}G`   | Go to a specific line number (e.g., `42G`) |
| `{count}%`  | Jump to [count] percentage through the file (e.g., `50%` = midpoint) |
| `%`         | Jump to the matching bracket: `(`, `)`, `[`, `]`, `{`, `}` |
| `:go {n}`   | Jump to byte offset `{n}` in the buffer |

> `%` also works on `/* */` C comments and `#if`/`#endif` preprocessor pairs.

---

## Window Position

Jump to a specific position within the visible window without changing what's on screen.

| Motion | Description |
|--------|-------------|
| `H`    | Jump to the first line of the window (top) |
| `M`    | Jump to the middle line of the window |
| `L`    | Jump to the last line of the window (bottom) |

> Combine with a count: `3H` jumps to the 3rd line from the top; `2L` jumps to the 2nd line from the bottom.

---

## Semantic

These motions understand code structure rather than just text.

| Motion | Description |
|--------|-------------|
| `gd`   | Jump to the definition of the symbol under the cursor |
| `gf`   | Jump to the file whose path is under the cursor |

> `gf` is useful for quickly opening imported files — place the cursor on a path string and press `gf`.

---

← [Back to index](README.md)
