# coding: utf-8
from .logging import setup_logging
from .debug import setup_debug
from .modules import load_modules
from .views import setup as setup_views

from flask.ext.cache import Cache
from flask.ext.mail import Mail

from david.core.db import db
from .admin import admin
from .babel import init_babel

# in case we need some references via `from david.ext import mail`
mail = Mail()
cache = Cache(config={ 'CACHE_TYPE': 'david.lib.cache.get_redis_cache' })

def init_app(app):
    setup_logging(app)

    db.app = app
    db.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    init_babel(app)

    admin.name = app.config.get('SITE_NAME')
    admin.init_app(app)

    load_modules(app)
    setup_views(app)
    setup_debug(app)
