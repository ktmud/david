# coding: utf-8
from david.core.article import Article, add_type
from david.lib.mixins.props import PropsItem
from david.lib.mixins.wrapper import WrapperMixin

TYPE_NEWS = 1

class News(Article):
    type = TYPE_NEWS
    type_name = '新闻'

add_type(TYPE_NEWS , News)
