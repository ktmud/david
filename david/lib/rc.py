# -*- coding: utf-8 -*-
import redis
from config import REDIS_SERVER

redis_client =  redis.StrictRedis(**REDIS_SERVER)
