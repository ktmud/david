# -*- coding: utf-8 -*-
from flask import Blueprint, abort, redirect, request as req
from david.lib.template import TemplateNotFound, st

from .model import Page


bp = Blueprint('pages', __name__)


@bp.route('/')
def home():
    return st('modules/pages/home.html')

@bp.route('/<page>')
def show(page='home'):
    if page == 'show' or page.isdigit():
        return abort(404)
    try:
        return st('modules/pages/%s.html' % page)
    except TemplateNotFound, e:
        pass
    item = Page.get_or_404(page)
    return st('modules/pages/show.html', **locals())

__all__ = [bp]
