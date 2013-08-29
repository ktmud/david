# -*- coding: utf-8 -*-
from config import SITE_ROOT
from david.core.db import db, orm, func, CatLimitedQuery, UidMixin
from david.core.accounts import User
from david.core.attachment import PictureMixin
from david.lib.utils import truncate, striptags

from david.ext.babel import lazy_gettext as _

from david.modules.artist.model import Artist


K_WORK = 210


class Work(db.Model, UidMixin, PictureMixin):

    kind = K_WORK
    kind_name = 'work'
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column('cat', db.SmallInteger, index=True, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    artist_id = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.Text())
    pubdate = db.Column(db.Date)
    create_at = db.Column(db.DateTime, default=func.now())
    update_at = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    deleted = db.Column(db.Boolean, default=False)

    @property
    def _DEFAULT_PIC(self):
        return self.extended_self._DEFAULT_PIC

    @property
    def cat_id(self):
        print self.cat
        return self.cat

    cat_name = 'work'
    catname = property(lambda x: _(x.cat_name))


    @property
    def artist(self):
        return Artist.get(self.artist_id)

    def url(self):
        return SITE_ROOT + 'work/' + self.slug

