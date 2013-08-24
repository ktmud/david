# -*- coding: utf-8 -*-
from david.core.mapper import add_kind

from .work import K_WORK, Work as BaseWork
from .movie import C_MOVIE, Movie
from .tv import C_TV, TV
from .music import C_MUSIC, Music


class Work(BaseWork):

    @classmethod
    def get(cls, ident):
        item = BaseWork.get(ident)
        if item:
            return cat2type[item.cat_id](item)


# Export Work kind
add_kind(K_WORK, Work)

cat2type = {
    C_MOVIE: Movie,
    C_TV: TV,
    C_MUSIC: Music,
}
