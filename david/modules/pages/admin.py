# -*- coding: utf-8 -*-
from david.ext.admin import ModelAdmin
from david.ext.babel import lazy_gettext as _

from .model import Page
from .homepage import homepage_admin

class PagesAdmin(ModelAdmin):
    column_labels = dict(
            title=_('Title'),
            id=_('ID'),
            uid=_('Slug'),
            content=_('Content'),
        )
    column_list = ('id', 'title', 'uid')
    form_widget_args = {
        'summary': dict(rows='8')
    }



views = [
  (PagesAdmin(Page, name=_('Pages')), 90),
  (homepage_admin, 5),
]
