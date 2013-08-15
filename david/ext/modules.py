# coding: utf-8
import sys
import os
import types
from importlib import import_module

from .views import register_views
from .admin import admin

def load_module(app, name):
    package = 'david.modules.%s' % name
    mod = __import__(package, fromlist=['admin', 'bp', 'setup'])

    # register module bp and setup
    register_views(app, mod)

    # register admin view
    if hasattr(mod, 'admin'):
        admin_views = [admin.add_view(v) for v in mod.admin.views]

def load_modules(app):
    names = app.config.get('MODULES')
    m = import_module('david.modules')
    if not names:
        modules_folder = import_module('david.modules').__path__[0]
        names = [x for x in os.listdir(modules_folder) if
                '__init__' not in x]
    for m in names:
        load_module(app, m)
