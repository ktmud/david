# -*- coding: utf-8 -*-
import re
from sqlalchemy.sql import or_
from david.lib.store import redis_store as rs
from david.core.article import Article
from david.modules.news.model import News

DB_HOMEPAGE_ARTICLES = 'homepage_articles'

RE_SPLITTER = re.compile(r'\s+')


def get_homepage_articles():
    data = rs.get(DB_HOMEPAGE_ARTICLES) or ''
    ids, captions = _parse_data(data)
    if ids:
        return Article.gets(ids), captions
    return News.query.order_by(News.create_at.desc()).limit(5).all(), [''] * 5


def _parse_line(x):
    if RE_SPLITTER.search(x):
        x, caption = RE_SPLITTER.split(x, 1)
    else:
        caption = ''
    x = x.strip('/')
    if '/' in x:
        x = x.split('/')[-1]
    return x, caption

def _parse_data(data):
    data = [x.strip() for x in data.split('\n')]
    ids, captions = [], []
    for x in data:
        if not x: continue
        a, b = _parse_line(x)
        ids.append(a)
        captions.append(b)
    return ids, captions

