# coding: utf-8
from flask import Blueprint, request
from david.lib.template import st
from .model import News

bp = Blueprint('news', __name__)

@bp.route('/news/')
def home():
    limit = perpage = 5
    start = request.args.get('start', '0')
    start = int(start) if start.isdigit() else 0
    news_entries = News.query.limit(limit).offset(start).all()
    total = News.query.count()
    return st('/modules/news/index.html', **locals())

__all__ = [bp]



