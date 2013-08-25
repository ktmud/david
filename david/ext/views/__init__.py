# -*- coding: utf-8 -*-
import jinja2
from flask import jsonify
from flask import json
from flask.ext.login import current_user

from david.config import HEADER_MENU, FOOTER_MENU
from david.config import STATIC_ROOT, DEBUG
from david.ext.babel import admin_gettext

from .static import static_url, inline_static, urlmap, admin_static_url
from .menu import Menu
from .errorhandler import setup_errorhandler
from .accounts import setup_accounts_manager


def setup(app):
    setup_accounts_manager(app)
    setup_errorhandler(app)

    @app.context_processor
    def inject_app_contexts():
        return context_globals

    app.jinja_env.filters.update(template_filters)



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
    'dir': dir,
    'jsonify': json.htmlsafe_dumps,
    'user': current_user,
    'context': get_context,
    'header_menu': header_menu,
    'footer_menu': footer_menu,
    'static': static_url,
    'admin_static': admin_static_url,
    'urlmap': urlmap,
    'istatic': inline_static,
}
template_filters = {
    'json': json.htmlsafe_dumps,
    'n2br': lambda x: x.replace('\n', '<br />'),
}

