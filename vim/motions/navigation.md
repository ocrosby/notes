# File, Window, and Semantic Navigation

Once a file gets beyond a few dozen lines, you need ways to move across it instantly — not line by line, but in big leaps. This page covers three kinds of large-scale navigation: jumping to specific positions in a file, repositioning within the window you can see, and following code references like definitions and imports.

---

## File-Level Jumps

These motions ignore line-by-line movement entirely and jump to specific positions in the file.

| Motion     | Description |
|------------|-------------|
| `gg`       | Go to the top of the file |
| `G`        | Go to the end of the file |
| `{line}G`  | Go to a specific line number (e.g., `42G`) |
| `{count}%` | Jump to [count] percentage through the file (e.g., `50%` = midpoint) |
| `%`        | Jump to the matching bracket: `(`, `)`, `[`, `]`, `{`, `}` |
| `:go {n}`  | Jump to byte offset `{n}` in the buffer |

`gg` and `G` are the ones you'll use most. Press `gg` to get to the top of a file — useful when you open a file and want to start reading from the beginning. Press `G` to jump to the end, which is handy when you're appending to a log or checking recent additions.

When someone says "look at line 237", press `237G` and you're there immediately.

`%` is underrated for new users. Place your cursor on any opening or closing bracket, brace, or parenthesis and press `%` — Vim jumps to the matching pair. This is extremely useful for checking that your brackets are balanced or for selecting the contents of a block.

> **Pattern — `gg` vs `G`:** `gg` (lowercase) goes to the *first* line — think of it as "go, go, all the way back to the start." `G` (uppercase, one decisive keystroke) goes to the *last* line. With a count, both jump to that line: `42G` goes to line 42.

> `%` also works on `/* */` C comments and `#if`/`#endif` preprocessor pairs, not just brackets.

---

## Window Position

Sometimes you don't want to jump to a different part of the file — you just want to put your cursor somewhere in the text that's already on screen. These three motions do that without scrolling anything.

| Motion | Description |
|--------|-------------|
| `H`    | Jump to the first line of the window (top) |
| `M`    | Jump to the middle line of the window |
| `L`    | Jump to the last line of the window (bottom) |

A common workflow: use `Ctrl-d`/`Ctrl-u` to scroll to roughly the right area, then use `H`, `M`, or `L` to position your cursor precisely within what you can see — without further scrolling.

> **Pattern — H / M / L:** These are simply the first letters of **H**igh, **M**iddle, and **L**ow. No other mnemonic needed — they describe exactly where in the window they put you.

> Combine with a count: `3H` jumps to the 3rd line from the top; `2L` jumps to the 2nd line from the bottom.

---

## Semantic Navigation

These motions aren't just about positions — they understand the *meaning* of what's under the cursor.

| Motion | Description |
|--------|-------------|
| `gd`   | Jump to the definition of the symbol under the cursor |
| `gf`   | Jump to the file whose path is under the cursor |

`gd` is the "go to definition" command. Place your cursor on a function name, variable, or class and press `gd` — Vim jumps to where it was defined. In a plain text environment this searches for the first occurrence of the word in the file. In a language-aware environment (like Neovim with LSP configured), it performs a proper semantic jump to the actual definition, even across files.

`gf` is surprisingly useful. If your cursor is on a file path — say, an import statement like `require('./utils/helpers')` or a Python `from models import user` — pressing `gf` opens that file directly. You never have to manually navigate to it.

---

← [Back to index](README.md)
