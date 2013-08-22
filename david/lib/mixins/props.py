# -*- coding: utf-8 -*-

"""
提供props常见操作支持，需要对应的类支持get_uuid, 目前是IData
"""

import types
import datetime
import copy

from david.lib.cache import get_redis_cache, lc


mc = get_redis_cache(key_prefix='david.props/')
mc.default_timeout = 0

class PropsMixin(object):

    def get_uuid(self):
        if not self.id:
            raise RuntimeError('PropsMixin must have an id')
        return '%s:%s' % (self.__tablename__, self.id)

    @property
    def _props_name(self):
        return '__%s/props_cached' % self.get_uuid()

    @property
    def _props_db_key(self):
        return '%s/props' % self.get_uuid()

    def _get_props(self):
        lc_name = self._props_name
        props = lc.get(lc_name)
        if props is None:
            props = mc.get(self._props_db_key) or {}
            lc.set(lc_name, props)
        return props

    def _set_props(self, props):
        mc.set(self._props_db_key, props)
        lc.delete(self._props_name)

    def _destory_props(self):
        mc.delete(self._props_db_key)
        lc.delete(self._props_name)

    get_props = _get_props
    set_props = _set_props

    props = property(_get_props, _set_props)

    def set_props_item(self, key, value):
        props = self.props
        props[key] = value
        self.props = props

    def delete_props_item(self, key):
        props = self.props
        props.pop(key, None)
        self.props = props

    def get_props_item(self, key, default=None):
        return self.props.get(key, default)

    def update_props(self, **data):
        props = self.props
        props.update(data)
        self.props = props


class PropsItem(object):
    def __init__(self, name, default=None, output_filter=None):
        self.name = name
        self.default = default
        self.output_filter = output_filter
        self.mutable_default_value = isinstance(
                self.default,
                (
                    set,
                    bytearray,
                    types.DictType,
                    types.ListType,
                    )
                )

    def __get__(self, obj, objtype):
        if obj is None:
            return
        r = obj.get_props_item(self.name, None)
        if r is None:
            if self.mutable_default_value:
                return copy.deepcopy(self.default)
            return self.default
        elif self.output_filter:
            return self.output_filter(r)
        else:
            return r

    def __set__(self, obj, value):
        obj.set_props_item(self.name, value)

    def __delete__(self, obj):
        obj.delete_props_item(self.name)


datetime_outputfilter = lambda v: datetime.datetime.strptime(v, '%Y-%m-%d %H:%M:%S') if v else None
date_outputfilter = lambda v: datetime.datetime.strptime(v, '%Y-%m-%d').date() if v else None


class DatetimePropsItem(PropsItem):
    def __init__(self, name, default=None):
        super(DatetimePropsItem, self).__init__(
            name, default, datetime_outputfilter)


class DatePropsItem(PropsItem):
    def __init__(self, name, default=None):
        super(DatePropsItem, self).__init__(name, default, date_outputfilter)
