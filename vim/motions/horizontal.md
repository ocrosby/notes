# Horizontal Motions

Your first instinct when editing in Vim will be to use the arrow keys — and that works. But arrow keys keep your hands away from the home row, and in Vim, leaving the home row has a cost. This page walks you through progressively better ways to move along a single line, from basic character steps all the way to surgical single-character jumps anywhere on the line.

---

## Basic Movement

The four foundational horizontal keys are `h` and `l` for left and right, and `0`/`$` to jump to the edges of the line. These keep your right hand on the home row.

| Motion | Description |
|--------|-------------|
| `h`    | Move left one character |
| `l`    | Move right one character |
| `0`    | Move to the first character of the line |
| `^`    | Move to the first non-blank character of the line |
| `$`    | Move to the end of the line |
| `g_`   | Move to the last non-blank character of the line |

The difference between `0` and `^` matters when lines are indented. `0` always goes to column 1 — the very start of the line including any leading whitespace. `^` skips past that whitespace and puts you at the first actual character. In code, `^` is almost always what you want.

Similarly, `$` goes to the end of the line including any trailing whitespace, while `g_` stops at the last non-blank character.

> **Tip:** You'll use `^` and `$` constantly — they're essential for operators. `d^` deletes from the cursor back to the first non-blank; `d$` (or just `D`) deletes to the end of the line.

---

## Screen Line Motions (When Lines Wrap)

When `wrap` is enabled, a single long logical line can span several visible lines on screen. The basic motions (`0`, `^`, `$`) treat the whole thing as one line — pressing `$` jumps to the far end of the wrapped line, which may be off-screen. The `g`-prefixed variants stay within the visible portion.

| Motion | Description |
|--------|-------------|
| `g0`   | Move to the first character of the screen line |
| `g^`   | Move to the first non-blank character of the screen line |
| `gm`   | Move to the middle of the screen width |
| `g$`   | Move to the last character of the screen line |
| `\|`   | Move to column [count] on the current line |

> **Pattern — `g` prefix:** The `g` variants are the display-aware versions of their base motions. Same letter, but `g` means "act on what I can *see* on this screen line, not the whole logical line."

---

## Word by Word

Once you're comfortable with `h` and `l`, the next step is jumping whole words at a time. This is where movement starts to feel fast.

Vim has two kinds of words:
- A **word** (`w`) is a sequence of letters, digits, or underscores — basically an identifier. Punctuation like `.`, `(`, and `{` are their own separate words.
- A **WORD** (`W`) is anything separated by whitespace. `foo.bar(baz)` is one WORD but five words.

```
wwww ==> v   v v   v   v
         word. are two words
         word. is one WORD
WWW  ==> ^     ^  ^   ^
```

| Motion | Description |
|--------|-------------|
| `w`    | Jump to the beginning of the next word |
| `b`    | Jump to the beginning of the previous word |
| `e`    | Jump to the end of the current/next word |
| `ge`   | Jump to the end of the previous word |
| `W`    | Jump to the beginning of the next WORD |
| `B`    | Jump to the beginning of the previous WORD |
| `E`    | Jump to the end of the current/next WORD |
| `gE`   | Jump to the end of the previous WORD |

> **Pattern — lowercase vs UPPERCASE:** Lowercase motions (`w`, `b`, `e`, `ge`) operate on *words* — respecting punctuation as boundaries. Uppercase (`W`, `B`, `E`, `gE`) operate on *WORDs* — only whitespace is a boundary. Use lowercase for precision when editing code; use uppercase for speed when you want to hop over entire expressions like `foo.bar()` in one jump.

> **Pattern — forward vs backward:** `w` and `e` move *forward*; `b` and `ge` move *backward*. The uppercase versions follow the same rule. When you need to go back, reach for `b` (beginning of previous word) or `ge` (end of previous word).

---

## Finding a Character

Word motions are great for structured code, but sometimes you just want to jump directly to a specific character on the line. The `f` and `t` motions do exactly that — and once you learn `;` to repeat them, they become one of the most efficient tools in Vim.

| Motion    | Description |
|-----------|-------------|
| `f{char}` | Move to the next occurrence of `{char}` on the line |
| `F{char}` | Move to the previous occurrence of `{char}` on the line |
| `t{char}` | Move just *before* the next occurrence of `{char}` |
| `T{char}` | Move just *after* the previous occurrence of `{char}` |
| `;`       | Repeat the last `f`/`F`/`t`/`T` forward |
| `,`       | Repeat the last `f`/`F`/`t`/`T` backward |

Here's the difference between `f` and `t` on the same line:

```
f(   ==> v                        v
         const fireball = function(target){
t(   ==> v                       v
         const fireball = function(target){
```

`f(` lands *on* the `(`. `t(` lands on the character *before* it. This distinction matters when combining with operators:

- `df(` — delete everything from the cursor up to and *including* the `(`
- `dt(` — delete everything up to but *not including* the `(` — leaving the `(` intact

For operators, `t` is usually what you want because it leaves the delimiter in place.

> **Pattern — lowercase vs UPPERCASE:** `f` and `t` search *forward*; `F` and `T` search *backward*. Capitalising the letter reverses the direction — a rule that applies to many motions in Vim.

> **Pattern — `f` vs `t`:** `f` = lands *on* the character (think: **f**ind it). `t` = lands just *before* it (think: up *t*ill the character, but not including it).

Don't retype the search to get to the next match. Use `;` to jump forward to the next occurrence and `,` to jump back:

```
fd;;   ==> v   v               v        v
           let damage = weapon.damage * d20();
```

Type `fd` once, then press `;` to walk through every `d` on the line. This is much faster than retyping `fd` each time.

> **Python tip:** A few characters come up constantly as `f`/`t` targets in Python code:
> - `f:` — jump to the `:` at the end of a `def`, `if`, `for`, `while`, or `class` statement
> - `f=` — jump to an assignment or keyword argument
> - `f,` — hop to the next argument separator in a function call
> - `t,` combined with `d` or `c` — delete or replace an argument without touching its trailing comma
>
> For example, on a line like `result = calculate(base, rate, discount)`, pressing `f,` moves you to each comma in turn, and `dt,` deletes the current argument up to (but not including) the comma.

---

← [Back to index](README.md)
