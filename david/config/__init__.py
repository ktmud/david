# coding: utf-8

SECRET_KEY = 'keyboardcat'
DEVELOP_MODE = False
DEBUG = False
HOST = 'localhost'
PORT = 19838

SITE_DOMAIN = 'tongdawei.cc'
SITE_ROOT = 'http://www.tongdawei.cc'
SITE_NAME = '佟大为官网'

from security import *
from database import *

SECURITY_EMAIL_SUBJECT_REGISTER = '欢迎加入%s(%s)' % (SITE_NAME, SITE_DOMAIN)
SECURITY_EMAIL_SUBJECT_PASSWORDLESS = '你在%s的登录信息' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_NOTICE = '你在%s的登录密码已重置' % SITE_NAME
SECURITY_EMAIL_SUBJECT_PASSWORD_CHANGE_NOTICE = '你在%s的登录密码已变更' % SITE_NAME
SECURITY_EMAIL_SUBJECT_CONFIRM = '请确认你的登录邮箱(%s)' % (SITE_DOMAIN)

MODULES = ['gallery', 'news']

try:
    from config import *
except Exception, e:
    pass


