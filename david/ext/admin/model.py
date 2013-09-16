# coding: utf-8
from flask import json, request, redirect
from david.core.db import db, func, sql
from david.ext.babel import gettext, lazy_gettext as _
from david.lib.store import redis_store as rs

from flask.ext.admin import AdminIndexView, expose, BaseView
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.actions import action
from flask.ext.security import current_user
from flask.ext.security.utils import url_for_security
from flask.ext.admin.helpers import get_form_data, validate_form_on_submit

from flask import redirect, flash, url_for, Response

from wtforms import fields, validators



__all__ = ['Roled', 'ModelAdmin', 'AdminIndex', 'Proped', 'DBKeyAdminView']



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
            return redirect(url_for_security('login', next=url_for('admin.index')))
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

    column_default_sort = ('id', True)


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


    @expose('/new/', methods=('GET', 'POST'))
    def create_view(self):
        """
            Create model view
        """
        return_url = request.args.get('url') or url_for('.index_view')

        if not self.can_create:
            return redirect(return_url)

        form = self.create_form()

        if validate_form_on_submit(form):
            if self.create_model(form):
                if '_add_another' in request.form:
                    flash(gettext('Creating succeed.'))
                    return redirect(url_for('.create_view', url=return_url))
                if self.has_attachments:
                    return redirect(url_for('.edit_view', url=return_url))
                return redirect(return_url)

        return self.render(self.create_template,
                           form=form,
                           form_widget_args=self.form_widget_args,
                           return_url=return_url)



class AdminIndex(Roled, AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')



class DBKeyAdminView(Roled, BaseView):
    def __init__(self, *args, **kwargs):
        super(DBKeyAdminView, self).__init__(*args, **kwargs)
        self.db_keys = ()
        self.key_labels = {}
        self.help_text = {}

    @expose('/', methods=['POST', 'GET'])
    def index(self):
        labels = self.key_labels
        dbkeys = self.db_keys
        helptext = self.help_text
        vals = dict(zip(dbkeys, rs.get_many(*dbkeys)))
        if request.method == 'POST':
            self.update_keys(request.form)
            return redirect(url_for('.index'))
        return self.render('admin/dbkey/edit.html', labels=labels,
                            dbkeys=dbkeys, vals=vals, helptext=helptext)
    
    def update_keys(self, form):
        for k,v in form.items():
            if k in self.db_keys:
                rs.set(k, v)

