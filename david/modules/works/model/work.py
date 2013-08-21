# -*- coding: utf-8 -*-
from david.core.db import db, orm, func, CatLimitedQuery
from david.core.accounts import User
from david.core.attachment.picture import PictureMixin
from david.lib.utils import truncate, striptags

from david.modules.artist.model import Artist


K_WORK = 100
WORK_DEFAULT_PIC = ''


class BaseWork(db.Model, PictureMixin):
    kind = K_WORK
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column('cat', db.SmallInteger, index=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(Artist.id), nullable=False)
    slug = db.Column(db.String(255), index=True, unique=True)
    summary = db.Column(db.String(600))
    content = db.Column(db.Text(), default='')
    pubdate = db.Column(db.DateTime)
    create_at = db.Column(db.DateTime, default=func.now())
    update_at = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    deleted = db.Column(db.Boolean, default=False)

    _DEFAULT_PIC = WORK_DEFAULT_PIC

    @property
    def cat_id(self):
        return self.cat
    cat_name = 'work'

