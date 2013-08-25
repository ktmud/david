# coding: utf-8
from david.core.article.admin import ArticleAdmin
from david.ext.babel import lazy_gettext as _

from .model import News

class NewsAdmin(ArticleAdmin):
    pass

views = [
  NewsAdmin(News, name=_('News'))
]
