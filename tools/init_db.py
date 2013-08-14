# coding: utf-8
from david.core.db import db
from david.core.accounts import user_datastore
from david import app

from flask.ext.security.utils import encrypt_password

def init_db():
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')
        # drop all the database data
        db.drop_all()
        db.create_all()


def add_test_users():
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        role_admin = user_datastore.find_or_create_role('admin', name='admin')
        role_editor = user_datastore.find_or_create_role('editor', name='editor')

        for i in range(1, 10):
            u = user_datastore.create_user(email='test%s@localhost' % i,
                    password=encrypt_password('test'))

        u = user_datastore.create_user(email='admin@localhost' % i,
                password=encrypt_password('test'))
        user_datastore.add_role_to_user(u, role_admin)
        u = user_datastore.create_user(email='editor@localhost' % i,
                password=encrypt_password('test'))
        user_datastore.add_role_to_user(u, role_editor)

        db.session.commit()

if __name__ == '__main__':
    init_db()
    add_test_users()

