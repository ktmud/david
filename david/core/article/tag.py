# -*- coding: utf-8 -*-
from david.core.db import db, orm, func

K_TAG = 2

tags_table = db.Table('article_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'))
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String, unique=True)
    name = db.Column(db.String)
    desc = db.Column(db.Text)
    create_at = db.Column(db.DateTime, default=func.now())

