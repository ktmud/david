# -*- coding: utf-8 -*-
from flask import g, request

class MenuItem(object):

    def __init__(self, path, text, name):
        self.name = name
        self.path = path
        self.text = text

    @property
    def is_current(self):
        return request.path == self.path


class Menu(object):

    def __init__(self, items=None):
        self._items = {}
        self._orders = {}
        if items is not None:
            for args in items:
                self.add_item(*args)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self.items()

    def __contains__(self, item):
        return item in self._items

    def add_item(self, path, text, name=None, order=None):
        if name is None:
            name = path.replace('/', '_').strip('_')
        if order is None:
            order = len(self._items) * 10
        self._items[name] = (path, text)
        self._orders[name] = order
        return self.get_item(name)

    def get_item(self, name):
        if name in self:
            val = self._items[name]
            return MenuItem(val[0], val[1], name)

    def change_order(name, order):
        self._orders[name] = order

    def items(self):
        ret = []
        for k, v in self._items.items():
            ret.append(MenuItem(v[0], v[1], k))
        orders = self._orders
        return sorted(ret, key=lambda x: orders[x.name])
