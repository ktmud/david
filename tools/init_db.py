# coding: utf-8
from david.core.db import db
from david import app

def init_db():
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')
        # drop all the database data
        db.drop_all()
        db.create_all()


if __name__ == '__main__':
    init_db()

