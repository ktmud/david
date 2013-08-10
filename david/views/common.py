# coding: utf-8
from flask import Blueprint, abort
from jinja2 import TemplateNotFound

from david.lib.template import st

bp = Blueprint('common', __name__)

@bp.route('/')
@bp.route('/<page>')
def show(page='index'):
    try:
        return st('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


def setup(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return st('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error(error):
        return st('errors/500.html'), 500

    @app.errorhandler(403)
    def not_allowed(error):
        return st('errors/403.html'), 403


__all__ = [bp, setup]
