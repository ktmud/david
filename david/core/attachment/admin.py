# -*- coding: utf-8 -*-
from flask import request
from wtforms import Form, fields , validators
from david.ext.babel import lazy_gettext as _


class AttachmentForm(Form):
    fp = fields.FileField(_('Choose File'))
    desc = fields.TextAreaField(_('Description'))


class ModelAttachmented(object):

    def attachments_form(self, model):
        form = AttachmentForm()
