# -*- coding: utf-8 -*-
from .attachment import AttachmentMixin, Attachment


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

    def picture_url(self, default=True, category='small'):
        if self.attachments:
            pic = self.picture
            if pic:
                return pic.url(category)
        if not default or not self._DEFAULT_PIC:
            return None
        if '%s' in self._DEFAULT_PIC:
            return self._DEFAULT_PIC % category
        return self._DEFAULT_PIC
