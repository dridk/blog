#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'sacha schutz'
SITENAME = 'SACHA SCHUTZ'
# SITEURL = 'http://dridk.me'
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
PLUGINS = ['gravatar','sitemap']

# #PLUGIN MATH 
# MATH_JAX = {'auto_insert':False, 'responsive':False}

# PURE THEME CONFIG
THEME = "pelican-themes/pure-single"

COVER_IMG_URL = "http://dridk.me/images/splash.svg"
PROFILE_IMG_URL= "http://dridk.me/images/avatar.jpg"
TAGLINE="bioinformatique génétique médecine"
# Blogroll
MENUITEMS = (('Archive', 'archives.html'),
         ('A propos', 'pages/contact-Fr.html'),
         ('Applications', 'pages/application-Fr.html')
         )
GOOGLE_ANALYTICS="UA-44929010-2"
DISQUS_SITENAME = "dridkme"
DISQUS_ON_PAGES = True
# Social widget
SOCIAL = (
    ('github', '/archives.html'),
    ('twitter-square', 'https://twitter.com/dridk'),
    ('rss-square', 'https://github.com/dridk.atom')
   )

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
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
