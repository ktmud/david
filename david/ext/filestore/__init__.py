# -*- coding: utf-8 -*-
"""
Store uploaded file to somewhere.
"""
import os
from flask.ext.uploads import UploadSet, secure_filename

from config import STATIC_ROOT


EXT_IMAGE = tuple('jpg jpe jpeg png gif svg bmp'.split())
EXT_AUDIO = tuple('wav mp3 aac ogg oga'.split())
EXT_VIDEO = tuple('mp4 flv mov'.split())



class FileStore(UploadSet):

    def save(self, storage, name=None):
        key = self.get_file_key(storage, name)
        path = os.path.join(self.config.destination, key)
        storage.save(path)
        return key
    
    def get_file_key(self, storage, name=None, folder=None):
        key = name or storage.filename
        key = lowercase_ext(secure_filename(key))
        if folder:
            key = os.path.join(folder, key)
        if self.exists(key):
            key = self.resolve_conflict(key)
        return key

    def exists(self, key):
        return os.path.exists(self.path(key))

    def resolve_conflict(self, key):
        name, ext = key.rsplit('.', 1)
        count = 0
        while True:
            count = count + 1
            newname = '%s_%d.%s' % (name, count, ext)
            if not self.exists(newname):
                return newname

    def path(self, key):
        return os.path.join(self.config.destination, key)

    def remove(self, key):
        return os.unlink(self.path(key))

    def url(self, key):
        return STATIC_ROOT + 'storage/' + key

    def stat(self, key):
        return os.stat(self.path(key))


def lowercase_ext(filename):
    if '.' in filename:
        main, ext = filename.rsplit('.', 1)
        return main + '.' + ext.lower()
    else:
        return filename.lower()


def addslash(url):
    if url.endswith('/'):
        return url
    return url + '/'

