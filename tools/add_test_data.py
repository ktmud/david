# -*- coding: utf-8 -*-
from david.core.db import db
from david.core.accounts import user_datastore
from david import app

from flask.ext.security.utils import encrypt_password

def add_test_users():
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        role_admin = user_datastore.find_or_create_role('admin',
                desc='Site Admin')
        role_editor = user_datastore.find_or_create_role('editor',
                desc='Content Editor')

        for i in range(1, 5):
            u = user_datastore.create_user(email='test%s@localhost' % i,
                    password=encrypt_password('test'))

        u = user_datastore.create_user(email='admin@localhost',
                password=encrypt_password('test'))
        user_datastore.add_role_to_user(u, role_admin)
        u = user_datastore.create_user(email='editor@localhost',
                password=encrypt_password('test'))
        user_datastore.add_role_to_user(u, role_editor)

        db.session.commit()

def add_test_articles():
    pass

if __name__ == '__main__':
    add_test_users()
    add_test_articles()

