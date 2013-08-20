# coding: utf-8
from .article import K_ARTICLE, Article
from .tag import K_TAG, Tag
from .article import add_cat, CATS

from david.core.mapper import add_kind


add_kind(K_ARTICLE, Article)
add_kind(K_TAG, Tag)
