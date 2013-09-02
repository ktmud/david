# -*- coding: utf-8 -*-
from sqlalchemy.sql import or_
from david.lib.store import redis_store as rs
from david.core.article import Article
from david.modules.news.model import News

DB_HOMEPAGE_ARTICLES = 'homepage_articles'


def get_homepage_articles():
    data = rs.get(DB_HOMEPAGE_ARTICLES) or ''
    ids = _parse_data(data)
    if ids:
        return Article.gets(ids)
    return News.query.order_by(News.create_at.desc()).limit(5).all()


def _parse_line(x):
    x = x.strip('/')
    if '/' in x:
        x = x.split('/')[-1]
    return x

def _parse_data(data):
    data = [x.strip() for x in data.split('\n')]
    return [_parse_line(x) for x in data if x]

