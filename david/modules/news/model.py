# coding: utf-8
from david.core.article import Article, add_cat
from david.lib.mixins.props import PropsItem
from david.lib.mixins.wrapper import WrapperMixin

C_NEWS = 1

class News(Article):
    cat_id = C_NEWS
    cat_name = 'news'

add_cat(C_NEWS , News)
