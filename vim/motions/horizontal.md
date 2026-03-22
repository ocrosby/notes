# Horizontal Motions

Horizontal motions move along the current line. They range from single-character steps to precise character searches.

---

## Basic

| Motion | Description |
|--------|-------------|
| `h`    | Move left one character |
| `l`    | Move right one character |
| `0`    | Move to the first character of the line |
| `^`    | Move to the first non-blank character of the line |
| `$`    | Move to the end of the line |
| `g_`   | Move to the last non-blank character of the line |

---

## Screen Line (Wrapped Text)

When `wrap` is enabled, long lines span multiple screen lines. These navigate by screen line rather than logical line:

| Motion | Description |
|--------|-------------|
| `g0`   | Move to the first character of the screen line |
| `g^`   | Move to the first non-blank character of the screen line |
| `gm`   | Move to the middle of the screen width |
| `g$`   | Move to the last character of the screen line |
| `\|`   | Move to column [count] on the current line |

---

## Word by Word

A **word** is a sequence of letters, digits, or underscores — or a sequence of other non-blank characters. A **WORD** is any sequence of non-blank characters separated by whitespace. WORDs are broader and particularly useful in code.

| Motion | Description |
|--------|-------------|
| `w`    | Jump to the beginning of the next word |
| `b`    | Jump to the beginning of the previous word |
| `e`    | Jump to the end of the current/next word |
| `ge`   | Jump to the end of the previous word |
| `W`    | Jump to the beginning of the next WORD |
| `B`    | Jump to the beginning of the previous WORD |
| `E`    | Jump to the end of the current/next WORD |
| `gE`   | Jump to the end of the previous WORD |

> Word motions allow for more precise changes; WORD motions allow for faster movement.

```
wwww ==> v   v v   v   v
         word. are two words
         word. is one WORD
WWW  ==> ^     ^  ^   ^
```

---

## Find Character

Jump directly to any character on the current line. This is the most precise horizontal motion.

| Motion    | Description |
|-----------|-------------|
| `f{char}` | Move to the next occurrence of `{char}` on the line |
| `F{char}` | Move to the previous occurrence of `{char}` on the line |
| `t{char}` | Move just before the next occurrence of `{char}` (until) |
| `T{char}` | Move just after the previous occurrence of `{char}` |
| `;`       | Repeat the last `f`/`F`/`t`/`T` forward |
| `,`       | Repeat the last `f`/`F`/`t`/`T` backward |

```
f(   ==> v                        v
         const fireball = function(target){
wwww ==> ^     ^        ^ ^       ^

t(   ==> v                       v
         const fireball = function(target){
f(   ==> ^                        ^
```

> `t` is especially useful with operators — `dt(` deletes everything up to (but not including) the next `(`.

Use `;` and `,` to walk between matches instead of retyping the search:

```
fd;;   ==> v   v               v        v
           let damage = weapon.damage * d20();
```

---

← [Back to index](README.md)
