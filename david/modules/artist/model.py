# -*- coding: utf-8 -*-

from david.core.mapper import add_kind
from david.core.db import db, UidMixin
from david.lib.mixins.props import PropsMixin, PropsItem


K_ARTIST = 110


class Artist(db.Model, UidMixin, PropsMixin):
    kind = K_ARTIST
    kind_name = 'artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    desc = db.Column(db.Text())


add_kind(K_ARTIST, Artist)
