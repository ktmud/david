# -*- coding: utf-8 -*-
from david.core.db import db
from david.core.accounts import user_datastore, User
from david.core.article import CATS
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

def add_test_articles():
    with app.test_client() as c:
        # send a fake request, so `current_app` can be the app
        rv = c.get('/')

        for cat, model in CATS.items():
            for i in range(5):
                article = model()
                article._cat_id = article.cat_id
                article.title = '%s 测试文章 - %s' % (article.cat_name, i + 1)
                article.content = '这段文字很难搞呢'
                article.owner_id = User.query.first().id
                db.session.add(article)
        db.session.commit()


if __name__ == '__main__':
    add_test_users()
    add_test_articles()

