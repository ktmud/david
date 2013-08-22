# coding: utf-8
from david.ext.admin import ModelAdmin
from david.ext.babel import lazy_gettext
from david.ext.babel import lazy_gettext as _

from .model import Work

class WorksAdmin(ModelAdmin):
    column_labels = dict(
            title=_('Title'),
            slug=_('Slug'),
            id=_('ID'),
            pubdate=_('Publish date'),
            create_at=_('Create at'),
            update_at=_('Update at'),
            desc=_('Description'),
            content=_('Content'),
        )
    column_list = ('id', 'title', 'pubdate', 'update_at')
    column_sortable_list = ('id', 'title', 'pubdate')

views = [
  WorksAdmin(Work, name=lazy_gettext('Works'))
]
