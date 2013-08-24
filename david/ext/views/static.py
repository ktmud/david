# -*- coding: utf-8 -*-
import os
from flask import url_for, current_app

from david.lib.cache import lc
from david.config import STATIC_ROOT, DEBUG

def static_url(filename):
    if DEBUG:
        return url_for('static', filename=filename)
    return config['STATIC_ROOT'] + _hashed_filename(filename)


def urlmap(*filenames):
    ret = {}
    for f in filenames:
        fname = f
        if not f.endswith('.js') and not f.endswith('.css'):
            fname = 'js/' + f + '.js'
        ret[f] = static_url(fname)
    return ret

def inline_static(filename):
    pass


hashmap = {}

def _hashed_filename(filename):
    if filename in hashmap:
        return
    return os.path.join('/', filename)

def _load_hashmap():
    fp = os.path.join(current_app.static_folder, 'hash.json')
    hashmap = json.load(fp)

if not DEBUG:
    _load_hashmap()

