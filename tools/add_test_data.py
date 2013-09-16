# -*- coding: utf-8 -*-
import os
import datetime
import random

from david.core.db import db
from david.core.accounts import user_datastore, User
from david.core.article import CATS
from app import app

from flask.ext.security.utils import encrypt_password

TOOLS_FOLER = os.path.dirname(__file__)

lorem = open(TOOLS_FOLER + '/data/loremipsum.txt').read()

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

        for cat, model in CATS.items():
            for i in range(40):
                article = model()
                article.cat = cat
                article.title = '%s 测试文章 - %s' % (article.cat_name, i + 1)
                article.content = unicode(lorem)[:random.randint(10, 600)]
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

        artist1 = Artist()
        artist1.name = '佟大为'
        artist1.uid = 'tong'

        artist2 = Artist()
        artist2.name = '关悦'
        artist2.uid = 'guan'

        db.session.add_all([artist1, artist2])
        db.session.commit()

        artist1, artist2 = Artist.query.all()
        artist1.desc = artist2.desc = lorem

        one_year = datetime.timedelta(days=366)
        one_month = datetime.timedelta(days=30)

        for cat, model in cat2type.items():
            pubdate = datetime.date.today() + one_year
            for i in range(20):
                pubdate -= one_year
                for i in range(7):
                    pubdate -= one_month
                    obj = Work()
                    obj.title = '%s作品%s' % (model.__name__, i + 1)
                    obj.cat = cat
                    obj.pubdate = pubdate
                    obj.desc = lorem
                    obj.artist_id = artist1.id if i % 2 else artist2.id
                    obj.owner_id = User.query.first().id
                    db.session.add(obj)
        db.session.commit()
    print 'Done.'
    print

def add_test_events():
    print 'Creating Events...'

    from david.modules.event.model import Event

    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        for i in range(20):
            obj = Event()
            obj.title = 'test event %s' % (i + 1)
            obj.content = lorem
            obj.link = 'http://www.example.com/'
            db.session.add(obj)
        db.session.commit()
    print 'Done.'
    print

def add_test_pages():
    print 'Creating pages...'

    from david.modules.pages.model import Page

    with app.test_client() as c:
        c.get('/')

        db.session.add(Page(title='About', uid='about',
            content='<h2>About us</h2>'))
        db.session.add(Page(title='English', uid='en',
            content='<h2>About us</h2>'))
        db.session.add(Page(title='Contact', uid='contact',
            content='<h2>Contact us</h2>'))
        db.session.commit()
    print 'Done.'
    print

if __name__ == '__main__':
    add_test_users()
    add_test_articles()
    add_test_works()
    add_test_pages()
    add_test_events()

