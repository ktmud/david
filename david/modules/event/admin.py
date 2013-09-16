# -*- coding: utf-8 -*-
from david.core.article.admin import ArticleAdmin, ModelAdmin
from david.ext.admin import _

from .model import Event

class EventAdmin(ArticleAdmin):
    column_labels = dict(
            title=_('Title'),
            slug=_('Slug'),
            id=_('ID'),
            tags=_('Tags'),
            create_at=_('Create at'),
            update_at=_('Update at'),
            summary=_('Summary'),
            link=_('Out link'),
            content=_('Content')
        )
    column_list = ('id', 'title', 'create_at')
    column_sortable_list = ('id', 'title')
    form_columns = ('title', 'content', 'link', 'create_at',)
    form_widget_args = dict(
            link=dict(placeholder='http://...')
        )

views = [
  (EventAdmin(Event, name=_('Event')), 20)
]
