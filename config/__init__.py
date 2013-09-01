# -*- coding: utf-8 -*-
from .security import *
from .database import *

from flask.ext.babel import lazy_gettext as _

DEVELOP_MODE = True
DEBUG = True

SECRET_KEY = 'keyboardcat'

HOST = 'localhost'
PORT = 19838

SENTRY_DSN = None
SENTRY_USER_ATTRS = ['name', 'email']

BABEL_ACCEPT_LANGUAGE = ['zh_CN', 'zh_TW', 'en']
BABEL_DEFAULT_LOCALE = 'zh_CN'
BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

SITE_NAME = _('Dawei Tong Official')
SITE_DOMAIN = 'tongdawei.cc'
SITE_ORIGIN = 'localhost:5000'
SITE_ROOT = 'http://' + SITE_ORIGIN + '/'
STATIC_ROOT = SITE_ROOT + 'static/'

UPLOADS_DEFAULT_DEST = '/var/uploads'
UPLOADS_DEFAULT_URL = None
#UPLOADS_DEFAULT_URL = STATIC_ROOT + '/'

QINIU_AK = ''
QINIU_SK = ''
QINIU_BUCKET = 'david'
QINIU_ROOT = 'http://%s.qiniudn.com/' % QINIU_BUCKET


SECURITY_EMAIL_SUBJECT_REGISTER = '欢迎加入%s(%s)' % (SITE_NAME, SITE_DOMAIN)
SECURITY_EMAIL_SUBJECT_PASSWORDLESS = '你在%s的登录信息' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = '你在%s的登录密码已重置' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = '你在%s的登录密码已变更' % SITE_NAME
SECURITY_EMAIL_SUBJECT_CONFIRM = '请确认你的登录邮箱(%s)' % (SITE_DOMAIN)

#TODO: move this to database or something
HEADER_MENU = [
        ('/', _('Home'), 'home', None, lambda x, req: False),
        #('/admin', _('Login')),
        ('javascript:void(0);', _('Star'), 'artist',
            [
                ('/artist/tong', _('Dawei')),
                ('/artist/guan', _('Yue')),
            ]
        ),
        #('http://tieba.baidu.com/f?ie=utf-8&kw=%E4%BD%9F%E5%A4%A7%E4%B8%BA', '活动'),
        ('/news/', _('News'), 'news', None, lambda x, req: req.path.startswith('/news/')),
        ('/gallery/photos/', _('Photos')),
        ('/works/', _('Works'), 'works',
            [
                ('/works/movie/', _('Movie')),
                ('/works/tv/', _('TV')),
                ('/works/music/', _('Music'))
            ]
        ),
        ('/gallery/magazine/', _('Magazine')),
        ('http://tieba.baidu.com/f?ie=utf-8&kw=%E4%BD%9F%E5%A4%A7%E4%B8%BA',
            _('Forum')),
        ]

FOOTER_MENU = [
        ('/about', _('About David Tong Studio')),
        ('/contact', _('Contact')),
        ('/jobs', _('Join us'))
        ]




import os
from flask.config import Config

APP_ROOT = os.path.abspath(os.path.join(__path__[0], '../'))

config = Config(APP_ROOT)

# load from environment
if 'DAVID_CONFIG_FILE' in os.environ:
    config.from_pyfile(os.environ['DAVID_CONFIG_FILE'])

# load from local config
config.from_pyfile('local_config.py', silent=True)

globals().update(config)
