# Text Object Selection

If there's one concept that separates casual Vim users from people who genuinely love editing in Vim, it's text objects. They're the key insight that makes editing feel almost telepathic.

Here's the idea. In most editors, to change the contents of a string you'd: click at the opening quote, hold shift, click at the closing quote, then type. In Vim, you press `ci"` — *change inside quotes* — and you're done. Vim knows what a quoted string is. It finds the nearest one, selects its contents, and drops you into insert mode ready to type.

Text objects describe *what* you want to operate on, not *where* to navigate. They're always used after an operator (`d` for delete, `c` for change, `y` for yank, `v` for visual select, `>` for indent, etc.).

---

## The Two Prefixes: `a` and `i`

Every text object comes in two flavours:

- `a` — **a**round: selects the object *including* its delimiters or surrounding whitespace
- `i` — **i**nside: selects only the *contents*, leaving the delimiters untouched

> **Pattern — `a` vs `i`:** Think of it as `a` = the whole package (container included), `i` = just the contents. Use `i` to replace a value while keeping its wrapper; use `a` to delete the whole thing.

For example, with your cursor anywhere inside `"hello world"`:
- `di"` — deletes `hello world`, leaving the empty quotes `""` behind
- `da"` — deletes `"hello world"`, quotes and all
- `ci"` — deletes `hello world` and puts you in insert mode inside the quotes
- `yi"` — yanks (copies) `hello world` without the quotes

---

## Words and WORDs

| Object | Description |
|--------|-------------|
| `aw`   | A word, including surrounding whitespace |
| `iw`   | Inner word, no whitespace |
| `aW`   | A WORD, including surrounding whitespace |
| `iW`   | Inner WORD, no whitespace |

`ciw` is one of the most useful commands in Vim — it changes the word under the cursor regardless of where within the word the cursor sits. You don't need to be at the start of the word. Just press `ciw` and start typing the replacement.

---

## Sentences and Paragraphs

| Object | Description |
|--------|-------------|
| `as`   | A sentence, including trailing whitespace |
| `is`   | Inner sentence |
| `ap`   | A paragraph, including trailing blank line |
| `ip`   | Inner paragraph |

These are most useful when editing documentation, comments, or prose. `dap` deletes the entire current paragraph — including the blank line after it — making it easy to remove a block of comments cleanly.

---

## Brackets and Blocks

This is where text objects shine most in code. You can operate on the contents of any surrounding bracket pair, no matter how deep you are inside nested structures.

> **Pattern — `b` vs `B`:** `b` (lowercase) targets **b**rackets — meaning parentheses `(...)`. `B` (uppercase) targets **B**ig brackets — meaning curly braces `{...}`. You can also type the actual bracket character if you prefer: `i(` is the same as `ib`, and `i{` is the same as `iB`.

| Object              | Description |
|---------------------|-------------|
| `ab` / `a(` / `a)`  | A parenthesis block `(...)` |
| `ib` / `i(` / `i)`  | Inner parenthesis block |
| `aB` / `a{` / `a}`  | A curly brace block `{...}` |
| `iB` / `i{` / `i}`  | Inner curly brace block |
| `a[` / `a]`         | A bracket block `[...]` |
| `i[` / `i]`         | Inner bracket block |
| `a<` / `a>`         | An angle bracket block `<...>` |
| `i<` / `i>`         | Inner angle bracket block |

Imagine your cursor is somewhere inside a function call like `calculate(price * quantity, taxRate)`. Press `ci(` and Vim deletes everything between the parentheses and drops you into insert mode — ready to rewrite the arguments. The parentheses themselves are left untouched.

> **Python tip:** In Python, `{}` is used for dict and set literals — not for code blocks. `iB`/`aB` will target dict/set contents, not the body of a function or `if` statement. The most common bracket text objects in Python code are:
> - `i(` / `a(` — function call arguments, tuples, generator expressions
> - `i[` / `a[` — list contents, subscript expressions, list comprehensions
> - `i{` / `a{` — dict and set contents
>
> `ci(` to rewrite a function's arguments and `di[` to clear a list literal come up constantly in Python. For navigating *code blocks*, Python uses indentation — Treesitter-based text objects (`:h nvim-treesitter-textobjects`) provide `if`/`class`/`function` scope selection in Neovim.

---

## Tags

| Object | Description |
|--------|-------------|
| `at`   | A tag block `<tag>...</tag>`, including the opening and closing tags |
| `it`   | Inner tag block — just the content between the tags |

These work on HTML and XML. Place your cursor anywhere inside a `<div>...</div>` and press `cit` to replace its contents, or `dat` to delete the entire element including the tags.

---

## Quoted Strings

| Object   | Description |
|----------|-------------|
| `a"`     | A double-quoted string, including the quotes |
| `i"`     | Inner double-quoted string |
| `a'`     | A single-quoted string, including the quotes |
| `i'`     | Inner single-quoted string |
| `` a` `` | A backtick-quoted string, including the backticks |
| `` i` `` | Inner backtick-quoted string |

These are among the most frequently used text objects in day-to-day coding. Whether you're editing a string value, a template literal, or a configuration string, `ci"` or `ci'` will become second nature.

---

## Putting It Together

Once you internalise the `a`/`i` + object pattern, a large part of your editing becomes: think about *what* you're editing, not *how* to navigate to it.

| Command | What it does |
|---------|-------------|
| `ciw`   | Change the word under the cursor |
| `dap`   | Delete the current paragraph |
| `yi)`   | Yank (copy) everything inside the nearest `()` |
| `va"`   | Visually select a double-quoted string including quotes |
| `=iB`   | Re-indent the contents of the current `{}` block |
| `>aB`   | Indent the entire `{}` block including the braces |
| `ci(`   | Change the arguments inside the nearest function call |
| `dat`   | Delete an entire HTML/XML element including tags |

---

← [Back to index](README.md)
