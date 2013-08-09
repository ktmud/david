# coding: utf-8

SECRET_KEY = 'keyboardcat'
DEVELOP_MODE = False
DEBUG = False
HOST = 'localhost'
PORT = 19838
SITE_ROOT = 'http://www.tongdawei.cc'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

try:
    from local_config import *
except Exception, e:
    pass


