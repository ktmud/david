# coding: utf-8
from .logging import setup_logging
from .debug import setup_debug
from .modules import load_modules
from .views import setup_errorhandler, context_globals, template_filters
from .views.accounts import setup_accounts_manager

from flask.ext.cache import Cache
from flask.ext.mail import Mail

from david.core.db import db
from david.ext.admin import admin

# in case we need some references via `from david.ext import mail`
mail = Mail()
cache = Cache(config={ 'CACHE_TYPE': 'david.lib.cache.get_redis_cache' })

def init_app(app):
    setup_logging(app)

    db.app = app
    db.init_app(app)
    mail.init_app(app)
    cache.init_app(app)

    admin.name = app.config.get('SITE_NAME')
    admin.init_app(app)

    load_modules(app)

    # after all modules ars loaded, setup the context globals
    @app.context_processor
    def inject_app_contexts():
        return context_globals

    for k, v in template_filters.items():
        app.jinja_env.filters[k] = v

    setup_debug(app)
    setup_errorhandler(app)
