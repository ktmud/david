# coding: utf-8
import sys
import os
import types
from importlib import import_module

from .views import register_views
from .admin import admin


def load_module(app, name):
    package = 'david.modules.%s' % name
    mod = __import__(package, fromlist=['admin', 'bp', 'setup', 'view'])

    # register module bp and setup
    register_views(app, mod)

    if hasattr(mod, 'view'):
        register_views(app, mod.view)

    return mod


def load_modules(app):
    names = app.config.get('MODULES')
    m = import_module('david.modules')
    if not names:
        modules_folder = import_module('david.modules').__path__[0]
        names = [x for x in os.listdir(modules_folder) if
                '__init__' not in x]
    mods = [load_module(app, m) for m in names]
    register_admin_views(mods)


def register_admin_views(modules):
    views = []
    for mod in modules:
        if hasattr(mod, 'admin') and hasattr(mod.admin, 'views'):
            views += mod.admin.views
    views = sorted(views, key=lambda x: x[1])
    for x in views:
        admin.add_view(x[0])
