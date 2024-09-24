#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sacha schutz'
SITENAME = 'Sacha Schutz'
# SITEURL = 'https://dridk.me'
AUTHOR_EMAIL ='sacha@labsquare.org'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['gravatar','sitemap','render_math', 'simple_footnotes']

# #PLUGIN MATH 
# MATH_JAX = {'auto_insert':False, 'responsive':False}

# PURE THEME CONFIG
THEME = "pelican-themes/pure-single"

COVER_IMG_URL = "https://dridk.me/images/common/dnaquestion_banner.jpg"
PROFILE_IMG_URL= "https://dridk.me/images/avatar.jpg"
TAGLINE="bioinformatique génétique médecine"
# Blogroll
MENUITEMS = (
         ('Biologie','category/biologie.html'),
         ('Informatique','category/informatique.html'),
         ('Historique', 'archives.html'),
         ('A propos', 'pages/contact-Fr.html')      
        )

# Social widget
SOCIAL = (
    ('github', 'https://github.com/dridk'),
    ('twitter-square', 'https://twitter.com/dridk'),
    ('rss-square', 'https://dridk.me/feeds/all.atom.xml')
   )

GITHUB_CONTENT="https://github.com/dridk/blog/tree/master/content"

DEFAULT_PAGINATION = 10

DISPLAY_PAGES_ON_MENU = True	
DISPLAY_CATEGORIES_ON_MENU = True	
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'daily',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


