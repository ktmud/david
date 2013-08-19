# -*- coding: utf-8 -*-
import jinja2
from flask.ext.login import current_user

from david.config import HEADER_MENU, FOOTER_MENU, STATIC_ROOT, DEBUG
from david.ext.babel import admin_gettext

from .static import static_url, inline_static
from .menu import Menu
from .errorhandler import setup_errorhandler
from .accounts import setup_accounts_manager


def setup(app):
    setup_accounts_manager(app)
    setup_errorhandler(app)

    @app.context_processor
    def inject_app_contexts():
        return context_globals

    for k, v in template_filters.items():
        app.jinja_env.filters[k] = v



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
    '_a': admin_gettext,
    'user': current_user,
    'context': get_context,
    'header_menu': header_menu,
    'footer_menu': footer_menu,
    'static': static_url,
    'istatic': inline_static,
}
template_filters = {}

