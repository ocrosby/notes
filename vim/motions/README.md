# VIM Motions

If you've ever watched an experienced Vim user edit code, it looks like magic. Their cursor teleports across the file. They rename a variable inside quotes without selecting anything. They jump between functions with a single keystroke. None of it is magic — it's motions.

**Motions are how you move in Vim.** Every navigation command you type is a motion: moving one character, jumping to the end of a word, searching for a pattern, leaping to a matching bracket. Motions are the vocabulary of movement.

What makes them powerful is that they compose. A motion on its own moves the cursor. A motion paired with an operator *does something* to the text it covers. `d` (delete) + `w` (word) = `dw` (delete word). `c` (change) + `i"` (inside quotes) = `ci"` (change what's inside quotes). Once you learn the motions, every operator you learn multiplies your editing power.

---

## How to Read These Docs

Each page covers one concept area. If you're just starting out, read them in order — each one builds on the last. If you're looking something up, use the summary table at the bottom to find what you need.

| Page | What you'll learn |
|------|-------------------|
| [Horizontal Motions](horizontal.md) | Moving along a line — from single characters to precise jumps |
| [Vertical Motions](vertical.md) | Moving between lines — from steps to search-powered teleportation |
| [File, Window & Semantic Navigation](navigation.md) | Jumping across an entire file or following code references |
| [Text Object Selection](text-objects.md) | Selecting structured regions like words, blocks, and quoted strings |
| [Marks](marks.md) | Saving positions and jumping back to them |
| [Jump Navigation](jumps.md) | Retracing your steps through Vim's movement history |
| [Bracket & Code Structure](brackets.md) | Navigating nested code — scopes, methods, and conditionals |
| [Modifiers](modifiers.md) | Making any motion more powerful with counts and type overrides |

---

## Quick Reference

| Type | Motions | Page |
|------|---------|------|
| Character | `h`, `l` | [horizontal](horizontal.md) |
| Line start/end | `0`, `^`, `$`, `g_` | [horizontal](horizontal.md) |
| Screen line | `g0`, `g^`, `gm`, `g$` | [horizontal](horizontal.md) |
| Word | `w`, `b`, `e`, `ge`, `W`, `B`, `E`, `gE` | [horizontal](horizontal.md) |
| Find character | `f`, `F`, `t`, `T`, `;`, `,` | [horizontal](horizontal.md) |
| Line up/down | `j`, `k`, `gj`, `gk`, `-`, `+`, `_` | [vertical](vertical.md) |
| Sentence | `(`, `)` | [vertical](vertical.md) |
| Paragraph/block | `{`, `}`, `Ctrl-u`, `Ctrl-d` | [vertical](vertical.md) |
| Section | `[[`, `]]`, `[]`, `][` | [vertical](vertical.md) |
| Search | `/`, `?`, `n`, `N`, `*`, `#` | [vertical](vertical.md) |
| File | `gg`, `G`, `{line}G`, `{count}%`, `%` | [navigation](navigation.md) |
| Window | `H`, `M`, `L` | [navigation](navigation.md) |
| Semantic | `gd`, `gf` | [navigation](navigation.md) |
| Text objects | `aw`, `iw`, `ab`, `ib`, `a"`, `i"` | [text-objects](text-objects.md) |
| Marks | `m{a-z}`, `` `{mark} ``, `''`, `` `. `` | [marks](marks.md) |
| Jump history | `Ctrl-o`, `Ctrl-i`, `g;`, `g,` | [jumps](jumps.md) |
| Unmatched brackets | `[(`, `[{`, `])`, `]}` | [brackets](brackets.md) |
| Methods | `]m`, `[m`, `]M`, `[M` | [brackets](brackets.md) |
| Preprocessor | `[#`, `]#` | [brackets](brackets.md) |
| C comments | `[*`, `[/`, `]*`, `]/` | [brackets](brackets.md) |
| Count multiplier | `{count}{motion}` | [modifiers](modifiers.md) |
| Motion type forcing | `v`, `V`, `Ctrl-v` after operator | [modifiers](modifiers.md) |

---

**One tip before you start:** resist the urge to learn everything at once. Pick two or three motions per session and use them until they're automatic. Speed comes from muscle memory, not memorisation.
