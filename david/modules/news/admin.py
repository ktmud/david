# coding: utf-8
from david.core.article.admin import ArticleAdmin
from david.ext.admin import _

from .model import News

class NewsAdmin(ArticleAdmin):
    pass

views = [
  NewsAdmin(News, name=_('News'), category=_('Article'))
]
