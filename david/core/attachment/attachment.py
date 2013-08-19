# -*- coding: utf-8 -*-
from david.core.db import db
from david.core.mapper import get_obj
from david.lib.mixins.props import PropsMixin, PropsItem
from david.ext.filestore import FileStore, EXT_IMAGES


default_uploader = FileStore('default')



class Attachment(PropsMixin):

    manager = default_uploader

    key = PropsItem('key')
    size = PropsItem('size')
    etag = PropsItem('etag')
    mime = PropsItem('mime')
    title = PropsItem('title', '')
    desc = PropsItem('desc', '')
    owner_id = PropsItem('owner_id')
    owner_kind = PropsItem('owner_kind')

    _url = PropsItem('url')
    _path = PropsItem('path')

    def __init__(self, id):
        self.id = id

    def url(self):
        return self._url or self.manager.url(self.key)

    def path(self):
        return self._path or self.manager.path(self.key)

    def owner(self):
        return get_obj(self.owner_kind, self.owner_id)

    @property
    def is_image(self):
        basename, ext = self.key.rsplit('.', 1)
        return ext in EXT_IMAGES

    def info(self):
        return dict(key=self.key, url=self.url(),
                is_image=self.is_image,
                size=self.size, mime=self.mime,
                etag=self.etag)


    @classmethod
    def get(cls, id):
        self = cls(id)
        if not self.key:
            return None
        return self

    @classmethod
    def gets(cls, ids):
        return [cls.get(i) for i in ids]

    @classmethod
    def add(cls, filestore=None, name=None, **props):
        key = self.manager.save(filestore, name)
        props['key'] = key
        self = cls(key)
        self.update_props(**props)
        return self


class AttachmentMixin(PropsMixin):

    attachments = PropsItem('attachments', [])

    @property
    def attachment_objs(self):
        return filter(None, [Attachment.get(i) for i in self.attachments])

