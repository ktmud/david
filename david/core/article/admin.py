# -*- coding: utf-8 -*-
""" admin view for article model """
from david.ext.admin import ModelAdmin, Proped, admin
from david.ext.babel import gettext
from .tag import Tag

class ArticleAdmin(Proped, ModelAdmin):

    column_labels = dict(
            title=gettext('Title'),
            slug=gettext('Slug'),
            id=gettext('ID'),
            tags=gettext('Tags'),
            create_at=gettext('Create at'),
            update_at=gettext('Update at'),
            summary=gettext('Summary'),
            content=gettext('Content')
        )
    column_list = ('id', 'title', 'update_at', 'tags')
    column_sortable_list = ('id', 'title')
    form_columns = ('title', 'summary', 'content', 'tags', 'create_at')


class TagAdmin(ModelAdmin):
    column_labels = dict(
            name=gettext('Name'),
            slug=gettext('Slug'),
            id=gettext('ID'),
            create_at=gettext('Create at'),
            desc=gettext('Description')
        )


admin.add_view(TagAdmin(Tag))
