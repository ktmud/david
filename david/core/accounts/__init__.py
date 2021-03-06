# coding: utf-8
from flask.ext.security import UserMixin, RoleMixin

from config import BABEL_DEFAULT_LOCALE, BABEL_DEFAULT_TIMEZONE

from david.core.mapper import add_kind
from david.core.db import db, UidMixin
from david.lib.mixins.props import PropsMixin, PropsItem
from flask.ext.security import SQLAlchemyUserDatastore

# Define models
roles_users = db.Table(
            'roles_users',
            db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
            db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
        )

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(255))



K_USER = 100

class User(db.Model, UserMixin, UidMixin, PropsMixin):
    kind = K_USER
    kins_name = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

    last_login_at = PropsItem('ll')
    current_login_at = PropsItem('cl')
    last_login_ip = PropsItem('llip')
    current_login_ip = PropsItem('clip')
    login_count = PropsItem('lc')
    name = PropsItem('name')
    locale = PropsItem('locale', BABEL_DEFAULT_LOCALE)
    timezone = PropsItem('timezone', BABEL_DEFAULT_TIMEZONE)

    @property
    def display_name(self):
        return self.name or (self.uid if self.uid else self.email.split('@')[0])

Account = User

user_datastore = SQLAlchemyUserDatastore(db, User, Role)

add_kind(K_USER, User)
