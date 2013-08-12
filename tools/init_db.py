# coding: utf-8
from david.core.db import db
from david.core.accounts import user_datastore
from david import app

from flask.ext.security.utils import encrypt_password

def init_db():

    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        db.drop_all()
        db.create_all()
        for i in range(1, 10):
            u = user_datastore.create_user(email='test%s@localhost' % i,
                    password=encrypt_password('test'))
            user_datastore.activate_user(u)
        db.session.commit()

if __name__ == '__main__':
    init_db()


