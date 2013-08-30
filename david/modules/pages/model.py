# -*- coding: utf-8 -*-
from flask import url_for

from david.core.db import db, UidMixin
from david.lib.mixins.props import PropsMixin, PropsItem

from david.core.mapper import add_kind


K_PAGE = 300


class Page(db.Model, UidMixin, PropsMixin):
    kind = K_PAGE
    kind_name = 'page'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text())

    def url(self):
        return url_for('pages.show', page=self.slug)


add_kind(K_PAGE, Page)
