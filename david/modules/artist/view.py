# -*- coding: utf-8 -*-
from flask import Blueprint, request
from david.lib.template import st
from .model import Artist

bp = Blueprint('artist', __name__)

@bp.app_template_global('artists')
def artists():
    return Artist.query.all()

@bp.route('/artist/<uid>/')
def intro(uid):
    artist = Artist.get_or_404(uid)
    return st('modules/artist/show.html', **locals())


@bp.route('/artist/<uid>/detail')
def detail(uid):
    artist = Artist.get_or_404(uid)
    return st('modules/artist/detailed.html', **locals())
