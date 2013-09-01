# coding: utf-8
from flask import Blueprint, request, abort, redirect
from david.lib.template import st
from .model import News

bp = Blueprint('news', __name__)

@bp.route('/news/')
@bp.route('/news/p<int:page>')
def list(page=1):
    limit = perpage = 5
    pagi = News.query.order_by(News.create_at.desc()).paginate(page, perpage)
    items = pagi.items
    total = pagi.total
    return st('/modules/news/index.html', **locals())

@bp.route('/news/<uid>')
def single(uid):
    article = News.get_or_404(uid)
    return st('/modules/news/show.html', **locals())


__all__ = [bp]



