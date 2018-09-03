#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

SITENAME = "Ares Central"

SITEURL            = os.environ.get("SITEURL", "")
RELATIVE_URLS      = not SITEURL

FEED_DOMAIN            = SITEURL
FEED_ALL_ATOM          = None if RELATIVE_URLS else "news.atom"
CATEGORY_FEED_ATOM     = None
AUTHOR_FEED_ATOM       = None
FEED_ALL_RSS           = None
CATEGORY_FEED_RSS      = None
AUTHOR_FEED_RSS        = None
TRANSLATION_FEED_ATOM  = None
TRANSLATION_FEED_RSS   = None

OUTPUT_PATH              = "output/"
DELETE_OUTPUT_DIRECTORY  = not RELATIVE_URLS

THEME             = "./theme"
THEME_STATIC_DIR  = ""
TYPOGRIFY         = True

PATH                    = "content"
PATH_METADATA           = "^(?P<fullname>(?:.*/)?(?P<slug>[^/.]*))(?P<ext>\..*)?$"
IGNORE_FILES            = [".*", "*.rsti", "*.css", "*.scss"]
USE_FOLDER_AS_CATEGORY  = False
DIRECT_TEMPLATES        = ["index"]

PLUGIN_PATHS      = ["plugins"]
PLUGINS           = ["pelican_youtube", "assets"]
DOCUTILS_SETTINGS = {"tab_width": 2}

MENUITEMS = [
    ("Home",    ""),
    ("About",   "about/"),
    ("Antares", "antares/"),
    ("Plugins", "plugins/"),
    ("Links",   "links/"),
]

TIMEZONE      = "UTC"
DEFAULT_LANG  = "en"
DATE_FORMATS  = {
    'en': '%B %d %Y',
    'jp': '%Y年%m月%d日',
}

PAGE_PATHS        = [""]
PAGE_URL          = "{fullname}/"
PAGE_SAVE_AS      = PAGE_URL + "index.html"

STATIC_PATHS      = [""]
STATIC_URL        = "{fullname}{ext}"
STATIC_SAVE_AS    = "{fullname}{ext}"

ARTICLE_PATHS     = ["news"]
ARTICLE_URL       = "news/{slug}/"
ARTICLE_SAVE_AS   = ARTICLE_URL + "index.html"

DIRECT_TEMPLATES  += ["tags"]
TAGS_URL          = "tags/"
TAGS_SAVE_AS      = TAGS_URL + "index.html"
TAG_URL           = "tags/{slug}/"
TAG_SAVE_AS       = TAG_URL + "index.html"

DEFAULT_PAGINATION = 10
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

AUTHOR_URL = ""
AUTHOR_SAVE_AS = "" 
CATEGORY_URL = ""
CATEGORY_SAVE_AS = "" 
