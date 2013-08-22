# -*- coding: utf-8 -*-
import os
from datetime import datetime, timedelta

from david.core.db import db
from david.core.accounts import user_datastore, User
from david.core.article import CATS
from david import app

from flask.ext.security.utils import encrypt_password

TOOLS_FOLER = os.path.dirname(__file__)

def add_test_users():
    print 'Init users...'
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        role_admin = user_datastore.find_or_create_role('admin',
                desc='Site Admin')
        role_editor = user_datastore.find_or_create_role('editor',
                desc='Content Editor')

        for i in range(1, 3):
            u = user_datastore.create_user(email='test%s@localhost' % i,
                    password=encrypt_password('test'))

        u = user_datastore.create_user(email='admin@localhost',
                password=encrypt_password('test'))
        user_datastore.add_role_to_user(u, role_admin)
        u = user_datastore.create_user(email='editor@localhost',
                password=encrypt_password('test'))
        user_datastore.add_role_to_user(u, role_editor)

        db.session.commit()
    print 'Done.'
    print

def add_test_articles():
    print 'Creating articles...'
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        lorem = open(TOOLS_FOLER + '/data/loremipsum.txt').read()

        for cat, model in CATS.items():
            for i in range(5):
                article = model()
                article.cat = cat
                article.title = '%s 测试文章 - %s' % (article.cat_name, i + 1)
                article.content = lorem
                article.owner_id = User.query.first().id
                db.session.add(article)
        db.session.commit()
    print 'Done.'
    print


def add_test_works():
    print 'Creating Works...'

    from david.modules.works.model import cat2type, Work
    from david.modules.artist.model import Artist

    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        lorem = open(TOOLS_FOLER + '/data/loremipsum.txt').read()

        artist = Artist()
        artist.name = 'David Lau'
        artist.uid = 'david'

        artist2 = Artist()
        artist2.name = 'Marry Jen'
        artist2.uid = 'marry'

        db.session.add_all([artist, artist2])
        db.session.commit()

        artist1, artist2 = Artist.gets(['david', 'marry'])
        artist.desc = artist2.desc = lorem

        pubdate = datetime.now()
        one_year = timedelta(days=366)
        one_month = timedelta(days=30)

        for cat, model in cat2type.items():
            for i in range(10):
                pubdate -= one_year
                for i in range(3):
                    pubdate -= one_month
                    obj = Work()
                    print model.__name__
                    obj.title = '%s作品%s' % (model.__name__, i + 1)
                    obj.cat = cat
                    obj.pubdate = pubdate
                    obj.desc = lorem
                    obj.artist_id = artist.id
                    obj.owner_id = User.query.first().id
                    db.session.add(obj)
        db.session.commit()
    print 'Done.'
    print


if __name__ == '__main__':
    add_test_users()
    add_test_articles()
    add_test_works()

