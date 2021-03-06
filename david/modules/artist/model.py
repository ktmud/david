# -*- coding: utf-8 -*-
from config import SITE_ROOT

from david.lib.utils import lazyget
from david.core.mapper import add_kind
from david.core.db import db, UidMixin
from david.lib.mixins.props import PropsMixin, PropsItem
from david.lib.utils import truncate, striptags
from david.ext.views.static import lazy_static_url 

from david.core.attachment import PictureMixin




K_ARTIST = 110


@lazyget
def all_artists():
    return [(str(a.id), a.name) for a in Artist.query.all()]

class Artist(db.Model, UidMixin, PictureMixin):
    kind = K_ARTIST
    kind_name = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    summary = db.Column(db.Text())
    desc = db.Column(db.Text())

    _DEFAULT_PIC = lazy_static_url('img/artist-default-%s.png')

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.id == other.id

    def url(self):
        return SITE_ROOT + 'artist/' + self.slug

    def abstract(self, limit=140):
        return truncate((self.summary or '').strip() or striptags(self.desc or '').strip(), limit)


add_kind(K_ARTIST, Artist)
