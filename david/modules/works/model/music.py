# -*- coding: utf-8 -*-
from david.lib.mixins.wrapper import WrapperMixin
from david.ext.views.static import lazy_static_url 

from .work import Work

C_MUSIC = 1002

class Music(WrapperMixin):
    cat_id = C_MUSIC
    cat_name = 'music'
    _DEFAULT_PIC = lazy_static_url('img/works/music-default-%s.gif')
