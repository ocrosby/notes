# Vertical Motions

Moving along a line gets you far, but most of the time you're navigating *between* lines — scrolling through a function, jumping to a block, or leaping straight to a pattern anywhere in the file. This page covers all of that, starting from basic up-down movement and working up to search-powered navigation that can put your cursor anywhere in a file in seconds.

---

## Basic Line Movement

The core vertical keys are `j` (down) and `k` (up). Like `h` and `l` for horizontal movement, they keep your hand on the home row instead of reaching for the arrow keys.

| Motion   | Description |
|----------|-------------|
| `j`      | Move down one line |
| `k`      | Move up one line |
| `gj`     | Move down one display line (for wrapped lines) |
| `gk`     | Move up one display line (for wrapped lines) |
| `-`      | Move up to the first non-blank character of the previous line |
| `+`      | Move down to the first non-blank character of the next line |
| `_`      | Move to the first non-blank of the current line ([count-1] lines down) |

> **Pattern — `g` prefix:** When `wrap` is enabled, a long logical line spans multiple visible lines. `j` and `k` jump the entire logical line, which may skip several visible rows at once. `gj` and `gk` move one *visible* line at a time. Use `gj`/`gk` when editing prose or long lines with wrap on.

---

## Jumping by Sentence and Paragraph

When you're reading through a large function or a block of documentation, jumping one line at a time with `j`/`k` is tedious. Sentence and paragraph motions let you skip in larger chunks.

| Motion   | Description |
|----------|-------------|
| `)`      | Jump forward to the beginning of the next sentence |
| `(`      | Jump backward to the beginning of a sentence |
| `}`      | Jump down to the next blank-line-separated block |
| `{`      | Jump up to the previous blank-line-separated block |
| `Ctrl-d` | Scroll down half a page |
| `Ctrl-u` | Scroll up half a page |

In practice, `{` and `}` are the ones you'll use constantly. In code, blank lines naturally separate functions, classes, and logical sections — `}` and `{` let you hop between them instantly.

> **Pattern — closing = forward, opening = backward:** `)` and `}` are *closing* brackets — they move *forward* (down the file). `(` and `{` are *opening* brackets — they move *backward* (up the file). Let the bracket shape guide you: `)` points right (forward), `(` points left (backward).

> A sentence ends at `.`, `!`, or `?` followed by a newline or two spaces. This makes sentence motions most useful in prose and documentation rather than code.

---

## Searching

This is where vertical navigation becomes truly powerful. Instead of navigating *to* where you want to be, you describe *what* you're looking for and Vim takes you there. Once you're used to searching for navigation, you'll reach for it constantly.

| Motion       | Description |
|--------------|-------------|
| `/{pattern}` | Search forward for `{pattern}` |
| `?{pattern}` | Search backward for `{pattern}` |
| `n`          | Jump to the next match |
| `N`          | Jump to the previous match |
| `*`          | Search forward for the word under the cursor |
| `#`          | Search backward for the word under the cursor |
| `/<Enter>`   | Re-run the last search forward |
| `?<Enter>`   | Re-run the last search backward |

The workflow looks like this: press `/`, type a few characters of what you're looking for, press `Enter`, and you're there. Then use `n` and `N` to walk between matches without retyping anything.

For example, if you want to jump to a function called `processPayment`, just type `/processPayment<Enter>`. If there are multiple matches, `n` takes you to the next one, `N` goes back.

A faster shortcut: position your cursor on any word and press `*`. Vim immediately searches forward for that exact word. This is perfect for jumping between all usages of a variable or function name.

> **Pattern — `/` vs `?`:** `/` searches *forward* (toward the bottom of the file); `?` searches *backward* (toward the top). Think of the slash leaning forward and the question mark leaning back.

> **Pattern — `n` vs `N`:** `n` repeats the search in the *same* direction you originally searched. `N` goes the *opposite* way. So if you searched with `/`, `n` goes forward and `N` goes backward. If you searched with `?`, it flips.

> **Pattern — `*` vs `#`:** `*` searches *forward* for the word under the cursor; `#` searches *backward*. Both automatically wrap around the file.

> `{pattern}` supports full regular expressions, not just plain strings.

---

## Section Motions

In languages that use `{` and `}` to define blocks — C, Go, JavaScript, Java — top-level definitions like functions and classes typically have their opening brace at column 1. Vim uses this convention to provide section-level jumps.

| Motion | Description |
|--------|-------------|
| `[[`   | Jump to the previous `{` in column 1 (function/class start) |
| `]]`   | Jump to the next `{` in column 1 (function/class start) |
| `[]`   | Jump to the previous `}` in column 1 (function/class end) |
| `][`   | Jump to the next `}` in column 1 (function/class end) |

These are most reliable in C-style languages. In Python or Ruby, `{`/`}` paragraph jumps tend to work better for navigating between definitions.

> **Python tip:** Python doesn't place `{` at column 1 — it uses indentation for blocks and blank lines to separate definitions. As a result, `[[`/`]]` won't reliably jump between Python functions or classes. Use `{` and `}` (paragraph jumps) instead. They work naturally with Python's blank-line-separated `def` and `class` blocks: `}` hops to the next definition, `{` goes back to the previous one.

---

← [Back to index](README.md)
