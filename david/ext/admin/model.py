# coding: utf-8
from flask.ext.admin import AdminIndexView
from flask.ext.admin.contrib.mongoengine import ModelView
from flask.ext.admin.actions import action
from flask.ext.security import current_user
from flask.ext.security.utils import url_for_security
from flask import redirect, flash, url_for, Response



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


class ModelAdmin(Roled, ModelView):

    def get_instance(self, i):
        try:
            return self.model.objects.get(id=i)
        except self.model.DoesNotExist:
            flash(gettext("Item not found %(i)s", i=i), "error")

    @action('export_to_json', 'Export as json')
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

    @action('export_to_csv', 'Export as csv')
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


