# Bracket and Code Structure Navigation

Real code is deeply nested. Functions inside classes inside modules, conditionals inside loops inside functions, preprocessor blocks wrapping platform-specific code. The motions on this page let you navigate that structure directly — jumping to the nearest enclosing scope, the next method, or the matching `#endif` — without searching or counting lines.

---

## The Core Pattern

Before diving in, there's one rule that applies to *everything* on this page:

> **Pattern — `[` vs `]`:** `[` always moves *backward* (toward the top of the file). `]` always moves *forward* (toward the bottom). This is completely consistent — every single motion here follows it. Learn this once and the whole page makes sense.

> **Pattern — lowercase vs UPPERCASE:** Within each pair, the lowercase variant jumps to the *start* of the target structure; uppercase jumps to the *end*. For example: `]m` = start of next method, `]M` = end of next method.

---

## Jumping to Unmatched Brackets

These motions find the nearest bracket that doesn't have a matching partner — in other words, the bracket that encloses the current scope.

| Motion | Description |
|--------|-------------|
| `[(`   | Jump to the previous unmatched `(` |
| `[{`   | Jump to the previous unmatched `{` |
| `])`   | Jump to the next unmatched `)` |
| `]}`   | Jump to the next unmatched `}` |

Imagine you're editing code deep inside several levels of nested braces and you want to find the opening `{` of the current block. Press `[{` and Vim jumps directly to it, no matter how many levels deep you are. This is faster than searching and more reliable than counting braces by eye.

Similarly, if you want to find where the current block ends, `]}` takes you to the closing `}` of the nearest enclosing scope.

---

## Method and Function Boundaries

These are particularly useful in object-oriented code where you're moving between methods in a class.

| Motion | Description |
|--------|-------------|
| `]m`   | Jump to the start of the next method/function |
| `]M`   | Jump to the end of the next method/function |
| `[m`   | Jump to the start of the previous method/function |
| `[M`   | Jump to the end of the previous method/function |

Use `]]` and `[[` (from [vertical motions](vertical.md)) if you're in a C-style language with top-level braces. Use `]m` and `[m` when you're in a class and the methods are indented — these look for method-start patterns rather than column-1 braces.

> **Python tip:** `]m` and `[m` work well inside Python class definitions. They jump between `def` method bodies by looking for method-start patterns, not column-1 braces — so they match Python's indented `def` statements correctly. Inside a class, `]m` takes you to the start of the next method and `[m` takes you to the previous one.

---

## Preprocessor Conditionals

If you work in C or C++, you'll often encounter blocks of code wrapped in `#if`/`#else`/`#endif` chains. These can be deeply nested and hard to navigate manually.

| Motion | Description |
|--------|-------------|
| `[#`   | Jump to the previous unmatched `#if` or `#else` |
| `]#`   | Jump to the next unmatched `#else` or `#endif` |

With your cursor inside a conditional block, `[#` takes you to the `#if` or `#else` that opened it. `]#` takes you forward to the next boundary.

> **Python tip:** Python has no preprocessor, so `[#` and `]#` don't apply. If you're using Neovim with Treesitter, plugins like `nvim-treesitter-textobjects` provide structure-aware navigation for Python — jumping between `if`/`elif`/`else` branches or `try`/`except`/`finally` blocks.

---

## C Comment Boundaries

When working with multi-line `/* ... */` comments in C-style languages, these motions jump to the edges of the comment block.

| Motion       | Description |
|--------------|-------------|
| `[*` or `[/` | Jump to the start of the current or previous `/* ... */` comment |
| `]*` or `]/` | Jump to the end of the current or next `/* ... */` comment |

> **Python tip:** Python doesn't use `/* ... */` comments, so these motions don't apply. For Python docstrings — triple-quoted strings like `"""..."""` or `'''...'''` — use quoted string text objects instead: `ci"` targets the contents of a docstring, and `da"` deletes the whole thing including the quotes. For a multi-line docstring that acts as a paragraph, `dip` (delete inner paragraph) is another clean option.

---

← [Back to index](README.md)
