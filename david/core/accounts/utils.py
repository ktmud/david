# -*- coding: utf-8 -*-
from flask import abort
from flask.ext.security import current_user


def require_editor(f):
    def _(*args, **kwargs):
        if current_user.has_role('editor') and not current_user.has_role('admin'):
            return abort(403)
        return f(*args, **kargs)
    return _

