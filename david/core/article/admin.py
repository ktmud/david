# -*- coding: utf-8 -*-
""" admin view for article model """
from david.ext.admin import ModelAdmin, Proped, admin
from david.ext.babel import lazy_gettext as _
from .tag import Tag


class ArticleAdmin(ModelAdmin):

    column_labels = dict(
            title=_('Title'),
            slug=_('Slug'),
            id=_('ID'),
            tags=_('Tags'),
            create_at=_('Create at'),
            update_at=_('Update at'),
            summary=_('Summary'),
            content=_('Content')
        )
    column_list = ('id', 'title', 'create_at', 'update_at')
    column_sortable_list = ('id', 'title')

    form_columns = ('title', 'content', 'summary', 'create_at',)
    richtext_columns = ('content', )
    form_widget_args = {
        'summary': dict(rows='4',
            placeholder=_('will abstract content body if not set')),
        'create_at': dict(placeholder=_('default to current time')),
        'content': dict(rows='12')
    }


class TagAdmin(ModelAdmin):
    column_labels = dict(
            name=_('Name'),
            slug=_('Slug'),
            id=_('ID'),
            create_at=_('Create at'),
            desc=_('Description')
        )
    form_columns = ('name', 'desc')


#admin.add_view(TagAdmin(Tag, name=_('Tag'), category=_('Article')))
