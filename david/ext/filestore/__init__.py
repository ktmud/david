# -*- coding: utf-8 -*-
"""
Store uploaded file to somewhere.
"""
import os
from flask.ext.uploads import UploadSet, secure_filename, IMAGES as EXT_IMAGES

class FileStore(UploadSet):

    def save(self, storage, name=None):
        key = self.get_file_key(storage, name)
        storage.save(target)
    
    def get_file_key(self, storage, name=None, folder=None):
        key = name or storage.filename
        key = lowercase_ext(secure_filename(key))
        if folder:
            key = os.path.join(folder, key)
        if self.exists(key):
            key = self.resolve_conflict(key)
        return key

    def exists(self, key):
        path = os.path.join(self.config.destination, key)
        return os.path.exists(path)

    def resolve_conflict(self, key):
        name, ext = key.rsplit('.', 1)
        count = 0
        while True:
            count = count + 1
            newname = '%s_%d.%s' % (name, count, ext)
            if not self.exists(newname):
                return newname


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

