# -*- coding: utf-8 -*-
import jinja2
from flask import jsonify, current_app
from flask import json
from flask.ext.login import current_user

from david.ext.babel import admin_gettext

from .static import static_url, inline_static, urlmap, admin_static_url
from .menu import Menu
from .errorhandler import setup_errorhandler
from .accounts import setup_accounts_manager


@jinja2.contextfunction
def get_context(c):
    return c


# app level template context globals
context_globals = {
    '_a': admin_gettext,
    'dir': dir,
    'jsonify': json.htmlsafe_dumps,
    'user': current_user,
    'context': get_context,
    'static': static_url,
    'admin_static': admin_static_url,
    'urlmap': urlmap,
    'istatic': inline_static,
}
template_filters = {
    'json': json.htmlsafe_dumps,
    'n2br': lambda x: x.replace('\n', '<br />'),
}



def setup(app):
    setup_accounts_manager(app)
    setup_errorhandler(app)

    app.context_processor(inject_app_contexts)
    app.jinja_env.filters.update(template_filters)



def inject_app_contexts():
    header_menu = Menu(current_app.config.get('HEADER_MENU'))
    footer_menu = Menu(current_app.config.get('FOOTER_MENU'))
    context_globals.update({
        'header_menu': header_menu,
        'footer_menu': footer_menu,
    })
    return context_globals



def register_views(app, *view_modules):
    for v in view_modules:
        if hasattr(v, 'bp'):
            app.register_blueprint(v.bp)
        if hasattr(v, 'setup'):
            v.setup(app)

