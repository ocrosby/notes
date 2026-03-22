# VIM Macros

A macro is a **recorded sequence of keystrokes** that you can replay on demand. Anything you can type in Vim — motions, operators, searches, commands — can be recorded and played back. Macros are the tool you reach for when you need to perform the same multi-step edit on many places in a file.

---

## The Core Loop

```
q{register}   →   type your keystrokes   →   q   →   @{register}
  (record)                                  (stop)     (replay)
```

There are 26 registers (`a`–`z`). Think of them as 26 named slots you can store macros in.

---

## Step 1 — Record a Macro

```
q{a-z}
```

- Press `q` followed by a register letter (e.g., `qa`) to start recording into that register.
- The status bar shows `recording @a`.
- Type every keystroke you want to record — motions, edits, searches, commands, everything.
- Press `q` again to stop recording.

> **Tip:** Use `q` (lowercase) registers for quick one-off macros. Uppercase `qA` *appends* to register `a` rather than overwriting it.

---

## Step 2 — Replay a Macro

```
@{a-z}    replay the macro stored in register {a-z}
@@        replay the last used macro
```

- `@a` runs the macro stored in `a` once.
- `5@a` runs it 5 times.
- `@@` re-runs whichever macro you ran last — useful for quick repetition.

---

## Step 3 — A Complete Example

**Task:** Add a semicolon to the end of every line in this block:

```
let x = 1
let y = 2
let z = 3
```

1. Move to the first line.
2. `qa` — start recording into register `a`.
3. `A;<Esc>` — append `;` at end of line, return to normal mode.
4. `j` — move down one line.
5. `q` — stop recording.
6. `2@a` — replay twice to fix the remaining two lines.

Result:
```
let x = 1;
let y = 2;
let z = 3;
```

> The `j` at the end is intentional — always end your macro with a motion that advances to the *next* target. This makes count repetition (`5@a`) and recursive macros work correctly.

---

## Applying a Macro to Multiple Lines

### Method 1 — Count prefix

```
{count}@a
```

Run the macro `{count}` times in sequence. Stops early if the macro hits an error (e.g., end of file).

### Method 2 — Visual selection + `:normal`

Select lines with `V`, then:

```
:'<,'>normal @a
```

Runs the macro on every line in the selection, regardless of whether individual runs fail.

### Method 3 — `:global`

```
:g/pattern/normal @a
```

Runs the macro on every line matching `pattern`. Precise and powerful.

---

## Viewing Macro Contents

```
:registers        list all registers and their contents
:reg a            show only register a
:reg ab           show registers a and b
```

Macro contents look like raw keystrokes — `^M` is Enter, `^[` is `<Esc>`, etc.

---

## Editing a Macro

Recorded a macro but made a small mistake? Don't re-record — edit it.

1. Paste the macro into the buffer: `"ap` (paste register `a` on a new line).
2. Edit the text as normal — fix the mistake, add keystrokes, remove steps.
3. Yank it back: visually select the corrected text, then `"ay` to yank back into register `a`.

> This works because macros are just text stored in registers. Editing them is editing text.

---

## Recursive Macros

A macro can call itself to repeat until it fails (e.g., hits end of file). This is an alternative to using a count.

**Setup:**
1. Clear the register first: `qaq` (record nothing into `a`, immediately stop).
2. Now record the macro: `qa` → your keystrokes → `@a` → `q`.

The `@a` at the end calls the macro recursively. When it eventually hits an error (no more matches, end of buffer, etc.), Vim stops without complaint.

**Example — add semicolons to every line until EOF:**

```
qaq            " clear register a
qa             " start recording
A;<Esc>        " append semicolon
j              " move to next line
@a             " recurse
q              " stop
@a             " run it
```

> Always clear the register before recording a recursive macro (`qaq`). If register `a` contained an old macro, the new recording would call the old version during the `@a` step — not what you want.

---

## Appending to a Macro

Use an uppercase register letter to **append** to an existing macro rather than overwrite it:

```
qA    " append to register a (note: uppercase A)
```

Useful when you recorded a macro but forgot to include a final step.

---

## Common Patterns

### Normalize a line

```
qa
^                " go to first non-blank
gU$              " uppercase the entire line
j                " advance
q
```

### Wrap each line in quotes

```
qa
I"<Esc>          " insert quote at start
A"<Esc>          " append quote at end
j
q
```

### Comment out a block (e.g., Python)

```
qa
I# <Esc>         " prepend "# "
j
q
{count}@a
```

### Rename a repeated symbol (search-based)

```
qa
n                " jump to next match
cw               " change word
NewName<Esc>     " type replacement
q
@@               " keep pressing @@ to walk through matches
```

---

## Pitfalls to Avoid

| Pitfall | Why | Fix |
|---------|-----|-----|
| Macro stops early | A motion or search failed mid-run | End each macro step with a reliable motion; check `:reg a` to inspect |
| Forgot to end with `j` | Count repetition re-edits the same line | Re-record with `j` as the last keystroke |
| Old macro in register before recursive record | `@a` calls stale macro during recording | Always `qaq` to clear before recording recursive macros |
| Macro acts on wrong column | You started recording mid-word | Begin with `^` or `0` to normalize position before editing |
| Counts overshoot | `10@a` ran past intended range | Use `:g/pattern/normal @a` for bounded application |

---

## Quick Reference

| Command              | Description |
|----------------------|-------------|
| `q{a-z}`             | Start recording into register |
| `q`                  | Stop recording |
| `@{a-z}`             | Replay macro from register |
| `@@`                 | Replay last macro |
| `{count}@{a-z}`      | Replay macro [count] times |
| `qA` (uppercase)     | Append to existing macro in register `a` |
| `"ap`                | Paste macro contents into buffer (to inspect/edit) |
| `"ay`                | Yank edited text back into register `a` |
| `:reg`               | List all register contents |
| `:'<,'>normal @a`    | Run macro on each line of a visual selection |
| `:g/pattern/normal @a` | Run macro on every line matching pattern |
