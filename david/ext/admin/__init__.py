# coding: utf-8
from flask.ext.admin import Admin
from flask.ext.admin.base import MenuLink as BaseMenuLink
from flask import Blueprint, abort

from david.ext.babel import lazy_gettext

from config import SITE_ROOT
from .model import Roled, ModelAdmin, AdminIndex, Proped


translations = {
    'Article': lazy_gettext('Article')
}

def _(string):
    if string in translations:
        return translations[string]
    return lazy_gettext(string)



class MenuLink(BaseMenuLink):

    def __init__(self, name, url=None, endpoint=None, target='_self'):
        self.name = name
        self.url = url
        self.endpoint = endpoint
        self.target = target



admin = Admin(index_view=AdminIndex(name=_('Home')))


admin.add_link(MenuLink(_('Visit Site'), url=SITE_ROOT, target='_blank'))
