# -*- coding: utf-8 -*-
from flask import Blueprint, request, g, abort, redirect
from david.lib.template import st
from .model import *

from ..artist.model import Artist


bp = Blueprint('works', __name__)

@bp.route('/works/')
def home():
    return st('/modules/works/index.html', **locals())


@bp.route('/work/<uid>/')
def show(uid):
    work = Work.get_or_404(uid)
    cat = work.cat_name
    return st('/modules/works/%s/show.html' % cat, **locals())


catname2id = {
    'movie': C_MOVIE,
    'music': C_MOVIE,
    'tv': C_TV, 
}

@bp.route('/works/<catname>/')
@bp.route('/works/<catname>/p<int:page>')
def list(catname, page=1):
    print catname
    cat_id = catname2id.get(catname)
    if not cat_id:
        abort(404)
    page = int(page)
    perpage = 50
    pagination = Work.query.filter(Work.cat == cat_id).paginate(page, perpage)
    items = pagination.items
    return st('/modules/works/%s/index.html' % catname, **locals())

__all__ = [bp]
