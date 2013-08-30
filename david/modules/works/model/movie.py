# -*- coding: utf-8 -*-
from david.lib.mixins.wrapper import WrapperMixin
from david.ext.views.static import lazy_static_url 

from .work import Work

C_MOVIE = 1001

class Movie(WrapperMixin):
    cat_id = C_MOVIE
    cat_name = 'movie'
    _DEFAULT_PIC = lazy_static_url('img/works/movie-default-%s.gif')
