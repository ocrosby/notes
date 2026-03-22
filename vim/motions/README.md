# VIM Motions

Motions are commands that move the cursor with speed and precision. They are composed of one or more keys typed as **melodies** — pressed one after the other in rapid succession, not simultaneously.

Motions can be used standalone to navigate, or combined with **operators** (`d`, `c`, `y`, `>`, etc.) to act on text. The same motion that moves you to the end of a word also defines what `dw` deletes.

---

## Sections

| Topic | What it covers |
|-------|----------------|
| [Horizontal Motions](horizontal.md) | `h`/`l`, line start/end, word-by-word, find-character |
| [Vertical Motions](vertical.md) | `j`/`k`, sentences, paragraphs, search patterns, sections |
| [File, Window & Semantic Navigation](navigation.md) | `gg`/`G`, `%`, `H`/`M`/`L`, `gd`, `gf` |
| [Text Object Selection](text-objects.md) | `aw`, `iw`, `ab`, `ib`, `a"`, `i"`, tags, and more |
| [Marks](marks.md) | Setting, jumping to, and traversing marks |
| [Jump Navigation](jumps.md) | Jumplist (`Ctrl-o`/`Ctrl-i`) and changelist (`g;`/`g,`) |
| [Bracket & Code Structure](brackets.md) | Unmatched brackets, methods, preprocessor, C comments |
| [Modifiers](modifiers.md) | Count multipliers and motion type forcing |

---

## Summary

| Type | Motions | Reference |
|------|---------|-----------|
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

**Repeaters** (`n`, `N`, `;`, `,`, `Ctrl-o`, `Ctrl-i`) let you keep moving by pressing a single key — train yourself to rely on them instead of retyping searches.
