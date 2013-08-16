# -*- coding: utf-8 -*-
from flask.ext.login import current_user
from flask.ext.babelex import Babel, gettext, ngettext, lazy_gettext
from flask.ext.admin.babel import domain
from flask import g, request

from david.config import BABEL_ACCEPT_LANGUAGE 

babel = Babel()

#babel.locale_selector_func = None
#babel.timezone_selector_func = None

@babel.localeselector
def get_locale():
    if current_user is not None:
        return current_user.locale
    return request.accept_languages.best_match(BABEL_ACCEPT_LANGUAGE)

@babel.timezoneselector
def get_timezone():
    if current_user is not None:
        return current_user.timezone
