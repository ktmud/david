# coding: utf-8
from werkzeug.contrib.cache import SimpleCache, RedisCache

from david.config import REDIS_SERVER, REDIS_KEY_PREFIX

from .decorators import create_decorators


lc = SimpleCache(threshold=10000)
redisc = RedisCache(key_prefix=REDIS_KEY_PREFIX, **REDIS_SERVER)

class CacheDict(dict):

    def __init__(props, name, lc):
        self._raw = props
        self._name = name
        self._lc = lc

    def __getitem__(self, name):
        return self._raw.get(name)

    def __setitem__(self, name, value):
        self._raw[name] = value
        self._lc.set(name, self._raw)

    def __getattr__(self, name):
        return getattr(self._raw, name)

def lcdict(item, name, lc=lc):
    return LcDict(item, name, lc)




globals().update(create_decorators(redisc))
