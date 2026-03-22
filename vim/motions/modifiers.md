# Motion Modifiers

These aren't motions themselves — they change how a motion behaves when combined with an operator or count.

---

## Counts (Multipliers)

Prefix any motion with a number to repeat it that many times:

```
{count}{motion}
```

| Example   | Description |
|-----------|-------------|
| `2w`      | Move 2 words forward |
| `5j`      | Move 5 lines down |
| `3;`      | Go to the 3rd next occurrence of the last searched character |
| `2/baby`  | Jump to the 2nd occurrence of `baby` |
| `10k`     | Move 10 lines up |

> Counts work with operators too — `2dw` deletes 2 words, `3dd` deletes 3 lines.
> When both the operator and motion have counts they multiply: `2d3w` deletes 6 words.

**Practical tip:** Our brains are slow at counting. For vertical jumps, enable relative line numbers so you can instantly read the jump distance to any visible line rather than counting yourself.

---

## Motion Type Forcing

After typing an operator but before the motion, you can override how Vim classifies the motion. This matters because motions are either *characterwise* or *linewise* by default, and that affects exactly what gets selected.

| Key      | Forces the motion to be... |
|----------|----------------------------|
| `v`      | Characterwise (inclusive) |
| `V`      | Linewise |
| `Ctrl-v` | Blockwise |

```vim
" dj is linewise — deletes the current line AND the next line entirely
" dvj forces characterwise — deletes from cursor to same column on next line

" d$ deletes to end of line (inclusive)
" dv$ same result usually, but the distinction matters in edge cases
"   like operating on a single-character line
```

> Most useful when a motion's default type doesn't match your intent.
> Example: `gUv}` uppercases a paragraph characterwise (stopping at the last character) rather than linewise (which would include the trailing blank line).

---

← [Back to index](README.md)
