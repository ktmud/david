# -*- coding: utf-8 -*-
from david.core.mapper import add_kind
from david.ext.babel import lazy_gettext as _

from .work import K_WORK, Work as BaseWork
from .movie import C_MOVIE, Movie
from .tv import C_TV, TV
from .music import C_MUSIC, Music

cat2type = {
    C_MOVIE: Movie,
    C_TV: TV,
    C_MUSIC: Music,
}


class Work(BaseWork):

    cat_choices = [(str(cat_id), _(cls.__name__)) for cat_id, cls in cat2type.items()]

    @classmethod
    def get(cls, ident):
        item = BaseWork.get(ident)
        if item:
            return cat2type[item.cat_id](item)

    @property
    def extended_self(self):
        return cat2type[self.cat_id](self)


# Export Work kind
add_kind(K_WORK, Work)

