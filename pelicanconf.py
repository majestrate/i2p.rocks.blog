#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeff'
SITENAME = u'i2p.rocks -- blog about i2p and other stuff'
SITEURL = '/blog'

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_DOMAIN = SITEURL
FEED_MAX_ITEMS = 0
FEED_ALL_RSS = 'rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('I2P', 'https://geti2p.net/'), ('Submit an I2P related blog via Github','https://github.com/majestrate/i2p.rocks.blog/'))

SOCIAL = (('GitHub', 'https://github.com/majestrate'),
           ('Twitter', 'https://twitter.com/ampernand'),
           ('RSS', FEED_DOMAIN + '/' + FEED_ALL_RSS),
           ('ATOM', FEED_DOMAIN + '/' + FEED_ALL_ATOM))
# markdown extensions
MD_EXTENSIONS = ['codehilite(linenums=False,guess_lang=True,use_pygments=True)', 'extra']

MENUITEMS = (('RSS Feed', FEED_DOMAIN + '/' + FEED_ALL_RSS), ('Atom Feeed', FEED_DOMAIN + '/' + FEED_ALL_ATOM))

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 150

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# begin custom configuration

# path to plugins directory
PLUGINS_PATHS = []

# plugins in use
PLUGINS = [
]

# theme name
THEME = 'i2p.rocks-theme'

# keywords for meta tag
KEYWORDS = [
    "i2pd",
    "i2p",
    "development",
    "nntpchan",
    "livechan",
    "llarp"
]

# css files in order of include
CSS_FILES = []

# css theme in use
css_theme = 'simplecss'
# extra css files
css_theme_stylesheets = ['github.css']
# local style override
css_local_override = 'local.css'


# js script files
JS_FILES = []

# do we want to use jquery?
use_jquery = False
# jquery version to use
jquery_version = "2.2.1"

# jquery related script files
# in order of include
jquery_jsfiles = [
    "jquery-{}.min.map",
    "jquery-{}.min.js"
]

# theme related script files
theme_jsfiles = [
    "zjs.min.js",
    "simplecss.min.js"
]


# first append jquery files as needed if enabled
if use_jquery:
    # if we want to use jquery append all the required jquery files
    for js in jquery_jsfiles:
        JS_FILES.append(js.format(jquery_version))


# append css theme script files
for js in theme_jsfiles:
    JS_FILES.append(js)

# add css theme to css stylesheets
CSS_FILES.append('{}.min.css'.format(css_theme))

# append extra theme stylesheets to css stylesheets
for css in css_theme_stylesheets:
    CSS_FILES.append(css)

# add local site stylesheet override
CSS_FILES.append(css_local_override)

# folders for static files
STATIC_PATHS = ['images']

OPEN_GRAPH_IMAGE = 'theme/images/og-logo.png'
FAVICON = OPEN_GRAPH_IMAGE

ABS_SITEURL = 'https://i2p.rocks/blog'
