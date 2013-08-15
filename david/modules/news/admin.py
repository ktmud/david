# coding: utf-8
from david.ext.admin import ModelAdmin

from .model import News

class NewsAdmin(ModelAdmin):
    pass

views = [
  NewsAdmin(News, name='新闻')
]
