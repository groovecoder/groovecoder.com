# groovecoder.com

Luke Crouch's personal blog. Jekyll 4.3 static site on GitHub Pages.

## Quick Start

```bash
bundle install
bundle exec jekyll serve  # http://localhost:4000
bundle exec jekyll build  # generates _site/
```

## Structure

- `_posts/` - 192 blog posts (2004-2017), many migrated from WordPress
- `_layouts/` - base.html (modernized HTML5), post.html (legacy XHTML)
- `_config.yml` - Jekyll config, 5 posts per page pagination
- `index.html` - Home page with pagination
- `uploads/` - Media assets organized by year
- `testpages/` - Experimental pages

## Key Facts

- **Branch**: gh-pages (main and deployment)
- **URL**: https://groovecoder.com
- **License**: Creative Commons BY-SA 4.0
- **Tagline**: "203 Non-Authoritative Information"

## Recent Changes

- Created Gemfile with Jekyll 4.3, webrick, logger, jekyll-paginate
- Modernized base.html layout (HTML5, responsive)
- Cleaned WordPress frontmatter from posts
- Updated _config.yml with full site settings
- Added README.md

## Quirks

- post.html still uses XHTML 1.0 Transitional
- Legacy WordPress metadata in post frontmatter (wordpress_id, etc)
- Google Analytics in post.html (UA-22568404-1)
- Old zBench theme files preserved in /zbench
- OpenAttribute plugin files in /openattribute-for-wordpress
