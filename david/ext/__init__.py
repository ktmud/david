# coding: utf-8
from .logging import setup_logging
from .modules import load_modules
from .views import register_views
from .sql import db

from flask.ext.mail import Mail
from flask.ext.security import Security, SQLAlchemyUserDatastore

from david.models.accounts import User, Role
from david.core.admin import admin

from david.views import common

mail = Mail()
security = Security()

def init_app(app):
    db.init_app(app)
    mail.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)

    admin.name = app.config.get('SITE_NAME')
    admin.init_app(app)

    register_views(app, common)

    load_modules(app)

