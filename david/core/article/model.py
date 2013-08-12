# coding: utf-8
from david.ext.sql import db
from david.lib.props import PropsMixin, PropsItem

tags = db.Table('article_tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
    db.Column('article_id', db.Integer, db.ForeignKey('article.id'))
)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(40), unique=True)
    title = db.Column(db.Text(80))
    desc = db.Column(db.Text(255))

class Article(db.Model, PropsMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Integer)
    tags = db.relationship('Tag', secondary=tags,
                            backref=db.backref('articles', lazy='dynamic'))
    slug = db.Column(db.String(120))
    title = db.Column(db.Text(200))
    summary = db.Column(db.Text(400))
    content = db.Column(db.Text())
    create_at = db.Column(db.DateTime())
