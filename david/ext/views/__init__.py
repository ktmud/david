# -*- coding: utf-8 -*-
import jinja2
from flask.ext.login import current_user

from david.config import HEADER_MENU, FOOTER_MENU, STATIC_ROOT, DEBUG

from .static import static_url, inline_static
from .errorhandler import setup_errorhandler
from .menu import Menu


def register_views(app, *view_modules):
    for v in view_modules:
        if hasattr(v, 'bp'):
            app.register_blueprint(v.bp)
        if hasattr(v, 'setup'):
            v.setup(app)


@jinja2.contextfunction
def get_context(c):
    return c


# menu can `add_item` and `get_item`
header_menu = Menu(HEADER_MENU)
footer_menu = Menu(FOOTER_MENU)

# app level template context globals
context_globals = {
    'user': current_user,
    'context': get_context,
    'header_menu': header_menu,
    'footer_menu': footer_menu,
    'static': static_url,
    'istatic': inline_static,
}
template_filters = {}

