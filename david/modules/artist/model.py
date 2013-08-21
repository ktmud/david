# -*- coding: utf-8 -*-

from david.core.db import db
from david.lib.mixins.props import PropsMixin, PropsItem

class Artist(db.Model, PropsMixin):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(60), unique=True)
    name = db.Column(db.String(255))
