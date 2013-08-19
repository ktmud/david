# coding: utf-8
from datetime import datetime

from david.ext.babel import lazy_gettext
from david.core.db import db, orm, func
from david.core.accounts import User
from david.core.attachment.picture import PictureMixin
from david.lib.utils import truncate, striptags

from david.config import ARTICLE_DEFAULT_PIC

from .tag import tags_table, Tag


K_ARTICLE = 1
C_COMMON = 0

class Article(db.Model, PictureMixin):
    kind = K_ARTICLE,
    id = db.Column(db.Integer, primary_key=True)
    _cat_id = db.Column('cat', db.Integer, index=True, nullable=False)
    title = db.Column(db.Text(200), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    slug = db.Column(db.String(120), index=True, unique=True)
    summary = db.Column(db.Text(400), default='')
    content = db.Column(db.Text(), default='')
    create_at = db.Column(db.DateTime, default=func.now())
    update_at = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    tags = db.relationship('Tag', secondary=tags_table,
                    backref=db.backref('articles', lazy='dynamic'))

    _DEFAULT_PIC = ARTICLE_DEFAULT_PIC

    cat_id = C_COMMON
    cat_name = 'article'

    @property
    def catname(self):
        return lazy_gettext(self.cat_name)

    def abstract(self):
        return truncate(self.summary.strip() or striptags(self.content).strip(), 255)

    @property
    def uid(self):
        return str(self.slug or self.id)

    def url(self):
        return '/%s/%s' % (self.cat_name, self.uid)

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
