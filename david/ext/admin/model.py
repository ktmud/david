# coding: utf-8
from david.core.db import db, func
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



class CatFiltered(object):
    """ This view's get_list will be filter by model's cat_id attribute """

    def get_query(self):
        return self.session.query(self.model)\
                           .filter(self.model.cat_id == self.model._cat_id)

    def get_count_query(self):
        return self.session.query(func.count('*'))\
                           .select_from(self.model)\
                           .filter(self.model.cat_id == self.model._cat_id)



def bind_hidden_field(form, name, value):
    field = fields.HiddenField()
    field = field.bind(form=form, name=name)
    field.data = value
    form._fields[name] = field

class ModelAdmin(Roled, ModelView):

    def __init__(self, model, name=None, endpoint=None, url=None, **kwargs):
        if url is None:
            url = model.__name__.lower().replace('view', '')
        if endpoint is None and url:
            endpoint = url + '.admin'
        super(ModelAdmin, self).__init__(model, db.session, name=name,
                endpoint=endpoint, url=url, **kwargs)

    def create_model(self, form):
        # override the create to add `cat_id` and `owner_id` field field value
        if hasattr(self.model, 'cat_id') and isinstance(self.model.cat_id, int):
            bind_hidden_field(form, '_cat_id', self.model.cat_id)
        if hasattr(self.model, 'owner_id'):
            bind_hidden_field(form, 'owner_id', current_user.id)
        return super(ModelAdmin, self).create_model(form)


    def get_instance(self, i):
        try:
            return self.model.objects.get(id=i)
        except self.model.DoesNotExist:
            flash(_("Item not found %(i)s", i=i), "error")

    @action('export_to_json', _('Export as json'))
    def export_to_json(self, ids):
        qs = self.model.objects(id__in=ids)

        return Response(
            qs.to_json(),
            mimetype="text/json",
            headers={
                "Content-Disposition":
                "attachment;filename=%s.json" % self.model.__name__.lower()
            }
        )

    @action('export_to_csv', _('Export as csv'))
    def export_to_csv(self, ids):
        qs = json.loads(self.model.objects(id__in=ids).to_json())

        def generate():
            yield ','.join(list(qs[0].keys())) + '\n'
            for item in qs:
                yield ','.join([str(i) for i in list(item.values())]) + '\n'

        return Response(
            generate(),
            mimetype="text/csv",
            headers={
                "Content-Disposition":
                "attachment;filename=%s.csv" % self.model.__name__.lower()
            }
        )



class AdminIndex(Roled, AdminIndexView):
    pass


