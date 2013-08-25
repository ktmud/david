# coding: utf-8
from flask import json
from david.core.db import db, func, sql
from david.ext.babel import lazy_gettext as _

from flask.ext.admin import AdminIndexView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.actions import action
from flask.ext.security import current_user
from flask.ext.security.utils import url_for_security
from flask import redirect, flash, url_for, Response

from wtforms import fields, validators


# to admin models with PropsMixin
class Proped(object):

    extra_props = ()

    def scaffold_form(self):
        form_class = super(Proped, self).scaffold_form()
        for e in self.extra_props:
            if isinstance(e, str):
                name = e
            else:
                name = e[0]
                field = e[1]
            label = self.column_labels.get(name, e.capitalize())
            # default extra props to a text fields
            if not field:
                field = fields.TextField(label)
            form_class[name] = field
        return form_class



class Roled(object):

    roles_accepted = ['admin', 'editor']

    def is_accessible(self):

        roles = getattr(self, 'roles_accepted', None)
        if not roles: return True
        for r in roles:
            if current_user.has_role(r):
                return True
        return False

    def _handle_view(self, name, *args, **kwargs):
        if not current_user.is_authenticated():
            return redirect(url_for_security('login', next="/admin"))
        if not self.is_accessible():
            return self.render("admin/denied.html")



def bind_hidden_field(form, name, value):
    field = fields.HiddenField()
    field = field.bind(form=form, name=name)
    field.data = value
    form._fields[name] = field


class ModelAdmin(Proped, Roled, ModelView):

    def __init__(self, model, name=None, endpoint=None, url=None, **kwargs):
        if url is None:
            url = model.__name__.lower().replace('view', '')
        if endpoint is None and url:
            endpoint = url + '.admin'
        super(ModelAdmin, self).__init__(model, db.session, name=name,
                endpoint=endpoint, url=url, **kwargs)

    
    richtext_columns = ('desc', 'content')


    def has_attachments(self):
        return hasattr(self.model, 'attachments')

    def get_query(self):
        return self.model.query
        #query = self.session.query(self.model)
        #if hasattr(self.model, 'cat_id'):
            #query = query.filter(self.model.cat_id == self.model.cat)
        #return query

    def get_count_query(self):
        model = self.model
        query = self.session.query(func.count('*')).select_from(model)
        if hasattr(model, 'cat') and isinstance(model.cat_id, int):
            query = query.filter(model.cat_id == model.cat)
        return query

    def create_model(self, form):
        # override the create to add `cat_id` and `owner_id` field field value
        if hasattr(self.model, 'cat_id') and isinstance(self.model.cat_id, int):
            bind_hidden_field(form, 'cat', self.model.cat_id)
        if hasattr(self.model, 'owner_id'):
            bind_hidden_field(form, 'owner_id', current_user.id)
        return super(ModelAdmin, self).create_model(form)



class AdminIndex(Roled, AdminIndexView):
    pass


