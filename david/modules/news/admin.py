# coding: utf-8
from david.core.admin import ModelAdmin

class NewsAdmin(ModelAdmin):
    pass

views = [NewsAdmin(name='新闻', endpoint='news.admin')]
