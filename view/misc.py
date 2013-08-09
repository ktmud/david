# coding: utf-8
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('misc', __name__)

__all__ = [bp]


@bp.route('/')
@bp.route('/<page>')
def show(page='index'):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)


