# coding: utf-8
from flask.ext.security import Security
from flask.ext.login import LoginManager
from flask import Blueprint, request, g

from david.core.accounts import user_datastore, User

security = Security()
login_manager = LoginManager()

bp = Blueprint('login', __name__)

def setup_accounts_manager(app):
    security.init_app(app, user_datastore)
    #login_manager.init_app(app)

    app.register_blueprint(bp)

    @login_manager.user_loger
    def load_user(userid):
        return User.get(userid)
