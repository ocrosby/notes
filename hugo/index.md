# Hugo

Hugo is a static site generator written in Go.  It is designed to be fast and flexible.  Hugo is a great choice for blogs, documentation, and other content-driven sites.

## Features

- Fast build times
- Flexible content organization
- Easy to use
- Extensible with themes and plugins
- Supports Markdown, HTML, and other formats
- Built-in server for development
- Live reloads for changes
- Customizable URLs
- Multilingual support
- Built-in taxonomies and menus
- Image processing
- Asset management
- Custom output formats
- Shortcodes
- Data templates

Example Hugo Sites:

- [Hugo Themes](https://themes.gohugo.io)
- [Hugo Documentation](https://gohugo.io/documentation/)
- [Hugo Community](https://discourse.gohugo.io)

## Installationn

```Shell
brew install hugo
```

## Usage

Displaying version

```Shell
hugo version
```

Creating and run a Hugo site with the Anake theme.

```Shell
hugo new site example-site
cd example-site
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo "theme = 'ananke'" >> hugo.toml
hugo server
```

Add a new page to your site

```Shell
hugo new content content/posts/my-first-post.md
```

Hugo created the file in the content/posts directory. It should look something like this:

```Markdown
+++
title = 'My First Post'
date = 2024-01-14T07:07:07+01:00
draft = true
+++
```

Notice the **draft** value in the [front matter](https://gohugo.io/content-management/front-matter/) is **true**.  By default, Hugo does not publish draft content when you build the site.


Add some Markdown to the body of the post, but do not change the draft value.

```Markdown
+++
title = 'My First Post'
date = 2024-01-14T07:07:07+01:00
draft = true
+++
## Introduction

This is **bold** text, and this is *emphasized* text.

Visit the [Hugo](https://gohugo.io) website!
```

Save the file and run the Hugo server again.

```Shell
hugo server --buildDrafts
hugo server -D
```

View your site at the URL displayed in your terminal. Keep the development server running as you continue to add and change content.

When satisfied with your new content, set the front matter draft parameter to false.


Edit the hugo.toml file 

1. Set the baseURL for your production site.  Ths value must begin with the protocol and end with a slash, as shown above.
2. Set the languageCode to your language and region 'en-us'.
3. Set the title for your production site.

Start the development server to see your changes, remembering to include draft content.

```Shell
hugo server --buildDrafts
hugo server -D
```

When you are ready to publish your site, build the site with the following command:

```Shell
hugo
```

## References

- [Hugo](https://gohugo.io)
- [Hugo Themes](https://themes.gohugo.io)
- [Quick Start](https://gohugo.io/getting-started/quick-start/)
- [Easy Guide](https://www.ii.com/easy-way-play-with-hugo-theme-examplesite/)
