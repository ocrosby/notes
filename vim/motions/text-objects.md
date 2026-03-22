# Text Object Selection

Text objects are used after an operator (`d`, `c`, `y`, `v`, `>`, `=`, etc.) to select a structured region of text. Instead of navigating manually to the start and end of something, you describe *what* to operate on.

The two prefixes:
- `a` — **a**round: includes the delimiters/whitespace surrounding the object
- `i` — **i**nner: the contents only, without delimiters

> Example: `di"` deletes inside a quoted string; `da"` deletes the string including its quotes; `ci(` changes everything inside parentheses.

---

## Word and WORD

| Object | Description |
|--------|-------------|
| `aw`   | A word, including surrounding whitespace |
| `iw`   | Inner word, no whitespace |
| `aW`   | A WORD, including surrounding whitespace |
| `iW`   | Inner WORD, no whitespace |

---

## Sentence and Paragraph

| Object | Description |
|--------|-------------|
| `as`   | A sentence, including trailing whitespace |
| `is`   | Inner sentence |
| `ap`   | A paragraph, including trailing blank line |
| `ip`   | Inner paragraph |

---

## Bracket and Block

| Object             | Description |
|--------------------|-------------|
| `ab` / `a(` / `a)` | A parenthesis block `(...)` |
| `ib` / `i(` / `i)` | Inner parenthesis block |
| `aB` / `a{` / `a}` | A curly brace block `{...}` |
| `iB` / `i{` / `i}` | Inner curly brace block |
| `a[` / `a]`        | A bracket block `[...]` |
| `i[` / `i]`        | Inner bracket block |
| `a<` / `a>`        | An angle bracket block `<...>` |
| `i<` / `i>`        | Inner angle bracket block |

---

## Tag Block

| Object | Description |
|--------|-------------|
| `at`   | A tag block `<tag>...</tag>`, including the tags |
| `it`   | Inner tag block, content only |

> Useful for HTML/XML editing. Works on the nearest enclosing tag pair.

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

---

## Common Combinations

| Command | Effect |
|---------|--------|
| `ciw`   | Change the word under the cursor |
| `dap`   | Delete the current paragraph |
| `yi)`   | Yank everything inside the nearest `()` |
| `va"`   | Visually select a double-quoted string including quotes |
| `=iB`   | Re-indent the contents of the current `{}` block |
| `>aB`   | Indent the entire `{}` block including braces |

---

← [Back to index](README.md)
