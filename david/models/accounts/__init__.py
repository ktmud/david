# coding: utf-8
from flask.ext.security import UserMixin, RoleMixin

from david.ext.sql import db
from david.lib.props import PropsMixin, PropsItem

# Define models
roles_users = db.Table(
            'roles_users',
            db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
            db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
        )

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin, PropsMixin):
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
