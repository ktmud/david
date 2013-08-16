# coding: utf-8
from david.core.article.admin import ArticleAdmin

from .model import News

class NewsAdmin(ArticleAdmin):
    pass

views = [
  NewsAdmin(News, name='新闻')
]
