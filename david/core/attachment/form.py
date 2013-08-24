# -*- coding: utf-8 -*-
import re
from wtforms import Form, fields, widgets, validators


class AttachmentForm(Form):
    pass

class AttachmentWidget(widgets.FileInput):
    pass

class AttachmentField(fields.FileField):
    widget = AttachmentWidget()


class AttachmentFieldList(fields.FieldList):
    pass



class ImageWidget(AttachmentWidget):

    validators = (validators.regexp(r'^[^/\\]\.(jpg|png|gif)$', re.IGNORECASE))

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('accept', 'image/*')
        value = field._value()
        if value:
            kwargs.setdefault('value', value)
        return widgets.HTMLString('<input %s>' % 
                widgets.html_params(name=field.name, type='file', **kwargs))



