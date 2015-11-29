#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Filippo Rossi & Luke Chang'
SITENAME = u'fexmetrica'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'


PATH = 'content'
STATIC_PATHS = ['examples', 'img', 'CNAME' ]
ARTICLE_PATHS = ['examples']
THEME = 'theme'

# DIRECT_TEMPLATES = ['examples']
DIRECT_TEMPLATES = (('index','example','tag','categories','archive'))
PAGINATED_DIRECT_TEMPLATES = (('example',))


MD_EXTENSIONS = [ 'codehilite(css_class=highlight)', 'extra', 'mdext.fix_code_blocks' ]

import os, sys
sys.path.append(os.path.join(os.getcwd(), "jinjaext"))
from table_of_contents import TableOfContents as TOC

JINJA_FILTERS = {
		  'extract_toc_info' : TOC.extractTableOfContentsInfo,
		  'create_toc' : TOC.createTableOfContents,
		  'add_toc_hooks' : TOC.addTableOfContentsHooks
		}

# GOOGLE_ANALYTICS = ""

PLUGINS = []

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
