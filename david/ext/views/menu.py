# -*- coding: utf-8 -*-
from flask import g, request

class MenuItem(object):

    def __init__(self, path, text, name, submenu=[], current_func=None):
        self.name = name
        self.path = path
        self.text = text
        self._sub = submenu
        self._current_func = current_func

    @property
    def has_submenu(self):
        return self._sub and len(self._sub) > 1

    @property
    def submenu(self):
        return Menu(self._sub)


    @property
    def is_current(self):
        if self._current_func:
            return self._current_func(self, request)
        return request.path == self.path


class Menu(object):

    def __init__(self, items=None, submenu={}):
        self._items = {}
        self._orders = {}
        self._funcs = {}
        self._subs = submenu
        if items is not None:
            for args in items:
                self.add_item(*args)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self.items()

    def __contains__(self, item):
        return item in self._items

    def add_item(self, path, text, name=None, submenu=None, current_func=None, order=None):
        if name is None:
            name = path.replace('/', '_').strip('_')
        if order is None:
            order = len(self._items) * 10
        self._items[name] = (path, text)
        self._orders[name] = order
        self._funcs[name] = current_func
        if submenu is not None:
            self._subs[name] = submenu
        return self.get_item(name)

    def get_item(self, name):
        if name in self:
            val = self._items[name]
            func = self._funcs[name]
            sub = self._subs.get(name)
            return MenuItem(val[0], val[1], name, sub, func)

    def change_order(name, order):
        self._orders[name] = order

    def items(self):
        ret = []
        for k in self._items:
            ret.append(self.get_item(k))
        orders = self._orders
        return sorted(ret, key=lambda x: orders[x.name])
