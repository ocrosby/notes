# Marks

Marks are Vim's bookmarking system. They let you pin a position in a file and jump back to it instantly, no matter how far you've scrolled or what you've edited in between. Think of them as sticky notes that you leave in your code.

There are two kinds of marks: ones you set manually, and special ones Vim sets automatically every time you do something significant.

---

## Setting Your Own Marks

Press `m` followed by any letter to drop a mark at the current cursor position.

| Command  | Description |
|----------|-------------|
| `m{a-z}` | Set a lowercase mark (local to the current file) |
| `m{A-Z}` | Set an uppercase mark (global — works across files) |

For example, press `ma` to set mark `a` at the current position. You can set up to 26 lowercase marks per file (`a` through `z`).

> **Pattern — lowercase vs UPPERCASE:** Lowercase marks (`a`–`z`) are *local* to the file — they only exist within that buffer. Uppercase marks (`A`–`Z`) are *global* and persist across files and sessions. Think: small letter = small scope, big letter = big scope. Use an uppercase mark like `mF` when you want to jump back to a specific place from anywhere in your project.

---

## Jumping to a Mark

Once you've set a mark, there are two ways to jump to it:

| Motion        | Description |
|---------------|-------------|
| `` `{mark} `` | Jump to the exact line *and column* of the mark |
| `'{mark}`     | Jump to the first non-blank character of the mark's line |

The difference comes down to precision. Backtick (`` ` ``) restores you to the exact column — useful when the specific cursor position matters. Apostrophe (`'`) just gets you to the right line, landing on the first non-blank character.

> **Pattern — backtick vs apostrophe:** Backtick (`` ` ``) = *precise*, restores both line and column. Apostrophe (`'`) = *loose*, just gets you to the right line. In practice, use backtick when you're jumping back to resume editing at a specific spot; use apostrophe when you just need to be on the right line.

---

## Special Marks Vim Sets Automatically

You don't need to set these — Vim maintains them automatically as you work. They're some of the most useful marks because they track where you've *been*.

| Motion   | Description |
|----------|-------------|
| ` `` `   | Jump back to the exact position before the latest jump |
| `''`     | Jump to the line before the latest jump (first non-blank) |
| `` `. `` | Jump to the exact position of the last change |
| `'.`     | Jump to the line of the last change |
| `` `^ `` | Jump to where insert mode was last exited |
| `` `[ `` | Jump to the start of the last changed or yanked text |
| `` `] `` | Jump to the end of the last changed or yanked text |
| `` `< `` | Jump to the start of the last visual selection |
| `` `> `` | Jump to the end of the last visual selection |

The double-backtick (` `` `) is worth memorising early. It's a two-way teleport: jump somewhere (with `/`, `G`, a mark, anything), and ` `` ` brings you straight back to where you were. Jump again and it flips back the other way. It's the quickest way to switch your attention between two locations in a file.

`` `. `` is also extremely handy — it takes you back to the last place you made a change. Useful when you've been reading around the codebase and want to get back to where you were actually editing.

---

## Walking Through Your Marks

Rather than remembering which letter you used for which mark, you can browse through all your marks in order:

| Motion   | Description |
|----------|-------------|
| `]'`     | Jump to the next line that has a lowercase mark |
| `` ]` `` | Jump to the next lowercase mark position after the cursor |
| `['`     | Jump to the previous line that has a lowercase mark |
| `` [` `` | Jump to the previous lowercase mark position before the cursor |

---

## Managing Your Marks

| Command            | Description |
|--------------------|-------------|
| `:marks`           | List all marks and where they point |
| `:marks {abc}`     | List only marks `a`, `b`, `c` |
| `:delmarks {abc}`  | Delete specific marks |
| `:delmarks!`       | Delete all lowercase marks in the current file |

Run `:marks` any time you lose track of what marks you have set. The output shows each mark's letter, line number, column, and the text on that line — enough context to remember why you set it.

---

← [Back to index](README.md)
