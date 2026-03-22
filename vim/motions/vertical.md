# Vertical Motions

Vertical motions move between lines — from single-line steps to paragraph jumps to regex-powered teleportation.

---

## Basic

| Motion   | Description |
|----------|-------------|
| `j`      | Move down one line |
| `k`      | Move up one line |
| `gj`     | Move down one display line (useful when `wrap` is on) |
| `gk`     | Move up one display line (useful when `wrap` is on) |
| `-`      | Move up to the first non-blank character of the previous line |
| `+`      | Move down to the first non-blank character of the next line |
| `_`      | Move to the first non-blank of the current line ([count-1] lines down) |
| `)`      | Jump forward to the beginning of the next sentence |
| `(`      | Jump backward to the beginning of a sentence |
| `}`      | Jump down to the next blank-line-separated block |
| `{`      | Jump up to the previous blank-line-separated block |
| `Ctrl-d` | Scroll down half a page |
| `Ctrl-u` | Scroll up half a page |

> A sentence ends at `.`, `!`, or `?` followed by a newline or two spaces.
> `{` and `}` are the fastest way to skip between code blocks or paragraphs.

---

## Search Pattern

Search-based navigation is the highest-precision vertical motion — jump anywhere in the file by pattern.

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

> `{pattern}` can be a string literal or a regular expression.
> Use `*` on a function name to instantly jump between all its usages.

---

## Section Motions

Jump between top-level definitions. These look for `{` or `}` at the first column — which is how C-style function bodies and many other languages delimit top-level blocks.

| Motion | Description |
|--------|-------------|
| `[[`   | Jump to the previous `{` in column 1 (function start) |
| `]]`   | Jump to the next `{` in column 1 (function start) |
| `[]`   | Jump to the previous `}` in column 1 (function end) |
| `][`   | Jump to the next `}` in column 1 (function end) |

---

← [Back to index](README.md)
