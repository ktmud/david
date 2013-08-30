# -*- coding: utf-8 -*-
from david.core.mapper import add_kind
from david.ext.babel import lazy_gettext as _

from .work import K_WORK, Work as BaseWork
from .movie import C_MOVIE, Movie as MovieWrapper
from .tv import C_TV, TV as TVWrapper
from .music import C_MUSIC, Music as MusicWrapper

cat2type = {
    C_MOVIE: MovieWrapper,
    C_TV: TVWrapper,
    C_MUSIC: MusicWrapper,
}


class Work(BaseWork):

    cat_choices = [(str(cat_id), _(cls.__name__)) for cat_id, cls in cat2type.items()]

    cat_id = None

    @classmethod
    def get(cls, ident):
        item = BaseWork.get(ident)
        if item:
            return cat2type[item.cat](item)

    @property
    def extended_self(self):
        return cat2type[self.cat](self)

class Music(BaseWork):
    cat_id = C_MUSIC

class Movie(BaseWork):
    cat_id = C_MOVIE

class TV(BaseWork):
    cat_id = C_TV


# Export Work kind
add_kind(K_WORK, Work)

