# -*- coding: utf-8 -*-
from david.core.mapper import add_kind

from .work import K_WORK, BaseWork
from .movie import C_MOVIE, Movie
from .tv import C_TV, TV
from .music import C_MUSIC, Music


class Work(BaseWork):

    @classmethod
    def get(cls, ident):
        item = BaseWork.get(ident)
        if item:
            return item.extended_self()

    def extended_self(self):
        return cat2type[self.cat_id](self)


# Export Work kind
add_kind(K_WORK, Work)

cat2type = {
    str(C_MOVIE): Movie,
    str(C_TV): TV,
    str(C_MUSIC): Music,
}
