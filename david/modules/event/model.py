# -*- coding: utf-8 -*-
from datetime import datetime
from flask import url_for
from david.core.db import db, func
from david.core.mapper import add_kind
from david.lib.mixins.props import PropsMixin, PropsItem
from david.ext.views.static import lazy_static_url
from david.core.attachment import PictureMixin
from david.lib.utils import truncate, striptags


K_EVENT = 301

class Event(db.Model, PictureMixin):
    kind = K_EVENT
    kind_name = 'event'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    link = db.Column(db.String(255), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    content = db.Column(db.Text())

    _DEFAULT_PIC = lazy_static_url('img/article-default-%s.png')

    def url(self):
        return self.link

    def abstract(self, limit=140):
        return truncate(striptags(self.content or '').strip(), limit, killwords=True)

    @property
    def thumb_url(self):
        return self.picture_url('sqr120')

    def serialize(self):
        pics = [dict(title=x.title, desc=x.desc, large_url=x.url('large'),
                     thumb_url=x.thumb_url)
                for x in self.attachment_pics()]
        return dict(id=self.id, title=self.title,
                url=self.url(),
                abstract=self.abstract(),
                thumb_url = self.thumb_url,
                median_url = self.picture_url('median'),
                pics=pics)


add_kind(K_EVENT, Event)
