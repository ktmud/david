# -*- coding: utf-8 -*-
import os
from fabric.api import *
import config

env.user = 'david'
env.hosts = ['localhost']

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + '/david'
TRANSLATION_ROOT = APP_ROOT + '/translations'


REMOTE_APP_ROOT = '/srv/user/david/www/david'



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



def static():
    local('cd ./david/static && grunt build')

def pack():
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    dist = local('python setup.py --fullname', capture=True).strip()
    put('dist/%s.tar.gz' % dist, '/tmp/david_app.tar.gz')
    run('mkdir /tmp/david_app')
    with cd('/tmp/david_app'):
        run('tar zxf /tmp/david_app.tar.gz')
        run('%s/venv/bin/python setup.py install' % REMOTE_APP_ROOT)
    run('rm -rf /tmp/david_app /tmp/david_app.tar.gz')


def bootstrap():
    run('mkdir -p %s' % REMOTE_APP_ROOT)
    with cd(REMOTE_APP_ROOT):
        run('virtualenv --distribute venv')
