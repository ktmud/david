# -*- coding: utf-8 -*-
import os
from flask.ext.admin import translations as admin_translations
from babel.support import Translations

root_dirname = os.path.dirname(os.path.abspath(__file__))
admin_dir = admin_translations.__path__[0]
cached_translations = {}

AVAILABLE_DOMAINS = {
    'admin': (admin_dir, 'admin'),
    'messages': (root_dirname, 'messages')
}

def get_translations(locale, domain='messages'):
    locale = str(locale)
    # to unify locale names
    if locale.startswith('zh_hans'):
        locale = 'zh_CN'
    elif locale.startswith('zh_hant'):
        locale = 'zh_TW'

    ident = locale + '/' + domain

    if ident in cached_translations:
        return cached_translations[ident]

    dirname, domain = AVAILABLE_DOMAINS[domain]
    translations = Translations.load(dirname, locale, domain=domain)
    cached_translations[ident] = translations
    return translations


__all__ = [get_translations]
