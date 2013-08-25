# -*- coding: utf-8 -*-
from flask import abort

from david.core.db import db, SerializeMixin
from david.core.mapper import get_obj
from david.lib.mixins.props import PropsMixin, PropsItem
from david.ext.filestore import FileStore, EXT_IMAGES
from david.ext.babel import lazy_gettext as _



default_uploader = FileStore('default')



class Attachment(PropsMixin, SerializeMixin):

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

    def get_uuid(self):
        return 'attachment:%s' % self.id

    def url(self, category='default', user=None):
        return self._url or self.manager.url(self.key, category=category,
                user=user)

    def path(self):
        return self._path or self.manager.path(self.key)

    @property
    def owner(self):
        return get_obj(self.owner_kind, self.owner_id)

    @property
    def thumb_url(self):
        return self.url('thumb') if self.is_image else ext_image_url(self.file_ext)

    @property
    def file_ext(self):
        basename, ext = self.key.rsplit('.', 1)
        return ext

    @property
    def is_image(self):
        return self.file_ext in EXT_IMAGES

    def serialize(self):
        return dict(
                id=self.id,
                title=self.title or self.key,
                desc=self.desc,
                key=self.key, url=self.url(),
                thumb_url=self.thumb_url,
                is_image=self.is_image,
                size=self.size, mime=self.mime,
                etag=self.etag)


    @classmethod
    def get(cls, id):
        self = cls(id)
        if not self.key:
            return None
        subclass = self.props.get('_subclass')
        if subclass and subclass in attachment_subclasses:
            self.manager = attachment_subclasses[subclass].manager
        return self
    
    @classmethod
    def get_or_404(cls, id):
        item = cls.get(id)
        if item is None:
            return abort(404)
        return item

    @classmethod
    def gets(cls, ids):
        return [cls.get(i) for i in ids]

    @classmethod
    def add(cls, filestore=None, name=None, **props):
        key = cls.manager.save(filestore, name)
        props['key'] = key
        if cls is not Attachment:
            props['_subclass'] = cls.__name__
        self = cls(key)
        self.update_props(**props)
        owner = self.owner
        if owner:
            owner.add_attachments([self.id])
        return self

    def remove(self, clean=False):
        owner = self.owner
        if owner:
            owner.remove_attachments([self.id])
        if clean:
            self.manager.remove(self.key)



attachment_subclasses = {}

def add_subclass(cls):
    attachment_subclasses[cls.__name__] = cls

def ext_image_url(ext):
    pass
