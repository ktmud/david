# -*- coding: utf-8 -*-
import os
from flask import url_for, current_app, json

from david.lib.cache import lc
from config import APP_ROOT, STATIC_ROOT, DEBUG, SITE_ROOT


class LazyStatic(object):
    def __init__(self, path):
        self.path = path

    def __get__(self, obj, type):
        return static_url(self.path)


def lazy_static_url(filename):
    return LazyStatic(filename)



def static_url(filename):
    if DEBUG:
        return url_for('static', filename=filename)
    return STATIC_ROOT + _hashed_filename(filename)

def admin_static_url(filename):
    return SITE_ROOT + url_for('admin.static', filename=filename).replace('/', '', 1)

def urlmap(*filenames):
    ret = {}
    for f in filenames:
        fname = f
        if not f.endswith('.js') and not f.endswith('.css'):
            fname = 'js/' + f + '.js'
        ret[f] = static_url(fname)
    return ret

def _hashed_filename(filename):
    if filename in hashmap:
        if '.' in filename:
            basename, ext = filename.rsplit('.', 1)
            return '%s_%s.%s' % (basename, hashmap[filename], ext)
        return filename + '_' + hashmap[filename]
    return filename


def inline_static(filename):
    pass


STATIC_HASH_JSON = os.path.join(APP_ROOT, 'david/static/dist/hash.json')

hashmap = {}

def load_hashmap():
    hashmap.update(json.load(open(STATIC_HASH_JSON)))


if not DEBUG:
    load_hashmap()
