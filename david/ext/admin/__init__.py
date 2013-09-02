# coding: utf-8
from flask import url_for
from flask.ext.admin import Admin
from flask.ext.admin.base import MenuLink as BaseMenuLink
from flask import Blueprint, abort

from david.ext.babel import lazy_gettext

from config import SITE_ROOT
from .model import *


translations = {}

def _(string):
    if string in translations:
        return translations[string]
    ret = translations[string] = lazy_gettext(string)
    return ret



class MenuLink(BaseMenuLink):

    def __init__(self, name, url=None, endpoint=None, target='_self'):
        self.name = name
        self.url = url
        self.endpoint = endpoint
        self.target = target



admin = Admin(index_view=AdminIndex(name=_('Home'), url='/dad'))


admin.add_link(MenuLink(_('Visit Site'), url=SITE_ROOT, target='_blank'))
admin.add_link(MenuLink(_('Logout'), endpoint='security.logout'))
