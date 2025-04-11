# NeoVim

```shell
brew install neovim
```

The configuration for Neovim can be found at `~/.config/nvim`


If you have an existing neovim configuration

```shell
mv ~/.config/nvim ~/.config/nvim.bak
rm -rf ~/.local/share/nvim
```

NvChad is a custom Neovim configuration framework designed to give you a modern, fast, and feature-rich coding experience out of the box. It's liek a preconfigured, battaries-included setup for Neovim, built on top of Lua.

Installing NvChad

```shell
git clone https://github.com/NvChad/starter ~/.config/nvim && nvim
```

- Run `:MasonInstallAll` command after lazy.nvim finishes downloading plugins.
- Delete the `.git` folder from the nvim folder.
- Learn customization of ui & base46 from `:h nvui`

## Update

- `Lazy sync` command


## Uninstall

```shell
# Linux / MacOS (unix)
rm -rf ~/.config/nvim
rm -rf ~/.local/state/nvim
rm -rf ~/.local/share/nvim

# Flatpak (linux)
rm -rf ~/.var/app/io.neovim.nvim/config/nvim
rm -rf ~/.var/app/io.neovim.nvim/data/nvim
rm -rf ~/.var/app/io.neovim.nvim/.local/state/nvim

# Windows CMD
rd -r ~\AppData\Local\nvim
rd -r ~\AppData\Local\nvim-data

# Windows PowerShell
rm -Force ~\AppData\Local\nvim
rm -Force ~\AppData\Local\nvim-data

```

## Post Install

- Vim tutor


Swtiching themes

`SPC t h`


## Configuration for Python

Setup the PYRIGHT LSP for code completion.

The Mason plugin in NeoVim is a package manager for external dependencies.

We can use Mason to install PYRIGHT as follows

Open the tree view using 

`ctrl + n`


I don't know exactly what tmux is but I've installed it via brew.

Look it up later.

https://www.youtube.com/watch?v=4BnVeOUeZxc

https://www.youtube.com/watch?v=IobijoroGE0

lookup null-ls plugin (use the fork named none-ls)

lookup the neovim kickstart plugin as an alternative to NvChad


PYWRITE and PYLSP are the most common LSP's for Python

try to use PYLSP

