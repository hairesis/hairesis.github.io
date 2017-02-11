# -*- coding: utf-8 -*-

# flake8: noqa

import tinkerer
import tinkerer.paths
from datetime import datetime


# Change this to the name of your blog
project = 'The next wave.'

# Change this to the tagline of your blog
tagline = 'If you don\'t have time to do it right, when will you have time to do it over? -- John Wooden'

# Change this to the description of your blog
description = 'A notebook rather than a Blog. Ideas, snippets... mostly an experiment written in the bed beside my sleepy beautiful wife.'

# Change this to your name
author = 'Andrea Baglioni'

# Change this to your copyright string
copyright = '{:%Y}, {:s}'.format(datetime.now(), author)

# Change this to your blog root URL (required for RSS feed)
website = 'http://0x41ndrea.ddns.net/blog/html/'

# **************************************************************
# More tweaks you can do
# **************************************************************

# Add your Disqus shortname to enable comments powered by Disqus
disqus_shortname = None

# Change your favicon (new favicon goes in _static directory)
html_favicon = '_static/tinkerer.ico'

# Pick another Tinkerer theme or use your own
html_theme = 'flat'

# Theme-specific options, see docs

html_theme_options = { 'accent_color': '#e74c3c'}

# Link to RSS service like FeedBurner if any, otherwise feed is
# linked directly
rss_service = None

# Generate full posts for RSS feed even when using "read more"
rss_generate_full_posts = False

# Number of blog posts per page
posts_per_page = 10

# Character use to replace non-alphanumeric characters in slug
slug_word_separator = '_'

# Set to page under /pages (eg. "about" for "pages/about.html")
landing_page = None

# Set to override the default name of the first page ("Home")
first_page_title = None

# **************************************************************
# Edit lines below to further customize Sphinx build
# **************************************************************

# Add other Sphinx extensions here
extensions = ['tinkerer.ext.blog', 'tinkerer.ext.disqus']

# Add other template paths here
templates_path = ['_templates']

# Add other static paths here
html_static_path = ['_static', tinkerer.paths.static]

# Add other theme paths here
html_theme_path = ['_themes', tinkerer.paths.themes]

# Add file patterns to exclude from build
exclude_patterns = ['drafts/*', '_templates/*', 'venv']

# Add templates to be rendered in sidebar here
html_sidebars = {
    '**': ['recent.html', 'searchbox.html']
}

# Add an index to the HTML documents.
html_use_index = False

# **************************************************************
# Do not modify below lines as the values are required by
# Tinkerer to play nice with Sphinx
# **************************************************************

source_suffix = tinkerer.source_suffix
master_doc = tinkerer.master_doc
version = tinkerer.__version__
release = tinkerer.__version__
html_title = project
html_show_sourcelink = False
html_add_permalinks = None
