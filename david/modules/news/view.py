# coding: utf-8
from flask import Blueprint, request, abort, redirect
from david.lib.template import st
from .model import News, Charity

bp = Blueprint('news', __name__)

@bp.route('/news/')
@bp.route('/news/p<int:page>')
def news_list(page=1):
    limit = perpage = 5
    pagi = News.query.order_by(News.create_at.desc()).paginate(page, perpage)
    items = pagi.items
    total = pagi.total
    Catname = 'News'
    endpoint = 'news.news_list'
    return st('/modules/news/index.html', **locals())

@bp.route('/news/<uid>')
def news_single(uid):
    article = News.get_or_404(uid)
    pics = article.attachment_pics()
    return st('/modules/news/show.html', **locals())

@bp.route('/charity/')
@bp.route('/charity/p<int:page>')
def charity_list(page=1):
    limit = perpage = 5
    pagi = Charity.query.order_by(Charity.create_at.desc()).paginate(page, perpage)
    items = pagi.items
    total = pagi.total
    Catname = 'Charity'
    endpoint = 'news.charity_list'
    return st('/modules/news/index.html', **locals())

@bp.route('/charity/<uid>')
def charity_single(uid):
    article = Charity.get_or_404(uid)
    pics = article.attachment_pics()
    return st('/modules/news/show.html', **locals())



__all__ = [bp]

