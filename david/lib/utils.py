# -*- coding: utf-8 -*-
from jinja2.filters import do_truncate as truncate, do_striptags as striptags


class LazyGetter(object):

    def __init__(self, fn):
        self.fn = fn

    def __get__(self, obj, typeclass):
        return self.fn()

    def __getattr__(self, name):
        return getattr(self.fn(), name)

    def __iter__(self):
        return self.fn().__iter__()


def lazyget(fn):
    return LazyGetter(fn)
