# coding: utf-8
from david.core.db import db
from david.core.accounts import user_datastore
from david import app

def init_db():
    db.create_all(app=app)
    for i in range(1, 10):
        user_datastore.create_user(email='test%s@localhost' % i, password='test')
    db.session.commit()

if __name__ == '__main__':
    init_db()


