# -*- coding: utf-8 -*-
import os
from fabric.api import *
import config

# Example usage
env.hosts = ['david@david:19848']


APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + '/david'
TRANSLATION_ROOT = APP_ROOT + '/translations'


REMOTE_APP_ROOT = '/srv/user/david/app/tongdawei.cc'



def babel():
    babel_init()
    babel_update()
    babel_compile()

def babel_extract():
    local('pybabel extract -F david/babel.cfg '
          '--msgid-bugs-address=kisdmud@gmail.com '
          '--copyright-holder="Jesse Yang" '
          '-o /tmp/messages.pot %s' % APP_ROOT)

def babel_update():
    babel_extract()
    local('pybabel update -i /tmp/messages.pot '
          '-d %s' % TRANSLATION_ROOT)

def babel_compile():
    local('pybabel compile -d %s -f --statistics' % TRANSLATION_ROOT)

def babel_init():
    langs = config.BABEL_ACCEPT_LANGUAGE
    for l in langs:
        if os.path.exists(os.path.join(TRANSLATION_ROOT, l)):
            print 'Skip existing translation dir %s' % l
            continue
        local('pybabel init -i messages.pot -d %s -l %s' % (TRANSLATION_ROOT, l))


def deploy():
    with cd(REMOTE_APP_ROOT):
        run('source venv/bin/activate && pip install -r requirements.txt')
        run('cd ./david/static && npm install && grunt build')
        run('make dpyc && sudo supervisorctl restart david')


def bootstrap():
    with cd(REMOTE_APP_ROOT):
        run('virtualenv --distribute venv')
        run('source venv/bin/activate && pip install gunicorn')
