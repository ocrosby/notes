# Motion Modifiers

Motions are already powerful on their own, but two modifiers can make any motion even more flexible: **counts** let you repeat a motion any number of times in one keystroke, and **motion type forcing** lets you override how Vim interprets what a motion selects. Neither is essential for beginners, but once you're comfortable with basic motions these will start to feel natural.

---

## Counts — Repeat Any Motion N Times

Prefix any motion with a number and Vim repeats it that many times:

```
{count}{motion}
```

| Example   | What it does |
|-----------|--------------|
| `2w`      | Move forward 2 words |
| `5j`      | Move down 5 lines |
| `3;`      | Jump to the 3rd next occurrence of the last searched character |
| `2/hello` | Jump to the 2nd occurrence of `hello` in the file |
| `10k`     | Move up 10 lines |

Counts work with operators too:

| Example | What it does |
|---------|--------------|
| `2dw`   | Delete 2 words |
| `3dd`   | Delete 3 lines |
| `4>>` | Indent 4 lines |

And when both the operator and the motion have a count, they multiply:

```
2d3w   →   deletes 6 words  (2 × 3)
```

**A practical tip about counting:** our brains are slow at counting lines in a file. For vertical jumps, enable relative line numbers — in Neovim, set `vim.wo.relativenumber = true`. With relative numbers, every line shows its distance from the cursor rather than its absolute number, so you can instantly read the count you need to type. `7k` to jump up 7 lines becomes obvious when you can see the `7` right there.

For large jumps, search (with `/`) is often faster than counting anyway — use counts for short, predictable distances.

---

## Motion Type Forcing — Override What Gets Selected

This one is more advanced, but understanding it prevents subtle bugs when writing complex commands.

Every motion in Vim has a default "type" — it either selects characters between two points (characterwise), whole lines (linewise), or a rectangular block (blockwise). This type determines exactly what an operator acts on. Sometimes the default type isn't what you want, and you can override it.

After typing an operator but *before* the motion, insert one of these:

| Key      | Forces the motion to be... |
|----------|----------------------------|
| `v`      | Characterwise (inclusive) |
| `V`      | Linewise |
| `Ctrl-v` | Blockwise |

Here's when this matters in practice:

```vim
" dj is linewise — deletes the current line AND the next entire line
dj

" dvj forces characterwise — deletes from cursor to the same column
" on the next line, rather than deleting whole lines
dvj
```

```vim
" d$ deletes to end of line (inclusive by default)
" On a single-character line, this may behave unexpectedly
" dv$ forces it to be characterwise exclusive — a subtle but real difference
dv$
```

A more practical example:

```vim
" gU} uppercases to the next blank line — but it's linewise,
" so it includes the blank line itself
gU}

" gUv} forces characterwise — stops before the blank line
gUv}
```

You probably won't need this often as a beginner, but when you find a motion doing something slightly unexpected — taking one character too many or one line too many — this is the tool to reach for.

---

← [Back to index](README.md)
