# -*- coding: utf-8 -*-
from .security import *
from .database import *

DEVELOP_MODE = False
DEBUG = False
DEBUG_TB_INTERCEPT_REDIRECTS = False

SECRET_KEY = 'keyboardcat'

HOST = 'localhost'
PORT = 19838


BABEL_ACCEPT_LANGUAGE = ['zh_CN', 'zh_TW', 'en']
BABEL_DEFAULT_LOCALE = 'zh_CN'
BABEL_DEFAULT_TIMEZONE = 'Asia/Shanghai'

SITE_DOMAIN = 'tongdawei.cc'
SITE_ROOT = 'http://www.tongdawei.cc'
STATIC_ROOT = '//img.tongdawei.cc' # cdn path
SITE_NAME = '佟大为官网'

SECURITY_EMAIL_SUBJECT_REGISTER = '欢迎加入%s(%s)' % (SITE_NAME, SITE_DOMAIN)
SECURITY_EMAIL_SUBJECT_PASSWORDLESS = '你在%s的登录信息' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = '你在%s的登录密码已重置' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = '你在%s的登录密码已变更' % SITE_NAME
SECURITY_EMAIL_SUBJECT_CONFIRM = '请确认你的登录邮箱(%s)' % (SITE_DOMAIN)

#TODO: move this to database or something
HEADER_MENU = [
    ('/', '首页'),
    ('/star', '明星'),
    #('http://tieba.baidu.com/f?ie=utf-8&kw=%E4%BD%9F%E5%A4%A7%E4%B8%BA', '活动'),
    ('/news/', '新闻'),
    ('/works/', '作品'),
    ('/magazine/', '杂志'),
    ('/photos/', '图片'),
    ('http://tieba.baidu.com/f?ie=utf-8&kw=%E4%BD%9F%E5%A4%A7%E4%B8%BA', '论坛'),
]
FOOTER_MENU = [
    ('/about', '关于佟大为工作室'),
    ('/contact', '联系方式'),
    ('/jobs', '加入我们')
]


# import local config
try:
    from config import *
except Exception, e:
    pass
