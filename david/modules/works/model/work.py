# -*- coding: utf-8 -*-
from david.core.db import db, orm, func, CatLimitedQuery, UidMixin
from david.core.accounts import User
from david.core.attachment import PictureMixin
from david.lib.utils import truncate, striptags

from david.modules.artist.model import Artist


K_WORK = 210
WORK_DEFAULT_PIC = ''


class Work(db.Model, UidMixin, PictureMixin):
    kind = K_WORK
    kind_name = 'work'
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column('cat', db.SmallInteger, index=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey(Artist.id), nullable=False)
    desc = db.Column(db.String(600))
    pubdate = db.Column(db.DateTime)
    create_at = db.Column(db.DateTime, default=func.now())
    update_at = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    deleted = db.Column(db.Boolean, default=False)

    _DEFAULT_PIC = WORK_DEFAULT_PIC

    @property
    def cat_id(self):
        return self.cat
    cat_name = 'work'

