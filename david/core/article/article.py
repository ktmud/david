# coding: utf-8
from datetime import datetime

from david.ext.babel import lazy_gettext as _
from david.core.db import db, orm, func, CatLimitedQuery, UidMixin, SerializeMixin
from david.core.accounts import User
from david.core.attachment import PictureMixin
from david.lib.utils import truncate, striptags
from david.ext.views.static import lazy_static_url 

from config import SITE_ROOT

from .tag import tags_table, Tag


K_ARTICLE = 200

class Article(db.Model, UidMixin, PictureMixin, SerializeMixin):
    kind = K_ARTICLE
    kind_name = 'article'
    id = db.Column(db.Integer, primary_key=True)
    cat = db.Column(db.SmallInteger, index=True, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    summary = db.Column(db.Text())
    content = db.Column(db.Text())
    create_at = db.Column(db.DateTime, default=func.now())
    update_at = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    published = db.Column(db.Boolean, default=True)
    sticking = db.Column(db.Boolean, default=False)
    tags = db.relationship('Tag', secondary=tags_table,
                    backref=db.backref('articles', lazy='dynamic'))

    _DEFAULT_PIC = lazy_static_url('img/article-default-%s.png')

    @property
    def cat_id(self):
        return self.cat

    @property
    def cat_name(self):
        return CAT_NAMES[str(self.cat)]

    catname = property(lambda x: _(x.cat_name))

    query_class = CatLimitedQuery


    def abstract(self, limit=140, killwords=True):
        return truncate((self.summary or '').strip() or
                striptags(self.content or '').strip(), limit, killwords)

    def url(self):
        return '%s%s/%s' % (SITE_ROOT, self.cat_name, self.slug)

    def listpage_url(self):
        page = 1
        return '%s%s/p%s' % (SITE_ROOT, self.cat_name, page)

    @orm.reconstructor
    def init_on_load(self, *kwargs):
        """ get an article, but return with subclassed """
        pass

    def extended_self(self):
        return CATS[str(self.cat_id)].get(self.id)


# article cats, will be extended later
CATS = {
}
CAT_NAMES = {
}

def add_cat(cat_id, cls):
    if cat_id in CATS:
        raise Exception('cat id %s already in use' % cat_id)
    CATS[str(cat_id)] = cls
    CAT_NAMES[str(cat_id)] = cls.cat_name
