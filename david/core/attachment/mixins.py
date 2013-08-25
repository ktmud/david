# -*- coding: utf-8 -*-
from david.lib.mixins.props import PropsMixin, PropsItem

from .attachment import Attachment
from .form import AttachmentFieldList


def _get_ids(items):
    return [(i.id if hasattr(i, 'id') else i) for i in items]


class AttachmentMixin(PropsMixin):
    """ Mixin for a db.Model """

    attachments = PropsItem('attachments', [])

    @property
    def attachment_items(self):
        return filter(None, Attachment.gets(self.attachments))

    @property
    def attachments_info(self):
        return [item.serialize() for item in self.attachment_items]

    def add_attachments(self, items):
        items = _get_ids(items)
        self.attachments = list(set(self.attachments + items))

    def remove_attachments(self, items):
        items = _get_ids(items)
        self.attachments = [i for i in self.attachments if i not in items]

    @property
    def _attachment_field(self, name):
        return AttachmentField(name)

    def attachment_fields(self, label=None, name='attachments',
                          max_entries=None):
        if label is None:
            label = _('Attachments')

        attached = [x for x in self.attachment_items]

        return AttachmentFieldList(
                    self._attachment_field(name),
                    label=label,
                    min_entries=1,
                    max_entries=max_entries,
                    default=attached)


        
class PictureMixin(AttachmentMixin):

    _DEFAULT_PIC = None

    @property
    def picture(self):
        if hasattr(self, 'attachments'):
            for key in self.attachments:
                a = Attachment.get(key)
                if a and a.is_image:
                    return a
        if hasattr(self, 'picture_id'):
            return Attachment.get(self.picture_id)

    def picture_url(self, category='small', default=True):
        pic = self.picture
        if pic:
            return pic.url(category)
        if not default:
            return None
        dft = self._DEFAULT_PIC.replace('%25s', '%s', 1)
        if '%s' in dft:
            return dft % category
        return self._DEFAULT_PIC
