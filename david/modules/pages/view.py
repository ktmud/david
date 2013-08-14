# -*- coding: utf-8 -*-
from flask import Blueprint, abort, redirect, request as req
from david.lib.template import TemplateNotFound, st

bp = Blueprint('pages', __name__)

@bp.route('/')
@bp.route('/<page>')
def show_pages(page='index'):
    if req.path == 'index':
        return redirect(url_for('pages.show_pages'))
    try:
        return st('pages/%s.html' % page)
    except TemplateNotFound, e:
        abort(404)

__all__ = [bp]
