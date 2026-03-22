# Bracket and Code Structure Navigation

These motions navigate code structure: unmatched delimiters, method boundaries, preprocessor conditionals, and C comment edges.

---

## Unmatched Brackets

Jump outward to the nearest enclosing unmatched bracket — useful for finding the scope you're currently inside.

| Motion | Description |
|--------|-------------|
| `[(`   | Jump to the previous unmatched `(` |
| `[{`   | Jump to the previous unmatched `{` |
| `])`   | Jump to the next unmatched `)` |
| `]}`   | Jump to the next unmatched `}` |

> Use `[{` to jump to the opening brace of the current block, no matter how deeply nested you are.

---

## Method / Function Boundaries

| Motion | Description |
|--------|-------------|
| `]m`   | Jump to the start of the next method/function |
| `]M`   | Jump to the end of the next method/function |
| `[m`   | Jump to the start of the previous method/function |
| `[M`   | Jump to the end of the previous method/function |

---

## Preprocessor Conditionals

Navigate `#if`/`#else`/`#endif` chains — useful in C and C++ codebases.

| Motion | Description |
|--------|-------------|
| `[#`   | Jump to the previous unmatched `#if` or `#else` |
| `]#`   | Jump to the next unmatched `#else` or `#endif` |

---

## C Comment Boundaries

| Motion        | Description |
|---------------|-------------|
| `[*` or `[/`  | Jump to the start of the current or previous `/* ... */` comment |
| `]*` or `]/`  | Jump to the end of the current or next `/* ... */` comment |

---

← [Back to index](README.md)
