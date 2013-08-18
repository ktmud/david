# -*- coding: utf-8 -*-
""" admin view for article model """
from david.ext.admin import ModelAdmin, Proped, admin
from david.ext.babel import lazy_gettext as _
from .tag import Tag

class ArticleAdmin(Proped, ModelAdmin):

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
    column_list = ('id', 'title', 'update_at', 'tags')
    column_sortable_list = ('id', 'title')
    form_columns = ('title', 'summary', 'content', 'tags', 'create_at')


class TagAdmin(ModelAdmin):
    column_labels = dict(
            name=_('Name'),
            slug=_('Slug'),
            id=_('ID'),
            create_at=_('Create at'),
            desc=_('Description')
        )
    form_columns = ('name', 'desc')


admin.add_view(TagAdmin(Tag, name=_('Tag')))
