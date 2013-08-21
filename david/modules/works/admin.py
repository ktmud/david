# coding: utf-8
from david.ext.admin import ModelAdmin
from david.ext.babel import lazy_gettext

from .model import Work

class WorksAdmin(ModelAdmin):
    pass

views = [
  WorksAdmin(Work, name=lazy_gettext('Works'))
]
