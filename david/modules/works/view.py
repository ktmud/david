# -*- coding: utf-8 -*-
from flask import Blueprint, request
from david.lib.template import st

bp = Blueprint('works', __name__)

@bp.route('/works/')
def home():
    return st('/modules/works/index.html', **locals())

@bp.route('/works/movie/')
def movies():
    return st('/modules/works/movie/index.html', **locals())

@bp.route('/works/music/')
def musics():
    return st('/modules/works/music/index.html', **locals())

@bp.route('/works/tv/')
def tvs():
    return st('/modules/works/movie/index.html', **locals())

__all__ = [bp]
