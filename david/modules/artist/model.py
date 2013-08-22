# -*- coding: utf-8 -*-

from david.core.db import db, UidMixin
from david.lib.mixins.props import PropsMixin, PropsItem

class Artist(db.Model, UidMixin, PropsMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    desc = PropsItem('desc')

