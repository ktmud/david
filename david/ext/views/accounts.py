# coding: utf-8
from flask.ext.security import Security
#from flask.ext.login import LoginManager
from flask import Blueprint, request, g

from david.core.accounts import user_datastore, User

security = Security()
#login_manager = LoginManager()

def setup_accounts_manager(app):
    security.init_app(app, user_datastore)
    #login_manager.init_app(app)

    #@login_manager.user_loader
    #def load_user(userid):
        #return User.get(userid)
