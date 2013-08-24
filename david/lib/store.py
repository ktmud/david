# -*- coding: utf-8 -*-
from .cache import get_redis_cache

redis_store = get_redis_cache(key_prefix='david.store/')
redis_store.default_timeout = None
