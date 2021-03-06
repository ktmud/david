# coding: utf-8
from wtforms import SelectField

from david.ext.admin import ModelAdmin
from david.ext.admin import _

from david.modules.artist.model import Artist, all_artists

from .model import Work, Movie, TV, Music

class WorksAdmin(ModelAdmin):
    column_labels = dict(
            title=_('Title'),
            slug=_('Slug'),
            id=_('ID'),
            cat=_('Category'),
            uid=_('Slug'),
            artist_id=_('Artist'),
            pubdate=_('Publish date'),
            create_at=_('Create at'),
            update_at=_('Update at'),
            desc=_('Description'),
            content=_('Content'),
        )
    column_list = ('id', 'title', 'artist_id', 'pubdate', 'update_at', 'uid')
    column_searchable_list = ('title', )
    column_sortable_list = ('id', 'title', 'pubdate', 'update_at', 'artist_id')
    column_filters = ('pubdate', 'cat', 'artist_id')
    richtext_columns = ('desc', )

    column_formatters = {
        'artist_id': lambda v,c,m,p: Artist.get(m.artist_id)
        }

    form_columns = ('title', 'cat', 'artist_id', 'uid', 'desc', 'pubdate')

    #form_overrides = dict(cat=SelectField, artist_id=SelectField)
    form_choices = dict(
        cat=Work.cat_choices,
        artist_id=all_artists
    )

views = [
  (WorksAdmin(Movie, name=_('Movie'), category=_('Works')), 40),
  (WorksAdmin(TV, name=_('TV'), category=_('Works')), 41),
  (WorksAdmin(Music, name=_('Music'), category=_('Works')), 42),
]
