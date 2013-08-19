# -*- coding: utf-8 -*-
from david.core.article.admin import ArticleAdmin
from david.ext.babel import lazy_gettext

from .model import Gallery

class GalleryAdmin(ArticleAdmin):
    pass

views = [
  GalleryAdmin(Gallery, name=lazy_gettext('Gallery'))
]
