# coding: utf-8
from david.ext.sql import db
from david.lib.props import PropsMixin, PropsItem

class Article(db.Model, PropsMixin):
    pass
