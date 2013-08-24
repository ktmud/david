# coding: utf-8
from werkzeug.contrib.cache import SimpleCache, RedisCache

from david.config import REDIS_KEY_PREFIX
from david.lib.rc import redis_client
from .decorators import create_decorators


lc = SimpleCache(threshold=10000)

class CacheDict(dict):

    def __init__(self, props, name, lc):
        self._raw = props
        self._name = name
        self._lc = lc

    def __getitem__(self, name):
        return self._raw.get(name)

    def __setitem__(self, name, value):
        self._raw[name] = value
        self._lc.set(name, self._raw)

    def __getattr__(self, name):
        if hasattr(self, '_raw'):
            return getattr(self._raw, name)
        raise AttributeError('No such attribute: %s' % name)

    def __getstate__(self):
        return self._raw

def lcdict(item, name, lc=lc):
    return CacheDict(item, name, lc)



class StrictRedisCache(RedisCache):

    def set(self, key, value, timeout=None):
        if timeout is None:
            timeout = self.default_timeout
        dump = self.dump_object(value)
        if timeout is not None:
            self._client.setex(self.key_prefix + key, timeout, dump)
        else:
            self._client.set(self.key_prefix + key, dump)



def get_redis_cache(*args, **kwargs):
    kwargs['key_prefix'] = kwargs.get('key_prefix', REDIS_KEY_PREFIX)
    # redis cache doesn't support strict client
    kwargs['host'] = kwargs.get('host', redis_client)
    return StrictRedisCache(**kwargs)



globals().update(create_decorators(redis_client))
