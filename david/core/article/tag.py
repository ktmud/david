# -*- coding: utf-8 -*-
from david.core.db import db, orm, func

tags_table = db.Table('article_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'))
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(40), unique=True)
    name = db.Column(db.Text(80))
    desc = db.Column(db.Text(255))
    create_at = db.Column(db.DateTime, default=func.now())

