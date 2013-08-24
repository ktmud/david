# coding: utf-8
from datetime import datetime

from david.ext.babel import lazy_gettext
from david.core.db import db, orm, func, CatLimitedQuery, UidMixin
from david.core.accounts import User
from david.core.attachment import PictureMixin
from david.lib.utils import truncate, striptags

from david.config import ARTICLE_DEFAULT_PIC, SITE_ROOT

from .tag import tags_table, Tag


K_ARTICLE = 200
C_COMMON = 0

class Article(db.Model, UidMixin, PictureMixin):
    kind = K_ARTICLE
    kind_name = 'article'
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.SmallInteger, index=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.String(800))
    content = db.Column(db.Text())
    create_at = db.Column(db.DateTime, default=func.now())
    update_at = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    deleted = db.Column(db.Boolean, default=False)
    sticking = db.Column(db.Boolean, default=False)
    tags = db.relationship('Tag', secondary=tags_table,
                    backref=db.backref('articles', lazy='dynamic'))

    _DEFAULT_PIC = ARTICLE_DEFAULT_PIC

    @property
    def cat_id(self):
        return self.cat

    cat_name = 'article'

    query_class = CatLimitedQuery

    @property
    def catname(self):
        return lazy_gettext(self.cat_name)

    def abstract(self, limit=140):
        return truncate((self.summary or '').strip() or striptags(self.content or '').strip(), limit)

    def url(self):
        return '%s%s/%s' % (SITE_ROOT, self.cat_name, self.slug)

    @orm.reconstructor
    def init_on_load(self, *kwargs):
        """ get an article, but return with subclassed """
        pass


# article cats, will be extended later
CATS = {
    str(C_COMMON): Article
}

def add_cat(cat_id, cls):
    if cat_id in CATS:
        raise Exception('cat id %s already in use' % cat_id)
    CATS[str(cat_id)] = cls
