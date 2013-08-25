# -*- coding: utf-8 -*-
from david.ext.admin import ModelAdmin
from david.ext.babel import lazy_gettext as _

from .model import Artist

class ArtistAdmin(ModelAdmin):

    column_labels = dict(
            name=_('Name'),
            id=_('ID'),
            uid=_('Slug'),
            summary=_('Short bio'),
            desc=_('Detail'),
        )
    column_list = ('id', 'name', 'uid')
    form_widget_args = {
        'summary': dict(rows='8')
    }

views = [
  ArtistAdmin(Artist, name=_('Artist'))
]
