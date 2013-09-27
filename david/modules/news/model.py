# coding: utf-8 from david.core.article import Article, add_cat
from david.core.article import Article, add_cat
from david.lib.mixins.props import PropsItem
from david.lib.mixins.wrapper import WrapperMixin

C_NEWS = 101
C_CHARITY = 102

class News(Article):
    cat_id = C_NEWS
    cat_name = 'news'

class Charity(Article):
    cat_id = C_CHARITY
    cat_name = 'charity'

add_cat(C_NEWS , News)
add_cat(C_CHARITY , Charity)
