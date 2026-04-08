# groovecoder.com

Personal blog powered by Jekyll and hosted on GitHub Pages.

## Local Development

### Prerequisites

- Ruby (version 2.7 or higher)
- Bundler gem

### Setup

1. Install dependencies:
```bash
bundle install
```

2. Run the local development server:
```bash
bundle exec jekyll serve
```

3. Open your browser to http://localhost:4000

### Build

To build the site for production:

```bash
bundle exec jekyll build
```

The generated site will be in the `_site` directory.

## Writing Posts

Create new posts in the `_posts` directory with the format:

```
YYYY-MM-DD-title.markdown
```

### Post Frontmatter

Minimal frontmatter example:

```yaml
---
layout: post
title: Your Post Title
date: YYYY-MM-DD HH:MM:SS -0500
categories:
- category1
- category2
tags:
- tag1
- tag2
---
```

## License

Content is licensed under [Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
