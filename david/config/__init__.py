# -*- coding: utf-8 -*-
DEVELOP_MODE = False
DEBUG = False
DEBUG_TB_INTERCEPT_REDIRECTS = True

SECRET_KEY = 'keyboardcat'

HOST = 'localhost'
PORT = 19838
SITE_DOMAIN = 'tongdawei.cc'
SITE_ROOT = 'http://www.tongdawei.cc'
STATIC_ROOT = '//img.tongdawei.cc' # cdn path
SITE_NAME = '佟大为官网'

from security import *
from database import *

SECURITY_EMAIL_SUBJECT_REGISTER = '欢迎加入%s(%s)' % (SITE_NAME, SITE_DOMAIN)
SECURITY_EMAIL_SUBJECT_PASSWORDLESS = '你在%s的登录信息' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = '你在%s的登录密码已重置' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = '你在%s的登录密码已变更' % SITE_NAME
SECURITY_EMAIL_SUBJECT_CONFIRM = '请确认你的登录邮箱(%s)' % (SITE_DOMAIN)

MODULES = ['gallery', 'news']

#TODO: move this to database or something
FOOTER_MENU = [
  ('/about', u'关于佟大为官网'),
  ('/contact', u'联系方式'),
  ('/jobs', u'加入我们')
]

try:
    from config import *
except Exception, e:
    pass

