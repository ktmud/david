# coding: utf-8
from importlib import import_module

from .views import register_views

from david.core.admin import admin

def load_module(app, name):
    package = 'david.modules.%s' % name
    mod = import_module(package)

    try:
        m_admin = import_module('admin', package)
        for v in m_admin.views:
            admin.add_view(v)
    except ImportError, e:
        pass
    try:
        app.register_blueprint(mod.bp)
    except Exception, e:
        pass

def load_modules(app):
    names = app.config.get('MODULES')
    for m in names:
        load_module(app, m)
