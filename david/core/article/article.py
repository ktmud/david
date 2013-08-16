# coding: utf-8
from datetime import datetime

from david.ext.babel import gettext
from david.core.db import db, orm, func
from david.core.accounts import User
from david.lib.mixins.props import PropsMixin, PropsItem
from david.lib.utils import truncate, striptags

from .tag import tags_table, Tag

class Article(db.Model, PropsMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    type_name = gettext('article')
    slug = db.Column(db.String(120), index=True, unique=True, nullable=True)
    title = db.Column(db.Text(200))
    summary = db.Column(db.Text(400), default='')
    content = db.Column(db.Text())
    create_at = db.Column(db.DateTime, default=func.now())
    update_at = db.Column(db.DateTime, default=func.now(), onupdate=func.utc_timestamp())
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id))
    tags = db.relationship('Tag', secondary=tags_table,
                    backref=db.backref('articles', lazy='dynamic'))

    def abstract(self):
        return truncate(self.summary.strip() or striptags(self.content).strip(), 255)

    @orm.reconstructor
    def init_on_load(self, *kwargs):
        """ get an article, but return with subclassed """
        pass


TYPE_COMMON = 0

# article types, later
TYPES = {
    TYPE_COMMON: Article
}

def add_type(type_id, cls):
    if type_id in TYPES:
        raise Exception('Type id %s already in use' % type_id)
    TYPES[type_id] = cls
