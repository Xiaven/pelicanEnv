#!/usr/bin/env python
# -*- coding: utf-8 -*- #
#from __future__ import unicode_literals

AUTHOR = u'raven'
SITENAME = u'Raven Site'
SITEURL = 'http://raven47git.github.io/myblog'

THEME = './pelican-themes/gum'
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'files']


ARTICLE_URL = ('articles/{slug}.html')
ARTICLE_SAVE_AS = ARTICLE_URL 



TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

GOOGLE_ANALYTICS = "UA-67802935-1"

DISQUS_SITENAME = "raven47"
