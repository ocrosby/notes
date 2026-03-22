# Marks

Marks save cursor positions so you can jump back to them later. Think of them as bookmarks — some you set manually, others Vim sets automatically.

---

## Setting Marks

| Command  | Description |
|----------|-------------|
| `m{a-z}` | Set a lowercase mark (local to the current file) |
| `m{A-Z}` | Set an uppercase mark (global — works across files) |

> Lowercase marks are per-file. Uppercase marks are global: `mA` in one file lets you jump back to that exact spot from any other file.

---

## Jumping to Marks

| Motion        | Description |
|---------------|-------------|
| `` `{mark} `` | Jump to the exact line and column of the mark |
| `'{mark}`     | Jump to the first non-blank character of the mark's line |

> Use backtick (`` ` ``) for exact position; use apostrophe (`'`) when you just want the right line.

---

## Special Auto-Set Marks

Vim sets these automatically — you never need to set them manually.

| Motion   | Description |
|----------|-------------|
| ` `` `   | Jump to the exact position before the latest jump |
| `''`     | Jump to the line before the latest jump (first non-blank) |
| `` `. `` | Jump to the exact position of the last change |
| `'.`     | Jump to the line of the last change |
| `` `^ `` | Jump to where insert mode was last exited |
| `` `[ `` | Jump to the start of the last changed or yanked text |
| `` `] `` | Jump to the end of the last changed or yanked text |
| `` `< `` | Jump to the start of the last visual selection |
| `` `> `` | Jump to the end of the last visual selection |

> ` `` ` (double backtick) is the most useful of these — it's a two-way teleport between your last two positions.

---

## Traversing Marks

Walk forward or backward through all marks set in the current file:

| Motion   | Description |
|----------|-------------|
| `]'`     | Jump to the next line that has a lowercase mark |
| `` ]` `` | Jump to the next lowercase mark position after the cursor |
| `['`     | Jump to the previous line that has a lowercase mark |
| `` [` `` | Jump to the previous lowercase mark position before the cursor |

---

## Managing Marks

| Command            | Description |
|--------------------|-------------|
| `:marks`           | List all active marks |
| `:marks {abc}`     | List only marks `a`, `b`, `c` |
| `:delmarks {abc}`  | Delete marks `a`, `b`, `c` |
| `:delmarks!`       | Delete all lowercase marks in the current file |

---

← [Back to index](README.md)
