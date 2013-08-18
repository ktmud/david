# -*- coding: utf-8 -*-
import os
from babel import support 

from flask.ext.babel import Babel, gettext, ngettext, lazy_gettext, _
from flask.ext.babel import get_locale
from flask import g, request
from flask import _request_ctx_stack
from flask.ext.login import current_user
from david.translations import get_translations

from david.config import BABEL_ACCEPT_LANGUAGE, BABEL_DEFAULT_LOCALE

def init_babel(app):
    babel = Babel(app)
    babel.timezoneselector(_get_timezone)
    app.before_request(_set_context_locale)

def gettext_fn_by_domain(domain):
    '''return a gettext function by domain'''
    def _(string, **variables):
        t = get_translations(get_locale(), domain=domain)
        if t is None:
            return string % variables
        return t.ugettext(string) % variables
    return _

admin_gettext = _a = gettext_fn_by_domain('admin')

def _set_context_locale():
    ctx = _request_ctx_stack.top
    if ctx is None:
        return None
    if not current_user.is_anonymous:
        locale = current_user.locale
    else:
        locale = request.accept_languages.best_match(BABEL_ACCEPT_LANGUAGE)
    if locale is None:
        locale = BABEL_DEFAULT_LOCALE
    ctx.babel_locale = locale
    # load customized translations
    ctx.babel_translations = get_translations(locale)

def _get_timezone():
    if current_user is not None:
        return current_user.timezone
