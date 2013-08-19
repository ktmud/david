# -*- coding: utf-8 -*-
from david.lib.mixins.props import PropsMixin, PropsItem
from david.core.article import Article, add_cat

C_GALLERY = 2

class Gallery(Article):
    cat_id = C_GALLERY
    cat_name = 'gallery'


add_cat(C_GALLERY, Gallery)
