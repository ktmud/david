# -*- coding: utf-8 -*-
from david.core.article.admin import ArticleAdmin
from david.ext.admin import _

from .model import Photos, Magazine

class PhotosAdmin(ArticleAdmin):
    pass


class MagazineAdmin(PhotosAdmin):
    pass


views = [
  (MagazineAdmin(Magazine, name=_('Magazine')), 30),
  (PhotosAdmin(Photos, name=_('Photos')), 31)
]
