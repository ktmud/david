# coding: utf-8
import os
import types
from importlib import import_module

from .views import register_views
from .admin import admin

def load_module(app, name):
    package = 'david.modules.%s' % name
    mod = import_module(package)

    register_views(app, mod)

    try:
        m_admin = import_module('admin', package)
        for v in m_admin.views:
            admin.add_view(v)
    except ImportError, e:
        pass

def load_modules(app):
    names = app.config.get('MODULES')
    m = import_module('david.modules')
    if not names:
        modules_folder = import_module('david.modules').__path__[0]
        names = [x for x in os.listdir(modules_folder) if
                '__init__' not in x]
    for m in names:
        load_module(app, m)
