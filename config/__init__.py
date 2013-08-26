# -*- coding: utf-8 -*-
from .security import *
from .database import *

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

SITE_NAME = '佟大为官网'
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
        ('/', '首页', 'home'),
        ('/admin', '登录'),
        ('javascript:void(0);', '明星', 'artist',
            [ ('/artist/tong', '佟大为'), ('/artist/guan', '关　悦'), ]
        ),
        #('http://tieba.baidu.com/f?ie=utf-8&kw=%E4%BD%9F%E5%A4%A7%E4%B8%BA', '活动'),
        ('/news/', '新闻'),
        ('/works/movie/', '作品', 'works',
            [('/works/movie/', '电影'), ('/works/tv/', '电视'), ('/works/music/', '音乐')]
        ),
        ('/magazine/', '杂志'),
        ('/photos/', '图片'),
        ('http://tieba.baidu.com/f?ie=utf-8&kw=%E4%BD%9F%E5%A4%A7%E4%B8%BA', '论坛'),
        ]

FOOTER_MENU = [
        ('/about', '关于佟大为工作室'),
        ('/contact', '联系方式'),
        ('/jobs', '加入我们')
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
