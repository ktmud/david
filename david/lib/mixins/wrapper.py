# -*- coding: utf-8 -*-

"""
"""

import types

# 使用该WrapperMixin
#   self._impl=
#   ...


class WrapperMixin(object):
    # stub for unpickle, or fail
    _impl = None

    def __init__(self, impl):
        self._impl = impl

    def __getattr__(self, attr):
        if hasattr(self._impl, attr):
            attr_value = getattr(self._impl, attr)
            if isinstance(attr_value, types.MethodType):
                def callable(*args, **kwargs):
                    return attr_value(*args, **kwargs)
                return callable
            else:
                return attr_value
        else:
            raise AttributeError("%s _impl: %s has not attribute %s" %
                    (self.__class__.__name__, self._impl, attr))

    def __delattr__(self, name):
        try:
            super(WrapperMixin, self).__delattr__(name)
        except AttributeError:
            self._impl.__delattr__(name)

    def __setattr__(self, name, value):
        if hasattr(self, name):
            object.__setattr__(self, name, value)
        elif name != "_impl" and hasattr(self._impl, name):
            self._impl.__setattr__(name, value)
        else:
            self.__dict__[name] = value

    def __nonzero__(self):
        return bool(self._impl)
