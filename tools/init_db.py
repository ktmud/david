# coding: utf-8
import sys
from david.core.db import db
from app import app

def init_db():
    print 'Init database...'
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/404')
        # drop all the database data
        db.drop_all()
        db.create_all()
    print 'Done.'
    print


if __name__ == '__main__':
    init_db()

