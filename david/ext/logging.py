# coding: utf-8
from __future__ import absolute_import

from logging.config import dictConfig
from raven.contrib.flask import Sentry

from config import SENTRY_DSN


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
          'simple': {
            'format': '%(message)s',
            'datefmt': '',
          },
          'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%Y-%d-%d %H:%M:%S',
          },
        },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
            },
        'simple': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            },
        #'file': {
            #'level': 'DEBUG',
            #'class': 'logging.StreamHandler',
            #'formatter': 'file',
            #},
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.handlers.logging.SentryHandler',
            'dsn': SENTRY_DSN,
            },
        },
}

DEFAULT_LOGGERS = ['console']


if SENTRY_DSN:
    sentry = Sentry()
    DEFAULT_LOGGERS.append('sentry')
else:
    sentry = None


LOGGING_CONFIG['loggers'] = {
    '': {
        'handlers': DEFAULT_LOGGERS,
        'level': 'DEBUG',
        'propagate': False,
        },
    'werkzeug': {
        'handlers': ['simple'],
        'propagate': False,
        },
    'david': {
        'level': 'DEBUG',
        'propagate': True,
        },
}


def setup_logging(app):
    if sentry:
        sentry.init_app(app)
    dictConfig(LOGGING_CONFIG)

