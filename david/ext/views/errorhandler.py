# coding: utf-8
from flask import request, jsonify

from david.lib.template import st
from jinja2 import TemplateNotFound
from sqlalchemy.orm.exc import NoResultFound

def show_error_page(code):
    def f(e):
        status_code = code if isinstance(code, int) else 500
        if request.is_xhr:
            return jsonify({ 'r': status_code })
        return st('errors/%s.html' % code), status_code
    f.__name__ = 'show_error_%s' % code
    return f


default_handlers = {}

for code in [404, 403, 500]:
    default_handlers[code] = show_error_page(code)


custom_handlers = [
    (NoResultFound, default_handlers[404])
]


def add_handler(instance_check, handler=show_error_page(500)):
    custom_handlers.append((instance_check, handler))

def setup_errorhandler(app):
    app.error_handler_spec[None] = default_handlers
    app.error_handler_spec[None][None] = custom_handlers
