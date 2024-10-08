# Basic `vi` Editor Instructions

## Opening a File
To open a file with `vi`, use the following command:
```sh
vi filename
```

## Modes in vi

**vi** operates in several modes:

- **Normal Mode**: This is the default mode when you open a file in `vi`. In this mode, you can navigate through the file, make changes, and execute commands.
- **Insert Mode**: In this mode, you can insert text into the file. To enter Insert Mode, press `i`.
- **Command Mode**: In this mode, you can execute commands. To enter Command Mode, press `:`.
- **Visual Mode**: In this mode, you can select text. To enter Visual Mode, press `v`.
- **Replace Mode**: In this mode, you can replace text. To enter Replace Mode, press `R`.
- **Ex Mode**: This mode is similar to Command Mode but is used for more advanced commands. To enter Ex Mode, press `Q`.
- **Command-Line Mode**: This mode is used to enter commands from the command line. To enter Command-Line Mode, press `/`.
- **Select Mode**: This mode is used to select text. To enter Select Mode, press `V`.
- **Visual Block Mode**: This mode is used to select text in a block. To enter Visual Block Mode, press `Ctrl + V`.
- **Insert Normal Mode**: This mode is used to insert text in Normal Mode. To enter Insert Normal Mode, press `Ctrl + O`.

## Configuring `vi` with Custom Settings

You can customize `vi` by adding settings to your `.vimrc` file. Here are some custom settings:

### Show Line Numbers

To show line numbers in `vi`, add the following line to your `.vimrc` file:

```sh
set number
```

or in the short form

```sh
set nu
```

### Enable Syntax Highlighting

To enable syntax highlighting in `vi`, add the following line to your `.vimrc` file:

```sh
syntax on
```

### Set Tab Width

To set the tab width in `vi`, add the following line to your `.vimrc` file:

```sh
set tabstop=4
```

### Set Auto Indent

To enable auto-indent in `vi`, add the following line to your `.vimrc` file:

```sh
set autoindent
```

### Shift Width

To set the shift width in `vi`, add the following line to your `.vimrc` file:

```sh
set shiftwidth=4
```

### Set Expand Tab

To set expand tab in `vi`, add the following line to your `.vimrc` file:

```sh
set expandtab
```

### Enable Line Wrapping

To enable line wrapping in `vi`, add the following line to your `.vimrc` file:

```sh
set wrap
```

### Highlight Search Results

To highlight search results in `vi`, add the following line to your `.vimrc` file:

```sh
set hlsearch
```


### Show Matching Parentheses

To show matching parentheses in `vi`, add the following line to your `.vimrc` file:

```sh
set showmatch
```

### Example .vimrc file

Here is an example `.vimrc` file with the above settings:

```text
set nu
syntax on
set tabstop=4
set shiftwidth=4
set expandtab
set wrap
set hlsearch
set autoindent
set showmatch 
```

## Basic Navigation

- h: Move the cursor left
- j: Move the cursor down
- k: Move the cursor up
- l: Move the cursor right
- w: Move the cursor to the beginning of the next word
- b: Move the cursor to the beginning of the previous word
- 0: Move the cursor to the beginning of the line
- $: Move the cursor to the end of the line
- G: Move the cursor to the end of the file
- gg: Move the cursor to the beginning of the file

## More Navigation Commands

- f<char>: Move the cursor to the next occurrence of a character
- F<char>: Move the cursor to the previous occurrence of a character

## Basic Editing

- i: Enter Insert Mode before the cursor
- a: Enter Insert Mode after the cursor
- x: Delete the character under the cursor
- dd: Delete the current line
- yy: Copy (yank) the current line
- p: Paste the copied or deleted text after the cursor
- u: Undo the last change
- Ctrl + r: Redo the last change

## Saving and Exiting

- :w: Save the file
- :q: Quit the file
- :wq: Save and quit the file
- :q!: Quit the file without saving

## Searching

- /<pattern>: Search for a pattern in the file
- n: Move to the next occurrence of the pattern
- N: Move to the previous occurrence of the pattern

## Replacing Text

- :%s/<old>/<new>/g: Replace all occurrences of `<old>` with `<new>` in the file

## Additional Resources

For more detailed instructions, refer to the vi manual by typing:

```Shell
man vi
```
