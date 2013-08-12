# coding: utf-8
from david.lib.template import st
from jinja2 import TemplateNotFound

def show_error_page(code):
    def f(e):
        status_code = code if isinstance(code, int) else 500
        return st('errors/%s.html' % code), status_code
    f.__name__ = 'show_error_%s' % code
    return f


custom_handlers = []

def add_handler(instance_check, handler):
    custom_handlers.append((instance_check, handler))


def setup_errorhandler(app):
    for code in [404, 403, 500]:
        app.error_handler_spec[None][code] = show_error_page(code)
    app.error_handler_spec[None][None] = custom_handlers
